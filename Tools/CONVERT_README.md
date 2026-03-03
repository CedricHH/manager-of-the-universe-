# Markdown to TinyMCE HTML Converter

Konvertiert Kapitel-Markdown-Dateien in TinyMCE-bereites HTML mit Erhaltung der ARMI-Systemnachrichten und deutschen Sonderzeichen.

## Verwendung

### Einzelnes Kapitel konvertieren

```powershell
.\Tools\convert_to_tinymce.bat Story\Chapters\Chapter_01_Dead_Capital.md
```

### Alle Kapitel konvertieren

```powershell
.\Tools\convert_to_tinymce.bat --all
```

Ausgabe: `Story/Chapters-HTML/` Verzeichnis mit `.html` Dateien

## Features

- ✅ **ARMI-Systemnachrichten** erhalten CSS-Klasse `armi-system-message`
- ✅ **Deutsche Sonderzeichen** (ä, ö, ü, ß, „") bleiben erhalten
- ✅ **Formatierungen** (Überschriften, Fett, Kursiv) werden korrekt übertragen
- ✅ **Metadaten** (YAML Frontmatter, Wortzähler) werden entfernt
- ✅ **Sauberes HTML** ohne Document-Wrapper (direkt für TinyMCE)

## CSS-Styling für ARMI-Nachrichten

Fügen Sie dies zu Ihrer TinyMCE Content-CSS hinzu:

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

## Voraussetzungen

```powershell
pip install markdown
```
