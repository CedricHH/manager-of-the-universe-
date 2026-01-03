# Guide: Automatisierte Manuskript-Zusammenführung

Dieses Dokument beschreibt, wie die einzelnen Kapiteldateien zu einem sauberen Gesamtmanuskript (`Resonanz_Der_naechste_Zyklus_Manuskript.md`) zusammengefügt werden.

## 1. Das Werkzeug
Das Skript befindet sich unter:
`g:\Meine Ablage\EBOOKS\Eigenes Buch\Tools\assemble_book.py`

Es handelt sich um ein Python-Skript, das speziell für dieses Buchprojekt konfiguriert wurde.

## 2. Automatische Bereinigungen
Beim Zusammenfügen führt das Skript folgende "Polishing"-Aufgaben automatisch durch:
*   **Metadaten-Entfernung**: Löscht Header-Informationen wie `**POV**:`, `**Ort**:`, `**Zeit**:`, `**Mythologischer Hintergrund**:` etc., damit diese nicht im Lesetext stehen.
*   **Szenen-Formatierung**:
    *   Entfernt Überschriften wie `## Szene 1`, da der Kapitelanfang für sich steht.
    *   Ersetzt fortlaufende Szenen-Überschriften (z.B. `## Szene 2`) durch literarische Trenner (`* * *`).
*   **Checklisten-Entfernung**: Schneidet alles ab dem Punkt `KONSISTENZ-CHECK` oder `Ende Kapitel` ab, um interne Notizen aus dem Manuskript fernzuhalten.
*   **Formatierung**: Fügt Seitenumbrüche (`\newpage` für PDF/LaTeX) und ein Titelblatt hinzu.

## 3. Ausführung
Um das Manuskript neu zu generieren (z.B. nach Überarbeitung eines Kapitels), führen Sie folgenden Befehl im Terminal (im Stammverzeichnis des Buches) aus:

```powershell
python "Tools\assemble_book.py"
```

Das Skript überschreibt die Datei `Resonanz_Der_naechste_Zyklus_Manuskript.md` automatisch mit der neuesten Version.

## 4. Konfiguration (Neue Kapitel hinzufügen)
Um neue Kapitel aufzunehmen oder die Reihenfolge zu ändern, öffnen Sie die Datei `Tools\assemble_book.py` in einem Texteditor.

Suchen Sie die Liste `chapter_files`:

```python
chapter_files = [
    "Kapitel_01_Volkov.md",
    "Kapitel_02_Die_scheiternde_Klimakonferenz.md",
    # ... weitere Kapitel
    "Kapitel_14_Lucas.md"
]
```

Fügen Sie einfach den Dateinamen des neuen Kapitels an der gewünschten Stelle in die Liste ein.

## 5. Voraussetzungen
*   Python muss installiert sein.
*   Die Kapiteldateien müssen im Ordner `Story/Chapters` liegen.

---

# Guide: EPUB-Konvertierung

Nach der Manuskript-Zusammenführung kann das Dokument in ein E-Book (EPUB) konvertiert werden.

## 1. Das Werkzeug
Das Skript befindet sich unter:
`g:\Meine Ablage\EBOOKS\Eigenes Buch\Tools\convert_to_epub.py`

## 2. Funktionen
Das Skript führt folgende Aufgaben automatisch durch:
*   **Cover einbetten**: Fügt `Cover.png` als Buchcover ein.
*   **Teaser/Zusammenfassung**: Liest die Beschreibung aus einer externen Datei (z.B. `Story/Prequel/Teaser.md`).
*   **Impressum**: Fügt automatisch eine Impressum-Seite mit Autor und Adresse ein.
*   **Kapitel-Splitting**: Trennt das Manuskript anhand von `# Kapitel`-Überschriften in separate Kapitel.
*   **Inhaltsverzeichnis**: Generiert automatisch ein navigierbares Inhaltsverzeichnis.

## 3. Ausführung (Standardaufruf für Teil I)

```powershell
python "Tools\convert_to_epub.py"
```

Das Skript erstellt `Resonanz_Der_naechste_Zyklus.epub` im Stammverzeichnis.

## 4. Erweiterte Nutzung (für weitere Teile)

Das Skript unterstützt Kommandozeilen-Argumente für Flexibilität:

```powershell
python "Tools\convert_to_epub.py" --teaser "Story/Teil_II/Teaser.md" --title "RESONANZ: Die Arena" --input "Manuskript_Teil2.md" --output "Resonanz_Teil2.epub" --cover "Cover_Teil2.png"
```

### Verfügbare Argumente:
| Argument   | Beschreibung                                      |
|------------|---------------------------------------------------|
| `--teaser` | Pfad zur Teaser/Zusammenfassung-Datei (relativ)   |
| `--title`  | Buchtitel                                         |
| `--input`  | Manuskript-Datei (relativ zum Stammverzeichnis)   |
| `--output` | Name der Ausgabe-EPUB-Datei                       |
| `--cover`  | Cover-Bilddatei (relativ zum Stammverzeichnis)    |

## 5. Teaser-Dateien
Für jeden Teil sollte eine eigene Teaser-Datei erstellt werden:
*   **Teil I**: `Story/Prequel/Teaser.md`
*   **Teil II**: `Story/Teil_II/Teaser.md` (zu erstellen)
*   usw.

Die Teaser-Datei sollte den Klappentext als Markdown enthalten. Das Skript extrahiert automatisch den reinen Text (ohne Überschriften).

## 6. Konfiguration (Standardwerte ändern)
Die Standardwerte können direkt im Skript unter `DEFAULT_CONFIG` (Zeilen 25-39) angepasst werden:

```python
DEFAULT_CONFIG = {
    'base_path': r"g:\Meine Ablage\EBOOKS\Eigenes Buch",
    'input_file': "Resonanz_Der_naechste_Zyklus_Manuskript1-14.md",
    'cover_file': "Cover.png",
    'teaser_file': "Story/Prequel/Teaser.md",
    'book_title': 'RESONANZ: Der nächste Zyklus',
    'book_author': 'Dr. Cedric Hawk Hinrichs',
    # ...
}
```

## 7. Voraussetzungen
*   Python muss installiert sein.
*   Benötigte Bibliotheken: `ebooklib`, `markdown`
    ```powershell
    pip install EbookLib markdown
    ```
