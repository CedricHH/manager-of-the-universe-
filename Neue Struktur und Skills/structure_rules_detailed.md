# Structure Rules - Detaillierte Struktur-Regeln

## Zweck
Diese Datei definiert die exakte Dateistruktur, YAML-Standards und Naming Conventions. Lade sie bei:
- Initial-Setup des Projekts
- Strukturfragen oder Problemen
- Wenn neue Elemente erstellt werden sollen

## Komplette Verzeichnisstruktur

```
/
├── PROJECT-CONTEXT.md          # Haupt-Kontext-Datei
├── WRITING-LOG.md              # Schreibfortschritt und Entscheidungen
├── /Meta
│   ├── CORE-RULES.md           # Kern-Regeln (immer laden)
│   ├── Structure-Rules.md      # Diese Datei
│   ├── Consistency-Rules.md    # Konsistenz-Checks
│   ├── Style-Rules.md          # Erzählstil
│   ├── Planning-Skill.md       # Skill: Planen
│   ├── Writing-Skill.md        # Skill: Schreiben
│   ├── Revision-Skill.md       # Skill: Überarbeiten
│   ├── Analysis-Skill.md       # Skill: Analyse
│   ├── Recherche.md            # Recherche-Notizen
│   └── Inspirationen.md        # Ideen-Sammlung
├── /Worldbuilding
│   ├── _INDEX.md               # Übersicht aller Elemente
│   ├── Magiesystem.md
│   ├── Orte.md
│   ├── Geschichte.md
│   ├── Technologie.md
│   ├── Gesellschaft.md
│   └── [Weitere Element-Dateien]
├── /Characters
│   ├── _INDEX.md               # Charakterübersicht
│   ├── _Relationships.md       # Beziehungsdiagramm
│   ├── [Charaktername].md      # Ein File pro Charakter
│   └── /Archive                # Verworfene Charaktere
│       └── [Alte Dateien]
├── /Plot
│   ├── _INDEX.md               # Plot-Übersicht
│   ├── Story-Outline.md        # ⭐ SINGLE SOURCE - Alle Kapitel
│   ├── Timeline.md             # Chronologische Ereignisse
│   ├── Handlungsstränge.md     # A/B/C-Plot Tracking
│   ├── Konflikte.md            # Zentrale Konflikte
│   └── Offene-Fragen.md        # Plot-Holes, zu klären
└── /Chapters
    ├── _INDEX.md               # Statistik
    ├── Kapitel-01.md           # Geschriebener Text
    ├── Kapitel-02.md
    └── ...
```

## YAML-Frontmatter Standards

### PROJECT-CONTEXT.md

```yaml
---
type: project
title: "[Buchtitel]"
genre: "[Fantasy, Sci-Fi, etc.]"
target_audience: "[YA, Adult, etc.]"
word_count_goal: 80000
current_word_count: 0  # Wird automatisch aktualisiert
status: "Planung" | "Entwurf" | "Revision" | "Fertig"
language: "de"
started: "2025-01-17"
---
```

**Inhalt:**
```markdown
# [Buchtitel]

## Ein-Satz-Pitch
[Dein Buch in einem Satz]

## Kern-Prämisse
[2-3 Sätze zur Hauptidee]

## Genre & Ton
**Genre:** [Fantasy, Sci-Fi, etc.]
**Zielgruppe:** [YA, Adult, etc.]
**Ton:** [Düster, Humorvoll, Episch, etc.]

## Wichtigste Regeln & Konsistenzen

### Magiesystem / Technologie / Besonderheiten
[Verweis auf Worldbuilding/[Element].md mit Kernprinzipien]

### Erzählweise
- **Perspektive:** Ich-Erzähler / Er/Sie-Erzähler / Multiperspektivisch
- **Zeitform:** Präsens / Vergangenheit
- **POV-Wechsel:** Fest / Pro Kapitel / Pro Szene

### Timeline-System
[Wie wird Zeit gemessen? Tage/Jahre/Eigenes System]
Siehe: Plot/Timeline.md

## Aktuelle Prioritäten
- [ ] [Aktuelle Schreibziele]
- [ ] [Zu klärende Plot-Fragen]
```

### Characters/[Name].md

```yaml
---
type: character
name: "Voller Name"
alias: ["Spitzname", "Titel"]
age: 28
gender: "männlich" | "weiblich" | "divers" | "andere"
role: "Hauptcharakter" | "Nebencharakter" | "Antagonist" | "Erwähnt"
first_appearance: "Kapitel-01"
last_appearance: "Kapitel-XX"  # Optional, falls nicht mehr auftretend
status: "lebendig" | "tot" | "unbekannt" | "verwandelt"
relationships:
  - character: "Andere Person"
    type: "Familie" | "Freund" | "Feind" | "Romantisch" | "Rivale" | "Mentor"
    description: "Kurze Beschreibung"
traits: ["mutig", "impulsiv", "loyal"]  # 3-5 Haupt-Traits
arc: "Kurze Beschreibung der Charakterentwicklung"
---
```

**Inhalt:**
```markdown
# [Name]

## Überblick
[2-3 Sätze wer diese Person ist]

## Aussehen
[Physische Beschreibung]

## Persönlichkeit
[Detaillierte Charakterzüge]

## Hintergrund
[Backstory]

## Motivation
[Was treibt den Charakter an?]

## Beziehungen
[Verweise auf andere Charaktere, Details]

## Entwicklung
### Zu Beginn der Story:
[Status, Haltung, Fähigkeiten]

### Nach Kapitel X:
[Entwicklung dokumentieren während des Schreibens]

## Besondere Fähigkeiten / Wissen
[Falls relevant]

## Notizen
[Wichtige Plot-bezogene Infos, Geheimnisse]
```

### Worldbuilding/[Element].md

```yaml
---
type: worldbuilding
category: "Ort" | "System" | "Geschichte" | "Kultur" | "Technologie"
name: "Name des Elements"
importance: "hoch" | "mittel" | "niedrig"
related_to: ["Andere Dokumente"]
introduced_in: "Kapitel-XX"
---
```

**Inhalt:** Frei, passend zum Element

### Plot/Story-Outline.md

```yaml
---
type: plot_outline
last_updated: "2025-01-17"
total_chapters: 28
acts: 3
---
```

**Inhalt:** Siehe detailliertes Format in Writing-Skill.md

### Chapters/Kapitel-XX.md (MINIMALES YAML!)

```yaml
---
type: chapter
number: 1
title: "Kapiteltitel"
pov: "Charaktername"
status: "Entwurf" | "Revision" | "Fertig"
word_count: 2500
timeline_date: "Tag X, Jahr Y"
---
```

**KEINE zusätzlichen Felder!** Alles andere lebt in Story-Outline.md

**Inhalt:** Der geschriebene Text des Kapitels

### Plot/Timeline.md

```yaml
---
type: timeline
chronology: "linear" | "non-linear"
time_system: "[Wie wird Zeit gemessen]"
---
```

**Inhalt:**
```markdown
# Timeline

## Tag/Jahr [X] - [Kurzbeschreibung]

**[Ereignis 1]** (Kapitel X)
- [Detail]
- [Detail]

**[Ereignis 2]** (Kapitel X)
- [Detail]

---

## Tag/Jahr [Y] - [Kurzbeschreibung]
[...]
```

### Plot/Handlungsstränge.md

```yaml
---
type: plot_threads
---
```

**Inhalt:**
```markdown
# Handlungsstränge

## A-Plot (Haupthandlung/Extern)
**Thema:** [z.B. "Kampf gegen den Antagonisten"]

### Setup (Kap X-Y):
[Wie beginnt dieser Thread]

### Entwicklung (Kap Y-Z):
[Wie entwickelt er sich]

### Auflösung (Kap Z-Ende):
[Wie wird er aufgelöst]

### Wichtige Kapitel:
- Kap X: [Ereignis]
- Kap Y: [Ereignis]

---

## B-Plot (Charakterentwicklung/Intern)
[Analog...]

---

## C-Plot (Beziehung/Subplot)
[Analog...]
```

### WRITING-LOG.md

```yaml
---
type: writing_log
---
```

**Inhalt:**
```markdown
# Writing Log

## [Datum - YYYY-MM-DD]

### [Was wurde gemacht] - [Status-Symbol]

**[Details]**

**Entscheidungen:**
- [Entscheidung 1]

**Offene Fragen:**
- [ ] [Frage]

---

## [Nächster Eintrag...]
```

## INDEX-Dateien Format

### Characters/_INDEX.md

```markdown
# Charakterübersicht

Letzte Aktualisierung: [Datum]

## Hauptcharaktere

| Name | Rolle | Status | Erster Auftritt | Charakterbogen |
|------|-------|--------|-----------------|----------------|
| [Name] | Protagonist | Lebendig | Kapitel-01 | [Kurzbeschreibung] |

## Nebencharaktere

[Analog]

## Antagonisten

[Analog]

## Beziehungen
Details: [_Relationships.md](_Relationships.md)
```

### Chapters/_INDEX.md

```markdown
# Kapitelübersicht

Letzte Aktualisierung: [Datum]

## Gesamt-Statistik
- **Ziel:** [X] Kapitel, [Y] Wörter
- **Geschrieben:** [A] Kapitel, [B] Wörter
- **Fortschritt:** [%]

## Kapitel-Liste

| # | Titel | POV | Wörter | Status | Kurz-Zusammenfassung |
|---|-------|-----|--------|--------|---------------------|
| 1 | [Titel] | [Name] | 2.500 | ✅ Fertig | [1 Satz] |
| 2 | [Titel] | [Name] | 2.300 | 🔄 Entwurf | [1 Satz] |

## Nächste Schritte
- [ ] [Aufgabe]
```

### Plot/_INDEX.md

```markdown
# Plot-Übersicht

Letzte Aktualisierung: [Datum]

## Zentrale Dokumente
- [Story-Outline.md](Story-Outline.md) - Komplette Kapitel-Outlines
- [Timeline.md](Timeline.md) - Chronologie
- [Handlungsstränge.md](Handlungsstränge.md) - A/B/C-Plots
- [Offene-Fragen.md](Offene-Fragen.md) - Zu klären

## Akt-Status
**Akt 1:** [Status] - Kap 1-8
**Akt 2:** [Status] - Kap 9-20
**Akt 3:** [Status] - Kap 21-28

## Wichtigste offene Fragen
- [ ] [Frage 1]
- [ ] [Frage 2]
```

### Worldbuilding/_INDEX.md

```markdown
# Worldbuilding-Übersicht

Letzte Aktualisierung: [Datum]

## Kategorien

### Orte
- [Ort 1](Orte.md#ort-1) - [Kurzbeschreibung]

### Systeme
- [System 1](System.md) - [Kurzbeschreibung]

### Geschichte
- [Epoche 1](Geschichte.md#epoche-1) - [Kurzbeschreibung]

### Kultur
- [Kultur 1](Kultur.md) - [Kurzbeschreibung]

## Konsistenz-Checks
- [ ] Alle Orte haben Beschreibungen
- [ ] Magiesystem-Regeln definiert
- [ ] Zeitrechnung festgelegt
```

## Naming Conventions

### Dateien
- **Charaktere:** `Vorname-Nachname.md` oder `Vorname.md`
  - Beispiele: `Elena-Morgenstern.md`, `Jakob.md`
- **Kapitel:** `Kapitel-01.md`, `Kapitel-02.md`, ... `Kapitel-99.md`
  - Mit führender Null bis 09
  - Ab 10 ohne führende Null
- **Worldbuilding:** `Beschreibender-Name.md`
  - Beispiele: `Magiesystem.md`, `Stadt-Shadowvale.md`
- **Keine Leerzeichen,** stattdessen Bindestriche `-`
- **Keine Umlaute** in Dateinamen (außer im Inhalt natürlich)
- **Lowercase für Ordner,** CamelCase für Dateien optional

### Interne Verweise (im Text)
- **Charakternamen:** Immer vollständiger Name beim ersten Verweis im Kapitel
- **Orte:** Exakt wie in Worldbuilding-Dateien definiert
- **Kapitel-Referenzen:** `Kapitel-XX` Format (mit Bindestrich)

## Status-Symbole

### Für Kapitel in Story-Outline.md:
- 📝 **Geplant** - Grobe Outline vorhanden
- 🎯 **Zu planen** - Nächster Planungsschritt, Details fehlen
- 🔄 **In Arbeit** - Wird gerade geschrieben
- ✅ **Geschrieben** - Entwurf fertig
- ✏️ **Revision** - Wird überarbeitet
- 🎉 **Fertig** - Abgeschlossen

### Für Projekt-Status:
- 🟢 **Aktiv** - Wird bearbeitet
- 🟡 **Pausiert** - Temporär auf Eis
- 🔴 **Blockiert** - Problem verhindert Fortschritt
- ✅ **Erledigt** - Abgeschlossen

## Workflow bei neuen Elementen

### Neuer Charakter erstellen:
1. Erstelle `/Characters/[Name].md` mit vollständigem YAML
2. Fülle Charakterprofil aus
3. Aktualisiere `/Characters/_INDEX.md`
4. Füge zu `/Characters/_Relationships.md` hinzu (falls relevant)
5. Falls bereits in Story erwähnt: Update `introduced_in` Feld

### Neues Worldbuilding-Element erstellen:
1. Bestimme Kategorie (Ort/System/Geschichte/Kultur/Technologie)
2. Erstelle `/Worldbuilding/[Name].md` mit YAML
3. Fülle Details aus
4. Aktualisiere `/Worldbuilding/_INDEX.md`
5. Falls wichtig für Story: Erwähne in `PROJECT-CONTEXT.md`

### Neues Kapitel erstellen:
**HINWEIS:** Dies geschieht automatisch durch Writing-Skill.md
1. Erstelle `/Chapters/Kapitel-XX.md` mit minimalem YAML
2. Füge geschriebenen Text ein
3. Aktualisiere `/Chapters/_INDEX.md` (Statistik)
4. Update `/Plot/Story-Outline.md` (Status)
5. Update `/Plot/Timeline.md` (neue Ereignisse)
6. Update `/WRITING-LOG.md` (Dokumentation)

## Backup & Archive

### Archive-Ordner nutzen:
- `/Characters/Archive/` - Verworfene Charaktere (nicht löschen!)
- Bei Bedarf auch `/Worldbuilding/Archive/`

### Backup-Empfehlung:
- Git-Repository nutzen
- Regelmäßig committen (z.B. nach jedem Kapitel)
- Branches für Experimente

## Struktur-Validierung

### Minimale funktionierende Struktur:
**Absolut notwendig:**
- PROJECT-CONTEXT.md
- Meta/CORE-RULES.md
- Plot/Story-Outline.md
- Chapters/_INDEX.md

**Sehr empfohlen:**
- Characters/_INDEX.md
- Plot/Timeline.md
- WRITING-LOG.md

**Optional aber nützlich:**
- Alle anderen Dateien

---

**Bei Strukturfragen oder -problemen: Diese Datei konsultieren!**
