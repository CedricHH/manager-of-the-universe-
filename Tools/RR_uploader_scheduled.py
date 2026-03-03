import os
import time
import random
import glob
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
INPUT_FOLDER = r"d:\current_projects\Der Manager des Universums\Story\Chapters-HTML"

# Die ID Ihrer Fiction
FICTION_ID = "147445" 

# Veröffentlichungs-Modus:
# 3 = "SCHEDULE" (Zeitgesteuert planen)
PUBLISH_MODE = 3 

# SCHEDULING OPTIONEN
# Wir setzen die Startzeit auf heute Abend 20:00 Uhr (English Timezone context: assuming user wants local evening)
# Da der User "jeden Abend" sagte, nutzen wir MINUTE_GAP = 1440 (24h)
now = datetime.now()
START_TIME = datetime(now.year, now.month, now.day, 20, 0)
if START_TIME < now:
    START_TIME += timedelta(days=1)

MINUTE_GAP = 1440

# DATEI-FILTER
START_CHAPTER = 56
END_CHAPTER = 60

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
    """Berechnet die Veröffentlichungszeit für das n-te Kapitel in 5-Minuten-Abständen."""
    release_dt = START_TIME + timedelta(minutes=index * MINUTE_GAP)
    return release_dt.strftime("%Y-%m-%d %H:%M")

def upload_chapter(driver, title, content, index_for_time):
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
        
        # 2. Inhalt über Source Code Editor eingeben
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

        # 3. Scheduling
        schedule_time = get_schedule_time(index_for_time)
        print(f"Plane Veröffentlichung für: {schedule_time}")
        
        sdate_field = driver.find_element(By.ID, "sdate")
        driver.execute_script("arguments[0].value = arguments[1];", sdate_field, schedule_time)
        driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", sdate_field)

        # 4. Absenden / Speichern (Save & Schedule)
        schedule_btn = driver.find_element(By.CSS_SELECTOR, "button[value='draft']")
        schedule_btn.click()

        time.sleep(random.uniform(3.0, 5.0))
        print(f"Status: '{title}' erfolgreich verarbeitet.")
        return True

    except Exception as e:
        print(f"FEHLER bei '{title}': {str(e)}")
        return False

def main():
    files = glob.glob(os.path.join(INPUT_FOLDER, "*.html"))
    if not files:
        print(f"Keine Dateien im Ordner {INPUT_FOLDER} gefunden!")
        return

    files = natsorted(files)

    # Filter nach Range (Chapter 1 bis 41)
    start_idx = START_CHAPTER - 1
    end_idx = END_CHAPTER if END_CHAPTER else len(files)
    files = files[start_idx:end_idx]
    print(f"Filtere Kapitel {START_CHAPTER} bis {END_CHAPTER}. ({len(files)} Dateien)")

    print(f"{len(files)} Kapitel werden verarbeitet. Bereit zum Upload.")

    driver = init_driver()

    try:
        driver.get("https://www.royalroad.com/account/login")
        print("\n" + "="*50)
        print("BITTE JETZT IM BROWSER EINLOGGEN.")
        print("Warte auf Login... (warte bis /home erreicht wird)")
        print("="*50)
        
        while "royalroad.com/home" not in driver.current_url:
            time.sleep(1)
        
        print("Login erkannt! Starte Upload...\n")

        for i, filepath in enumerate(files):
            title, content = read_file(filepath)
            success = upload_chapter(driver, title, content, i)
            
            if success:
                wait_time = random.uniform(10.0, 15.0) 
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
