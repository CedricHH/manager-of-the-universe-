
---
description: Schreibe ein vollständiges Kapitel aus einem Chapter-Outline (Szene für Szene)
---
# Workflow: Kapitel schreiben (Agentic)

> Transformiert ein Kapitel-Outline in ein vollständiges literarisches Kapitel (6.000-10.000 Wörter)

## Voraussetzungen

- Kapitel-Outline existiert in `Story/Chapter-Outline/Kapitel_XX_[Name].md`
- Charakter-Profil existiert in `Characters/`

---

## PHASE 1: Vorbereitung

### Schritt 1.1: Dateien laden

1. Lies das Kapitel-Outline: `Story/Chapter-Outline/Kapitel_XX_[Name].md`
2. Lies das Charakter-Profil: `Characters/Researcher_[Name].md` oder `Characters/Hero_[Name].md`
3. Lies den Writing-Prompt: `Story/CHAPTER_WRITING_PROMPT.md`
4. Optional: Relevante Dokumente aus `World/`, `Science/` je nach Kapitelinhalt

### Schritt 1.2: Charakter-Dossier erstellen

Erstelle ein kompaktes Dossier mit:

- Basisdaten (Alter, Nationalität, Beruf)
- Aktueller emotionaler Zustand für DIESE Szenen
- Kognitiver Filter (wie nimmt der Charakter die Welt wahr?)
- Persönliches Symbol
- Charakteristische Gesten/Ticks
- Dialog-Stil

### Schritt 1.3: Szenen identifizieren

Liste alle Szenen aus dem Outline:

- Szene 1: [Titel/Beschreibung]
- Szene 2: [Titel/Beschreibung]
- Szene 3: [Titel/Beschreibung]
- Cliffhanger: [Beschreibung]

---

## PHASE 2: Szenen-Expansion (ITERATIV)

### Für jede Szene wiederholen:

#### Schritt 2.1: Beat-Sheet erstellen

Vor dem Schreiben der Szene:

- Setting (Ort, Zeit, Atmosphäre, Sinneseindrücke)
- Emotionaler Bogen (Start → Wendepunkt → Ende)
- 5-7 Mikro-Beats (was passiert konkret?)
- Sensorische Pflicht-Details (mind. 5 Sinne abdecken)
- Foreshadowing/Seeds
- Subtext (was wird NICHT gesagt?)

#### Schritt 2.2: Szene schreiben

- Ziel: 1.500 - 2.500 Wörter
- Struktur: Einstieg (150-300) → Entwicklung (800-1500) → Höhepunkt (200-400) → Transition (100-200)
- Stil: Gemäß CHAPTER_WRITING_PROMPT.md

// turbo

#### Schritt 2.3: Szenen-Check

Nach jeder Szene prüfen:

- [ ] POV-Disziplin eingehalten?
- [ ] Mind. 5 sensorische Details?
- [ ] Keine KI-Klischees?
- [ ] Kognitiver Filter durchgängig?
- [ ] Subtext in Dialogen?
- [ ] Wortanzahl erreicht?

Bei Mängeln: Überarbeiten bevor nächste Szene

#### Schritt 2.4: Speichern

Speichere jede fertige Szene in:
`Story/Chapters/Kapitel_XX_[Name]_Szene_Y.md`

---

## PHASE 3: Integration

### Schritt 3.1: Szenen zusammenführen

Kombiniere alle Szenen zu einem Kapitel:
`Story/Chapters/Kapitel_XX_[Name].md`

### Schritt 3.2: Übergänge glätten

- Prüfe Szenenübergänge
- Füge `***` als Szenentrenner ein wo nötig
- Eliminiere Wiederholungen

### Schritt 3.3: Konsistenz-Check

- [ ] Timeline korrekt? (World/Timeline_Chronology.md)
- [ ] Charakterdetails korrekt? (Character-Profil)
- [ ] Keine Plotholes? (Story/Plothole_Solutions.md)

### Schritt 3.4: Finale Politur

- Hook stark genug?
- Cliffhanger wie im Outline?

---

## PHASE 4: FEEDBACK-SCHLEIFE (PFLICHT)

> **Diese Phase ist PFLICHT und wird wiederholt bis alle Kriterien erfüllt sind.**

### Schritt 4.1: Wortanzahl verifizieren

// turbo

```powershell
powershell -ExecutionPolicy Bypass -File "g:\Meine Ablage\EBOOKS\Eigenes Buch\Tools\count-words.ps1" "[KAPITEL-PFAD]"
```

**Zielbereich: 6.000-10.000 echte Wörter**

### Schritt 4.2: Quantitäts-Feedback-Schleife

```
WIEDERHOLE solange word_count < 6000:
    1. Identifiziere schwächste Szene (kürzeste oder dünnste)
    2. Erweitere mit:
       - Mind. 2 zusätzliche sensorische Details
       - 1 tieferer Flashback/Backstory-Moment
       - 1 erweiterter innerer Monolog
    3. Speichere Änderungen
    4. Führe count-words.ps1 erneut aus
    5. Dokumentiere: "[Szene X] +[N] Wörter hinzugefügt"
ENDE WIEDERHOLE
```

### Schritt 4.3: Qualitäts-Checkliste

Nach Erreichen des Wortziels, prüfe:

| Kriterium                                                | Bestanden? |
| -------------------------------------------------------- | ---------- |
| POV-Disziplin: Kein Gedankenlesen anderer Charaktere     | ☐         |
| 5+ Sinneseindrücke pro Szene                            | ☐         |
| Keine KI-Klischees ("ein Schauer lief...", "Herz raste") | ☐         |
| Kognitiver Filter durchgängig spürbar                  | ☐         |
| Dialoge mit Subtext (nicht zu direkt)                    | ☐         |
| Foreshadowing-Seeds aus Outline eingebaut                | ☐         |
| Hook zieht in ersten 3 Sätzen                           | ☐         |
| Cliffhanger erzeugt Spannung                             | ☐         |

### Schritt 4.4: Qualitäts-Korrektur-Schleife

```
FÜR JEDES nicht bestandenes Kriterium:
    1. Lokalisiere problematische Stellen
    2. Überarbeite gezielt
    3. Markiere als geprüft
ENDE FÜR
```

### Schritt 4.5: Finale Validierung

// turbo

1. Letzte Wortanzahl-Prüfung:

```powershell
powershell -ExecutionPolicy Bypass -File "g:\Meine Ablage\EBOOKS\Eigenes Buch\Tools\count-words.ps1" "[KAPITEL-PFAD]"
```

2. Bestätige:

   - ☐ Wortanzahl ≥ 6.000
   - ☐ Alle Qualitätskriterien bestanden
   - ☐ Konsistenz-Check am Ende der Datei eingefügt
3. Status-Report an User:

```
✅ Kapitel X fertig
   Wortanzahl: [XXXX] Wörter
   Qualitäts-Score: [X]/8 Kriterien
```

---

## Ausgabe

Das fertige Kapitel liegt in:

```
Story/Chapters/Kapitel_XX_[Name].md
```

Mit Metadaten + Konsistenz-Check am Ende:

```markdown
# Kapitel X: [Titel]

**POV**: [Name]
**Ort**: [Location]
**Zeit**: [Timeline]
**Wortanzahl**: [XXXX]

---

[Kapiteltext...]

---

*Ende Kapitel X*

---

## KONSISTENZ-CHECK

☑ Timeline korrekt
☑ Charakterdetails korrekt
☑ Foreshadowing eingebaut
☑ Cliffhanger vorhanden
```

---

## Quick-Start

Sage einfach:

```
/write-chapter Kapitel 1
```

Oder:

```
Schreibe Kapitel 3 (Kaia) gemäß dem Workflow
```
