import os
from datetime import datetime
import re

# Configuration
base_path = r"g:\Meine Ablage\EBOOKS\Eigenes Buch\Story\Chapters"
output_path = r"g:\Meine Ablage\EBOOKS\Eigenes Buch\Resonanz_Der_naechste_Zyklus_Manuskript.md"

book_title = "RESONANZ"
subtitle = "Der nächste Zyklus"

chapter_files = [
    "Kapitel_01_Volkov.md",
    "Kapitel_02_Die_scheiternde_Klimakonferenz.md",
    "Kapitel_03_Chen.md",
    "Kapitel_04_Kaia.md",
    "Kapitel_05_Amara.md",
    "Kapitel_06_Nyx.md",
    "Kapitel_07_Tanaka.md",
    "Kapitel_08_Der_Weg_durch_die_Wueste.md",
    "Kapitel_09_Yara.md",
    "Kapitel_10_Mandla.md",
    "Kapitel_11_Rebecca.md",
    "Kapitel_12_Mei.md",
    "Kapitel_13_Weber.md",
    "Kapitel_14_Lucas.md"
]

def clean_chapter_content(content):
    lines = content.splitlines()
    cleaned_lines = []
    
    # Metadata markers (extended list)
    db_markers = [
        "**POV**:", "**Ort**:", "**Zeit**:", "**Wortanzahl**:", 
        "**Mythologischer Hintergrund**", "**Mythologischer Analog**", 
        "**Fähigkeit**", "**Fähigkeiten**", "**Kern-Konzept**",
        "**ENDE KAPITEL", "**Qualitäts-Score", "**Qualität"
    ]
    
    # Regex for Scene Headers
    scene_header_pattern = re.compile(r'^#{1,6}\s+Szene\s+\d+.*', re.IGNORECASE)
    
    stop_processing = False
    
    for line in lines:
        stripped = line.strip()
        
        # 1. Check for CUT-OFF points
        if "KONSISTENZ-CHECK" in stripped or "Ende Kapitel" in stripped and not stripped.startswith("**"):
             # Note: "Ende Kapitel" might be in "**ENDE KAPITEL...**". 
             # If it is simple "Ende Kapitel 1" (often used as footer), we stop.
             # But if it is "**ENDE KAPITEL...**", we might want to filter it but NOT stop if there is text after?
             # Actually, usually nothing comes after.
             pass
        
        # Consistent stop trigger:
        if "KONSISTENZ-CHECK" in stripped:
            stop_processing = True
            
        if stop_processing:
            break
            
        # 2. Filter out Metadata
        is_metadata = False
        for marker in db_markers:
            if marker in stripped:
                is_metadata = True
                break
        if is_metadata:
            continue
            
        # 3. Handle Scene Headers
        if scene_header_pattern.match(stripped):
            if "Szene 1" in stripped or "Szene 01" in stripped:
                continue 
            else:
                cleaned_lines.append("\n* * *\n")
                continue
                
        # 4. Filter out isolated separators at START
        if (stripped == "---" or stripped == "***") and len(cleaned_lines) < 20:
             has_text = False
             for past_line in cleaned_lines:
                 p_strip = past_line.strip()
                 if p_strip.startswith("#"): continue
                 if len(p_strip) > 3 and not p_strip.startswith("-") and not p_strip == "---" and not p_strip.startswith("* * *"): 
                     has_text = True
                     break
             if not has_text:
                 continue

        cleaned_lines.append(line)
        
    text = "\n".join(cleaned_lines)
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    
    return text

def create_title_page():
    return f"""
<br>
<br>
<br>
<br>
<br>
<h1 style="text-align: center;">{book_title}</h1>
<h3 style="text-align: center;">{subtitle}</h3>
<br>
<br>
<p style="text-align: center;">Manuskript - Stand: {datetime.now().strftime('%d.%m.%Y')}</p>
<div style="page-break-after: always;"></div>
\\newpage
"""

def assemble():
    full_content = []
    full_content.append(create_title_page())
    
    for filename in chapter_files:
        path = os.path.join(base_path, filename)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                raw_content = f.read()
                cleaned = clean_chapter_content(raw_content)
                full_content.append(f"\n\n<div style='page-break-after: always;'></div>\n\\newpage\n\n{cleaned}")
                print(f"Processed and Added {filename}")
        else:
            print(f"WARNING: Could not find {path}")

    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write("".join(full_content))
    
    print(f"Successfully created cleaned manuscript at: {output_path}")

if __name__ == "__main__":
    assemble()
