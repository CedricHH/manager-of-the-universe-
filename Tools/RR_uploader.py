import os
import time
import random
import glob
import argparse
from natsort import natsorted 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta

# --- KONFIGURATION START ---

# Pfad zu Ihrem Ordner mit den HTML-Dateien
INPUT_FOLDER = r"g:\Meine Ablage\EBOOKS\Der Manager des Universums\Story\Chapters-HTML"

# Die ID Ihrer Fiction
FICTION_ID = "147445" 

# SCHEDULING OPTIONEN (Nur relevant wenn PUBLISH_MODE = 3)
START_DATE = "2026-01-10"    # Format: YYYY-MM-DD
CHAPTERS_PER_DAY = 10        # Wie viele Kapitel pro Tag?
FIRST_HOUR = 8               # Erste Veröffentlichung um wie viel Uhr?
HOUR_GAP = 1                 # Abstand zwischen Kapitelexemplaren in Stunden

# --- KONFIGURATION ENDE ---

def init_driver():
    print("Starte Browser...")
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def read_file(filepath):
    """Liest Titel und Inhalt aus einer HTML-Datei."""
    filename = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    import re
    title_match = re.search(r'<h1>(.*?)</h1>', content, re.IGNORECASE)
    if title_match:
        title = title_match.group(1).strip()
        content = re.sub(r'<h1>.*?</h1>', '', content, count=1, flags=re.IGNORECASE)
    else:
        title = os.path.splitext(filename)[0].replace("_", " ")
        print(f"WARNUNG: Kein <h1> Titel in {filename} gefunden. Nutze Dateiname: {title}")

    return title, content.strip()

def get_schedule_time(index):
    """Berechnet die Veröffentlichungszeit für das n-te Kapitel."""
    start_dt = datetime.strptime(START_DATE, "%Y-%m-%d")
    
    days_offset = index // CHAPTERS_PER_DAY
    hours_offset = (index % CHAPTERS_PER_DAY) * HOUR_GAP
    
    release_dt = start_dt + timedelta(days=days_offset, hours=FIRST_HOUR + hours_offset)
    return release_dt.strftime("%Y-%m-%d %H:%M")

def upload_chapter(driver, title, content, index_for_time, publish_mode):
    print(f"Verarbeite: {title}")
    
    url = f"https://www.royalroad.com/author-dashboard/chapters/new/{FICTION_ID}"
    driver.get(url)
    
    time.sleep(random.uniform(3.0, 5.0))

    try:
        # 1. Titel eingeben
        title_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "Title"))
        )
        title_field.clear()
        title_field.send_keys(title)
        
        # 2. Inhalt über Source Code Editor eingeben (CHAPTER CONTENT, nicht Pre-chapter note!)
        # Es gibt 3 Editoren auf der Seite. Wir brauchen den zweiten (Chapter Content).
        source_code_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div/div[6]/div/div/div[1]/div[1]/div[1]/div/div[7]/button[2]"))
        )
        source_code_btn.click()
        
        textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.tox-textarea"))
        )
        
        driver.execute_script("arguments[0].value = arguments[1];", textarea, content)
        textarea.send_keys(" ") 
        
        save_btn = driver.find_element(By.CSS_SELECTOR, ".tox-dialog__footer-end button.tox-button:nth-child(2)")
        save_btn.click()
        
        time.sleep(random.uniform(1.0, 2.0))

        # 3. Scheduling (falls gewünscht)
        if publish_mode == 3:
            schedule_time = get_schedule_time(index_for_time)
            print(f"Plane Veröffentlichung für: {schedule_time}")
            
            sdate_field = driver.find_element(By.ID, "sdate")
            driver.execute_script("arguments[0].value = arguments[1];", sdate_field, schedule_time)
            driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", sdate_field)

        # 4. Absenden / Speichern
        if publish_mode == 3:
            # "Save & Schedule" Button verwenden
            schedule_btn = driver.find_element(By.CSS_SELECTOR, "button[value='draft']")
            schedule_btn.click()
        elif publish_mode == 2:
            # Sofort veröffentlichen
            publish_btn = driver.find_element(By.CSS_SELECTOR, "button[value='publish']")
            publish_btn.click()
        else:
            # Nur als Entwurf speichern (ohne Schedule)
            draft_btns = driver.find_elements(By.CSS_SELECTOR, "button")
            found_draft = False
            for btn in draft_btns:
                if "Save Draft" in btn.text:
                    btn.click()
                    found_draft = True
                    break
            if not found_draft:
                print("Warnung: 'Save Draft' Button nicht gefunden.")

        time.sleep(random.uniform(3.0, 5.0))
        print(f"Status: '{title}' erfolgreich verarbeitet.")
        return True

    except Exception as e:
        print(f"FEHLER bei '{title}': {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Royal Road Uploader')
    parser.add_argument('--start', type=int, help='Start chapter number')
    parser.add_argument('--end', type=int, help='End chapter number')
    parser.add_argument('--mode', type=int, default=2, choices=[1, 2, 3], 
                        help='Publish mode: 1=Draft, 2=Publish, 3=Schedule')
    
    # Scheduling arguments
    parser.add_argument('--date', type=str, help='Start Date (YYYY-MM-DD)')
    parser.add_argument('--time', type=int, default=8, help='First Hour (0-23)')
    parser.add_argument('--gap', type=int, default=1, help='Gap in hours')

    args = parser.parse_args()

    # Update Global Configs if args provided
    if args.date:
        global START_DATE
        START_DATE = args.date
    if args.time:
        global FIRST_HOUR
        FIRST_HOUR = args.time
    if args.gap:
        global HOUR_GAP
        HOUR_GAP = args.gap

    files = glob.glob(os.path.join(INPUT_FOLDER, "*.html"))
    if not files:
        print(f"Keine Dateien im Ordner {INPUT_FOLDER} gefunden!")
        return

    files = natsorted(files)

    # Filter nach Range
    if args.start:
        start_idx = args.start - 1
        end_idx = args.end if args.end else len(files)
        # Verify bounds
        if start_idx < 0: start_idx = 0
        
        # Slicing logic depends on chapters being in order and matching index+1
        # More robust approach: Filter by filename
        filtered_files = []
        import re
        for f in files:
            # Extract number from filename (e.g. Chapter_47_...)
            match = re.search(r'Chapter_(\d+)', os.path.basename(f))
            if match:
                num = int(match.group(1))
                if args.end:
                    if args.start <= num <= args.end:
                        filtered_files.append(f)
                else:
                    if num >= args.start:
                        filtered_files.append(f)
        
        files = filtered_files
        print(f"Filtere Kapitel {args.start} bis {args.end if args.end else 'Ende'}. ({len(files)} Dateien)")

    if not files:
        print("Keine Dateien im gewählten Bereich gefunden.")
        return

    print(f"{len(files)} Kapitel werden verarbeitet. Modus: {args.mode}. Bereit zum Upload.")

    driver = init_driver()

    try:
        driver.get("https://www.royalroad.com/account/login")
        print("\n" + "="*50)
        print("BITTE JETZT IM BROWSER EINLOGGEN.")
        print("Warte auf Login... (warte bis /home erreicht wird)")
        print("="*50)
        
        # Warte bis wir auf royalroad.com/home angekommen sind
        while "royalroad.com/home" not in driver.current_url:
            time.sleep(1)
        
        print("Login erkannt! Starte Upload...\n")

        # Wir nutzen i als relativen Index für die Scheduling-Zeiten (0, 1, 2...)
        for i, filepath in enumerate(files):
            title, content = read_file(filepath)
            success = upload_chapter(driver, title, content, i, args.mode)
            
            if success:
                wait_time = random.uniform(20.0, 30.0) 
                print(f"Warte {wait_time:.1f} Sekunden...")
                time.sleep(wait_time)
            else:
                print("Abbruch oder Fehler. Drücken Sie Enter zum Fortfahren.")
                input() 

    except KeyboardInterrupt:
        print("Vorgang vom Benutzer abgebrochen.")
    finally:
        print("Fertig. Browser bleibt offen zur Kontrolle.")

if __name__ == "__main__":
    main()
