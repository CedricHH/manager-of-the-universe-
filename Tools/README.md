# Tools Directory

**Werkzeuge für "Der Manager des Universums" Webnovel-Projekt**

Diese Sammlung von Skripten automatisiert den gesamten Workflow von der Kapitelbearbeitung bis zur Veröffentlichung auf Royal Road und eBook-Erstellung.

---

## 📋 Inhaltsverzeichnis

- [Kapitelbearbeitung](#kapitelbearbeitung)
- [HTML-Konvertierung](#html-konvertierung)
- [Royal Road Upload](#royal-road-upload)
- [eBook-Erstellung](#ebook-erstellung)
- [Version Control](#version-control)
- [Konfiguration](#konfiguration)

---

## 📝 Kapitelbearbeitung

### `count-words.bat` / `count-words.ps1`

**Zweck**: Präzise Wortzählung für Kapitel unter Ausschluss von Metadaten und Formatierung.

**Verwendung**:

```powershell
.\Tools\count-words.bat "Story/Chapters/Chapter_XX_Name.md"
```

**Features**:

- ✅ Liest Zielwerte aus `PROJECT.md`
- ✅ Entfernt YAML-Frontmatter, Session Summaries und Metadaten
- ✅ Bereinigt Markdown-Formatierung für echte Wortzählung
- ✅ Zeigt Abweichung vom Zielbereich (1500-1800 Wörter)

**Ausgabe-Beispiel**:

```
=== WORTANZAHL ===
Datei: Chapter_44_Liquidation_Event.md

Woerter:   1742
Ziel:      1500 - 1800

[OK] Im Zielbereich!
```

> [!IMPORTANT]
> **MANDATORY**: Dieses Skript MUSS für Wortzählungen verwendet werden. Nutzen Sie NICHT `Measure-Object` oder andere PowerShell-Befehle direkt!

---

### `add-chapter-footers.ps1`

**Zweck**: Fügt automatisch Fußzeilen mit Wortzahl und nächstem Kapitel zu Kapiteldateien hinzu.

**Verwendung**:

```powershell
.\Tools\add-chapter-footers.ps1 -StartChapter 16 -EndChapter 116
```

**Features**:

- Berechnet Wortzahl über `count-words.bat`
- Fügt Verweis auf nächstes Kapitel hinzu
- Überspringt bereits vorhandene Fußzeilen
- Batch-Verarbeitung mehrerer Kapitel

---

## 🌐 HTML-Konvertierung

### `convert_to_tinymce.bat` / `convert_to_tinymce.py`

**Zweck**: Konvertiert Markdown-Kapitel in TinyMCE-bereites HTML für Royal Road.

**Verwendung**:

```powershell
# Einzelnes Kapitel
.\Tools\convert_to_tinymce.bat "Story\Chapters\Chapter_01_Dead_Capital.md"

# Alle Kapitel
.\Tools\convert_to_tinymce.bat --all
```

**Ausgabe**: `Story/Chapters-HTML/` mit `.html` Dateien

**Features**:

- ✅ **ARMI-Systemnachrichten** erhalten CSS-Klasse `armi-system-message`
- ✅ **Deutsche Sonderzeichen** (ä, ö, ü, ß, „") bleiben erhalten
- ✅ **Formatierungen** korrekt übertragen
- ✅ **Metadaten** (YAML, Word Count) werden entfernt
- ✅ **Sauberes HTML** ohne Document-Wrapper

**CSS für ARMI-Nachrichten**:

```css
blockquote.armi-system-message {
    font-family: 'Courier New', monospace;
    background-color: #f0f8ff;
    border-left: 4px solid #4682b4;
    padding: 10px 15px;
    margin: 15px 0;
    color: #2c3e50;
}
```

**Voraussetzungen**:

```powershell
pip install markdown
```

Siehe auch: [CONVERT_README.md](file:///G:/Meine%20Ablage/EBOOKS/Der%20Manager%20des%20Universums/Tools/CONVERT_README.md)

---

## 🚀 Royal Road Upload

### `RR_uploader.py`

**Zweck**: Automatisiertes Hochladen von Kapiteln zu Royal Road mit Scheduling-Funktionen.

**Features**:

- 3 Veröffentlichungs-Modi:
  - **DRAFT**: Nur als Entwurf speichern
  - **PUBLISH_NOW**: Sofort veröffentlichen
  - **SCHEDULE**: Zeitgesteuert planen
- Automatisches Lesen von Titel aus `<h1>` Tags
- Zufällige Wartezeiten zwischen Uploads (Anti-Bot)
- Kapitelbereich-Filter (z.B. nur Kapitel 11-40)

**Konfiguration** (in `RR_uploader.py`):

```python
INPUT_FOLDER = r"g:\Meine Ablage\EBOOKS\Der Manager des Universums\Story\Chapters-HTML"
FICTION_ID = "147445"
PUBLISH_MODE = 3  # 1=DRAFT, 2=PUBLISH_NOW, 3=SCHEDULE

# Scheduling Optionen
START_DATE = "2026-01-10"
CHAPTERS_PER_DAY = 10
FIRST_HOUR = 8
HOUR_GAP = 1

# Filter
START_CHAPTER = 11
END_CHAPTER = 40
```

**Verwendung**:

```powershell
python Tools\RR_uploader.py
```

Das Skript öffnet einen Browser, wartet auf manuelles Login und startet dann den Upload.

**Voraussetzungen**:

```powershell
pip install selenium webdriver-manager natsort
```

---

### `RR_uploader_scheduled.py`

**Zweck**: Vereinfachte Version für tägliche Einzelkapitel-Uploads.

**Unterschiede zu `RR_uploader.py`**:

- Nur SCHEDULE-Modus
- Startet 5 Minuten in der Zukunft
- `MINUTE_GAP = 1440` (1 Tag zwischen Kapiteln)
- Optimiert für kontinuierliche Release-Zeitpläne

**Konfiguration**:

```python
START_TIME = datetime.now() + timedelta(minutes=5)
MINUTE_GAP = 1440  # 24 Stunden
START_CHAPTER = 42
END_CHAPTER = 44
```

**Verwendung**:

```powershell
python Tools\RR_uploader_scheduled.py
```

---

## 📚 eBook-Erstellung

### `generate_ebook.bat`

**Zweck**: All-in-One Pipeline für EPUB-Erstellung.

**Schritte**:

1. Führt `assemble_book.py` aus (Manuskript-Zusammenfügung)
2. Führt `convert_to_epub.py` aus (EPUB-Konvertierung)

**Verwendung**:

```powershell
.\Tools\generate_ebook.bat
```

**Ausgabe**:

- `Manager_of_Universe_Arc1_Manuscript.md`
- `Manager_of_Universe_Arc1.epub`

---

### `assemble_book.py`

**Zweck**: Fügt einzelne Kapitel zu einem Gesamtmanuskript zusammen.

**Automatische Bereinigungen**:

- Entfernt Metadaten (`POV`, `Ort`, `Zeit`, etc.)
- Entfernt Szenen-Überschriften (`## Szene 1`)
- Ersetzt fortlaufende Szenen durch literarische Trenner (`* * *`)
- Schneidet Checklisten ab (`KONSISTENZ-CHECK`, `Ende Kapitel`)
- Fügt Seitenumbrüche und Titelblatt hinzu

**Konfiguration**: Liste `chapter_files` im Skript bearbeiten

Siehe: [GUIDE_MANUSCRIPT_ASSEMBLY.md](file:///G:/Meine%20Ablage/EBOOKS/Der%20Manager%20des%20Universums/Tools/GUIDE_MANUSCRIPT_ASSEMBLY.md)

---

### `convert_to_epub.py`

**Zweck**: Konvertiert Manuskript in EPUB-Format.

**Features**:

- Cover einbetten (`Cover.png`)
- Teaser/Zusammenfassung aus Datei lesen
- Automatisches Impressum
- Kapitel-Splitting anhand von `# Kapitel`-Überschriften
- Navigierbares Inhaltsverzeichnis

**Verwendung**:

```powershell
# Standard (Teil I)
python Tools\convert_to_epub.py

# Erweitert (weitere Teile)
python Tools\convert_to_epub.py --teaser "Story/Teil_II/Teaser.md" --title "RESONANZ: Die Arena" --input "Manuskript_Teil2.md" --output "Resonanz_Teil2.epub" --cover "Cover_Teil2.png"
```

**Voraussetzungen**:

```powershell
pip install EbookLib markdown
```

Siehe: [GUIDE_MANUSCRIPT_ASSEMBLY.md](file:///G:/Meine%20Ablage/EBOOKS/Der%20Manager%20des%20Universums/Tools/GUIDE_MANUSCRIPT_ASSEMBLY.md)

---

### `convert_to_docx.py`

**Zweck**: Konvertiert Manuskript in DOCX-Format (Microsoft Word).

**Features**:

- Profesionelle Formatierung
- Kapitelüberschriften
- Seitenumbrüche
- Kompatibel mit Word/LibreOffice

**Voraussetzungen**:

```powershell
pip install python-docx markdown
```

---

## 🔄 Version Control

### `git-commit.bat`

**Zweck**: Automatisiertes Git-Commit und Push für Projektdateien.

**Verwendung**:

```powershell
.\Tools\git-commit.bat
```

**Staged Directories**:

- `Story/Chapters/`
- `Story/LECTOR_LOGS/`
- `Story/Sync_Reports/`
- `Characters/`
- `World/`

**Commit Message**: `"written, analyzed, synced"`

> [!IMPORTANT]
> **MANDATORY**: Verwenden Sie dieses Skript für Commits. Nutzen Sie NICHT manuelle Git-Befehle!

---

## ⚙️ Konfiguration

### Gemeinsame Pfade

Alle Skripte verwenden den Basis-Pfad:

```
g:\Meine Ablage\EBOOKS\Der Manager des Universums
```

### Wichtige Verzeichnisse

| Verzeichnis | Zweck |
|-------------|-------|
| `Story/Chapters/` | Markdown-Kapitel |
| `Story/Chapters-HTML/` | Konvertierte HTML-Dateien |
| `Tools/` | Skripte (dieses Verzeichnis) |
| `Characters/` | Charakterprofile |
| `World/` | Worldbuilding-Dateien |

### PROJECT.md Integration

Mehrere Tools lesen Konfiguration aus `PROJECT.md`:

- `count-words.ps1` → Liest `Words per Chapter` Zielwerte
- `assemble_book.py` → Liest Kapitelreihenfolge
- `convert_to_epub.py` → Liest Metadaten (Titel, Autor)

---

## 🔧 Technische Details

### Selenium-basierte Tools

**`RR_uploader.py`** und **`RR_uploader_scheduled.py`** nutzen:

- Selenium WebDriver mit Chrome
- XPath für TinyMCE-Editor-Navigation
- WebDriverWait für robustes Element-Handling

**Wichtige Selektoren**:

- Titel-Feld: `#Title`
- Source Code Button: `/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div/div[6]/div/div/div[1]/div[1]/div[1]/div/div[7]/button[2]`
- Schedule-Feld: `#sdate`

### Python-Dependencies

Komplette Liste:

```powershell
pip install markdown EbookLib python-docx selenium webdriver-manager natsort
```

---

## 📖 Weiterführende Dokumentation

- [CONVERT_README.md](file:///G:/Meine%20Ablage/EBOOKS/Der%20Manager%20des%20Universums/Tools/CONVERT_README.md) - HTML-Konvertierung Details
- [GUIDE_MANUSCRIPT_ASSEMBLY.md](file:///G:/Meine%20Ablage/EBOOKS/Der%20Manager%20des%20Universums/Tools/GUIDE_MANUSCRIPT_ASSEMBLY.md) - Manuskript-Zusammenfügung & EPUB-Erstellung
- [elements und selector.md](file:///G:/Meine%20Ablage/EBOOKS/Der%20Manager%20des%20Universums/Tools/elements%20und%20selector.md) - Royal Road Element-Selektoren

---

## 🎯 Typischer Workflow

### Neues Kapitel veröffentlichen

1. **Kapitel schreiben**:

   ```powershell
   # Kapitel in Story/Chapters/ erstellen
   ```

2. **Wortzählung prüfen**:

   ```powershell
   .\Tools\count-words.bat "Story\Chapters\Chapter_XX_Name.md"
   ```

3. **Zu HTML konvertieren**:

   ```powershell
   .\Tools\convert_to_tinymce.bat "Story\Chapters\Chapter_XX_Name.md"
   ```

4. **Zu Royal Road hochladen**:

   ```powershell
   # RR_uploader.py konfigurieren (START_CHAPTER, END_CHAPTER)
   python Tools\RR_uploader_scheduled.py
   ```

5. **Änderungen committen**:

   ```powershell
   .\Tools\git-commit.bat
   ```

### eBook erstellen (Arc abgeschlossen)

1. **Manuskript zusammenfügen & EPUB erstellen**:

   ```powershell
   .\Tools\generate_ebook.bat
   ```

2. **Alternativ: Einzelschritte**:

   ```powershell
   python Tools\assemble_book.py
   python Tools\convert_to_epub.py
   python Tools\convert_to_docx.py  # Optional: Word-Version
   ```

---

## 🐛 Troubleshooting

### `count-words.ps1` findet PROJECT.md nicht

- Stellen Sie sicher, dass Sie im Stammverzeichnis des Projekts sind
- Das Skript sucht bis zu 5 Ebenen nach oben

### Royal Road Upload schlägt fehl

- Überprüfen Sie `FICTION_ID` in den Uploader-Skripten
- Stellen Sie sicher, dass Sie nach dem Login auf `/home` weitergeleitet werden
- Bei XPath-Fehlern: Royal Road könnte das HTML geändert haben (siehe `elements und selector.md`)

### EPUB-Erstellung schlägt fehl

- Überprüfen Sie, ob `Cover.png` existiert
- Stellen Sie sicher, dass Teaser-Datei vorhanden ist
- Prüfen Sie Python-Dependencies: `pip list | findstr -i "ebook markdown"`

---

## 📝 Lizenz und Autor

**Projekt**: Der Manager des Universums  
**Autor**: Dr. Cedric Hawk Hinrichs  
**Repository**: [GitHub](https://github.com/CedricHH/manager-of-the-universe-)

---

**Letzte Aktualisierung**: 2026-01-22
