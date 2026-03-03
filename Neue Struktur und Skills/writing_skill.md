# Writing Skill - Kapitel schreiben

## Zweck
Dieser Skill definiert wie du Kapitel schreibst UND synchronisierst. Er wird aktiviert wenn der Autor sagt:
- "Schreibe Kapitel X"
- "Verfasse Kapitel X"
- "Schreib Kapitel X basierend auf der Outline"

## Workflow: Kapitel schreiben

### SCHRITT 1: Kontext laden (automatisch, ohne zu fragen)

**Basis-Kontext:**
```
@Meta/CORE-RULES.md
@Plot/Story-Outline.md
@Plot/Timeline.md
```

**Stil-Richtlinien (falls vorhanden):**
```
@Meta/Style-Rules.md
```

### SCHRITT 2: Outline analysieren

1. **Finde Kapitel X in Story-Outline.md**
2. **Prüfe Status:**
   - 📝 Geplant (detailliert)? → GUT, weiter
   - 🎯 Zu planen / grob geplant? → WARNUNG
   - ✅ Geschrieben? → HINWEIS
   - 🔄 In Arbeit? → Fortsetzen?

3. **Bei nicht-detaillierter Outline:**
```
⚠️ KAPITEL NICHT DETAILLIERT GEPLANT

Kapitel X hat Status: [aktueller Status]
Die Outline ist [grob/nicht vorhanden].

Optionen:
1. Zuerst detailliert planen (empfohlen)
   → Sage: "Plane Kapitel X"
2. Mit grober Outline schreiben (riskanter, weniger konsistent)
3. Gemeinsam jetzt schnell planen, dann schreiben

Wie möchtest du vorgehen?
```

**STOPPE hier und warte auf Antwort, falls Outline nicht detailliert!**

### SCHRITT 3: Charaktere und Settings laden (automatisch)

**Basierend auf der Outline:**

```
@Characters/[POV-Charakter].md
@Characters/[Alle in Outline erwähnten Charaktere].md
@Worldbuilding/[Alle in Outline erwähnten Orte].md
@Worldbuilding/[Relevante Systeme wie Magiesystem, Technologie].md
```

**Für Kontinuität:**
```
@Chapters/Kapitel-[X-1].md  # Vorheriges Kapitel
```

**Falls POV-Wechsel oder komplexe Beziehung:**
```
@Characters/_Relationships.md
```

### SCHRITT 4: Pre-Writing-Check

**Prüfe die Checkliste aus der Outline:**

Aus Story-Outline.md unter "Checkliste vor dem Schreiben":
- [ ] Timeline-Konsistenz? (Zeitpunkt klar)
- [ ] Charaktere haben korrektes Wissen/Status?
- [ ] Setting-Details verfügbar?
- [ ] Kontinuität zum vorherigen Kapitel klar?
- [ ] Handlungsstränge im Blick?
- [ ] System-Regeln (Magie/Tech) klar?

**Bei Problemen in der Checkliste:**
```
⚠️ PRE-WRITING-PROBLEME:

Folgende Punkte sind unklar:
- [Problem 1]
- [Problem 2]

Soll ich:
1. Trotzdem weiterschreiben (du klärst später)
2. Diese Punkte jetzt mit dir klären
3. Fehlende Infos recherchieren/erstellen
```

### SCHRITT 5: Kapitel schreiben

**Arbeite Szene für Szene durch die Outline:**

#### Für jede Szene:

1. **Lies die geplanten Beats** aus der Outline
2. **Schreibe die Szene in vollem Prosa-Stil**

**Berücksichtige dabei:**

**A) POV und Perspektive:**
- Aus CHARACTER.md: Wie denkt/spricht dieser Charakter?
- Perspektive: Ich-Erzähler / Er-Sie-Erzähler (aus PROJECT-CONTEXT oder Style-Rules)
- Voice: Charakteristischer Ton dieser Person

**B) Erzählzeit:**
- Präsens oder Vergangenheit (aus PROJECT-CONTEXT oder Style-Rules)
- Konsistent durch ganzes Kapitel

**C) Show don't Tell:**
- Emotionen durch Handlung und Körpersprache zeigen
- Gedanken des POV-Charakters direkt
- Dialoge natürlich und charakteristisch
- Weniger Adjektive, mehr konkrete Details

**D) Sinnliche Details:**
- 5 Sinne nutzen (nicht nur Sehen)
- Atmosphäre durch Details aufbauen
- Setting lebendig machen

**E) Pacing:**
- Action-Szenen: Kurze Sätze, schneller Rhythmus
- Ruhige Momente: Längere Sätze, mehr Reflexion
- Dialog-Tempo variieren

**F) Dialog:**
- Charakteristisch für jeden Sprecher
- Subtext (was NICHT gesagt wird)
- Action während Dialog (nicht nur "talking heads")
- Nutze geplante Dialog-Highlights aus Outline

**G) Übergänge zwischen Szenen:**
- Fließend oder mit klarem Bruch (je nach Bedarf)
- Zeitsprünge klar machen
- Ortswechsel etablieren

#### Kapitel-Ende:

- Setze den geplanten Hook/Ending um (aus Outline)
- Letzter Satz sollte Impact haben
- Emotionaler Zustand klar für nächstes Kapitel
- Varianten:
  - Cliffhanger (Was passiert als nächstes?)
  - Reflexion (Charakter verarbeitet)
  - Entscheidung (Charakter wählt Weg)
  - Revelation (Neue Information)

#### Wortanzahl-Ziel:

- Orientiere dich an geplanten Längen aus Outline
- Aber: Qualität > exakte Länge
- Szenen brauchen so viel Raum wie sie brauchen

### SCHRITT 6: Kapitel-Datei erstellen

**Erstelle `/Chapters/Kapitel-[XX].md`:**

```markdown
---
type: chapter
number: [X]
title: "[Titel aus Outline]"
pov: "[POV-Charakter]"
status: "Entwurf"
word_count: [Tatsächliche Wortanzahl zählen]
timeline_date: "[Aus Timeline oder Outline]"
---

[Der vollständige geschriebene Text des Kapitels]
```

**Wichtig:**
- Wortanzahl TATSÄCHLICH zählen
- Keine plot_points oder anderen Felder im YAML!
- Status = "Entwurf" (nicht "Fertig", das kommt nach Revision)

---

## SCHRITT 7: AUTOMATISCHE SYNCHRONISIERUNG

**KRITISCH: Du führst JETZT ALLE Updates durch - automatisch!**

### 7.1 Story-Outline.md aktualisieren

**Lade:**
```
@Plot/Story-Outline.md
```

**Update:**
1. Finde Kapitel X
2. Ändere Status: 📝 oder 🔄 → ✅ Geschrieben ([Wortanzahl] Wörter)
3. **Falls während des Schreibens Änderungen gemacht wurden:**
   - Dokumentiere in **Notizen**-Feld:
   - "Geschrieben am [Datum]. Änderungen gegenüber Outline: [...]"
   - Beispiel: "Szene 2 wurde länger, Maria hat größere Rolle als geplant"
4. Update `last_updated` im YAML

### 7.2 Chapters/_INDEX.md aktualisieren

**Lade:**
```
@Chapters/_INDEX.md
```

**Update:**
1. Finde oder erstelle Zeile für Kapitel X in der Tabelle
2. Fülle aus:
   - Nummer: [X]
   - Titel: [Aus Kapitel]
   - POV: [Charaktername]
   - Wörter: [Wortanzahl]
   - Status: ✅ Entwurf (mit Emoji)
   - Zusammenfassung: [1 Satz was passiert]

3. **Gesamt-Statistik NEU BERECHNEN:**
   - Zähle alle geschriebenen Kapitel
   - Summiere alle Wortanzahlen
   - Berechne Fortschritt: (Geschriebene Wörter / Ziel-Wörter) × 100
   - Update die Statistik-Sektion

**Beispiel:**
```markdown
## Gesamt-Statistik
- **Ziel:** 28 Kapitel, 80.000 Wörter
- **Geschrieben:** 5 Kapitel, 12.500 Wörter
- **Fortschritt:** 15,6%
```

### 7.3 Plot/Timeline.md aktualisieren

**Lade:**
```
@Plot/Timeline.md
```

**Update:**
1. Identifiziere wichtige Ereignisse aus dem geschriebenen Kapitel
2. Finde den richtigen chronologischen Platz (nutze `timeline_date`)
3. Trage Ereignisse ein:

```markdown
## [Timeline-Datum] - [Kurzbeschreibung der Phase]

**[Ereignis 1]** (Kapitel X)
- [Detail was passiert ist]
- [Relevante Info für Kontinuität]

**[Ereignis 2]** (Kapitel X)
- [Detail]
```

**Was gehört in Timeline:**
- Plot-relevante Ereignisse
- Erste/letzte Erwähnung wichtiger Elemente
- Wendepunkte in Beziehungen
- Geografische Bewegungen (wenn wichtig)
- NICHT: Jedes Detail, nur wichtiges!

### 7.4 WRITING-LOG.md aktualisieren

**Lade:**
```
@WRITING-LOG.md
```

**Erstelle neuen Eintrag:**

```markdown
## [Aktuelles Datum - YYYY-MM-DD]

### Kapitel X: "[Titel]" - Geschrieben ✅

**Wortanzahl:** [X] Wörter
**POV:** [Charaktername]
**Timeline:** [Datum/Tag in der Story]

**Kern des Kapitels:**
[2-3 Sätze Zusammenfassung was passiert]

**Wichtige Entscheidungen während des Schreibens:**
- [Entscheidung 1, z.B. "Jakob hat früher eingegriffen als geplant - fühlte sich richtiger an"]
- [Entscheidung 2, z.B. "Dialog-Szene mit Maria erweitert für Charaktermoment"]
- [Oder: "Keine nennenswerten Änderungen von der Outline"]

**Abweichungen von Outline:**
- [Falls vorhanden: Was wurde geändert und warum]
- [Oder: "Outline wurde wie geplant umgesetzt"]

**Neue Elemente eingeführt:**
- [z.B. "Nebencharakter: Händler Gregor (grauer Bart, misstrauisch)"]
- [z.B. "Magiesystem-Detail: Amulett leuchtet rot bei Gefahr"]
- [z.B. "Ort-Detail: Shadowvale hat einen unterirdischen Markt"]
- [Oder: "Keine neuen Elemente"]

**Herausforderungen beim Schreiben:**
- [Optional: Was war schwierig?]
- [z.B. "Dialog zwischen Elena und Jakob fühlte sich anfangs steif an, mehrfach überarbeitet"]

**Offene Fragen für nächste Kapitel:**
- [ ] [Frage 1, z.B. "Wie reagiert Maria wenn sie von Jakobs Geheimnis erfährt?"]
- [ ] [Frage 2, z.B. "Muss das Magiesystem noch genauer definiert werden?"]
- [Oder leer lassen wenn keine]

**Nächster Schritt:**
[z.B. "Kapitel X+1 planen" oder "Kapitel X überarbeiten" oder "Kapitel X-1 und X zusammen prüfen"]

---
```

### 7.5 Charakterdateien aktualisieren (falls nötig)

**Lade die relevanten Charaktere:**
```
@Characters/[Alle im Kapitel auftretenden wichtigen Charaktere].md
```

**Update NUR wenn:**
- ✅ Neue Charakterzüge wurden gezeigt (die nicht in Datei stehen)
- ✅ Beziehungen haben sich signifikant entwickelt
- ✅ Status hat sich geändert (verletzt, neues Wissen, neue Fähigkeit, etc.)
- ✅ Wichtiges Ereignis für diesen Charakter passiert

**NICHT updaten für:**
- ❌ Details die schon in Charakterdatei stehen
- ❌ Kleine Momente ohne langfristige Bedeutung
- ❌ Dinge die in anderen Dateien besser dokumentiert sind

**Update-Format in Charakterdatei:**

Unter Abschnitt "## Entwicklung" ergänzen:

```markdown
### Nach Kapitel X ([Datum]):
- [Neue Erkenntnis/Trait/Fähigkeit]
- [Status-Änderung, z.B. "Verletzt am linken Arm"]
- [Beziehung zu Y]: [Was hat sich geändert]
- [Wissen]: [Was hat Charakter erfahren]
```

**Beispiel:**
```markdown
### Nach Kapitel 5 (Tag 12):
- Erste erfolgreiche Magie-Anwendung (kontrolliertes Licht)
- Weiß jetzt von Jakobs Vergangenheit als Magier
- Beziehung zu Jakob: Verstehen hat sich vertieft, aber auch Angst vor seiner Macht
- Emotional: Von Selbstzweifel zu vorsichtigem Selbstvertrauen
```

---

## SCHRITT 8: Zusammenfassung an Autor

**Gib dem Autor einen vollständigen Bericht:**

```
🎉 KAPITEL X FERTIGGESTELLT & SYNCHRONISIERT

**Kapitel:** [X] - "[Titel]"
**Wortanzahl:** [X] Wörter
**POV:** [Charaktername]
**Timeline:** [Datum/Tag in der Story]
**Status:** ✅ Entwurf fertig

---

**Was passiert in diesem Kapitel:**
[3-4 Sätze Zusammenfassung des Kapitels]

---

## 📊 AUTOMATISCHE UPDATES DURCHGEFÜHRT:

✅ **Plot/Story-Outline.md**
   - Status geändert: [alter Status] → ✅ Geschrieben ([X] Wörter)
   - [Falls Änderungen:] Notizen ergänzt mit Abweichungen
   
✅ **Chapters/_INDEX.md**
   - Kapitelzeile hinzugefügt/aktualisiert
   - Gesamt-Statistik neu berechnet:
     * Fortschritt: [Jetzt X%] (vorher [Y%])
     * Kapitel geschrieben: [A]/[B]
     * Wortanzahl: [C]/[D]
   
✅ **Plot/Timeline.md**
   - [Anzahl] neue Ereignisse eingetragen
   - Chronologisch bei [Datum/Tag] eingeordnet:
     * [Ereignis 1]
     * [Ereignis 2]
   
✅ **WRITING-LOG.md**
   - Neuer Eintrag erstellt ([Datum])
   - Entscheidungen dokumentiert: [Anzahl]
   - Abweichungen notiert: [Anzahl oder "Keine"]
   - Offene Fragen: [Anzahl oder "Keine"]

[Falls Charakter-Updates:]
✅ **Charakterdateien aktualisiert:**
   - **[Charakter A]**: [Was updated wurde]
   - **[Charakter B]**: [Was updated wurde]

---

## 📝 WICHTIGE ERKENNTNISSE AUS DEM SCHREIBPROZESS:

**Abweichungen von Outline:**
[Liste der Änderungen oder "Keine nennenswerten Abweichungen"]

**Neue Elemente eingeführt:**
[Liste oder "Keine"]

**Herausforderungen:**
[Falls relevant, sonst weglassen]

**Offene Fragen für nächste Kapitel:**
[Liste oder "Keine"]

---

## 🎯 NÄCHSTE SCHRITTE:

**Empfehlungen:**
- Kapitel [X+1] planen? (Sage: "Plane Kapitel [X+1]")
- Dieses Kapitel überarbeiten? (Sage: "Überarbeite Kapitel X")
- Konsistenz-Check durchführen? (Sage: "Konsistenzprüfung")
- Mehrere Kapitel vorausplanen? (Sage: "Plane Kapitel [X+1] bis [X+3]")

**Story-Status:**
- Akt [X] ist zu [%] geschrieben
- [Noch X Kapitel bis Midpoint/Plot Point/Ende]
- Handlungsstrang A-Plot: [Status]

---

✨ **Alle Dateien sind synchron!** Du bist startklar für das nächste Kapitel.
```

---

## Spezialfälle & Probleme

### Fall 1: Kapitel ist länger als geplant

Kein Problem! Qualität geht vor.

**Im Writing-Log dokumentieren:**
```markdown
**Abweichungen:**
- Kapitel wurde länger als geplant ([X] statt [Y] Wörter)
- Grund: [z.B. "Dialog-Szene brauchte mehr Raum für Emotionen"]
```

### Fall 2: Beim Schreiben ergab sich neue Richtung

Das ist normal und gut (organisches Schreiben)!

**Dokumentiere es:**
1. In Story-Outline.md unter Notizen
2. In WRITING-LOG.md unter Abweichungen
3. Falls es spätere Kapitel betrifft: In `/Plot/Offene-Fragen.md`

**Beispiel:**
```markdown
**Wichtige Entscheidung:**
- Jakob hat sein Geheimnis früher enthüllt als geplant (war für Kap 8 geplant)
- Grund: Die Szene führte natürlich dorthin, fühlte sich richtiger an
- Folgen: Kapitel 6-8 müssen neu geplant werden
```

### Fall 3: Neue Charaktere tauchten auf

**Während des Schreibens:**
- Weiter schreiben, Namen merken

**Nach dem Schreiben (in Sync-Phase):**
1. Dokumentiere in WRITING-LOG.md unter "Neue Elemente"
2. Biete an Charakterdatei zu erstellen:

```
💡 NEUE CHARAKTERE EINGEFÜHRT:

In Kapitel X sind neue Charaktere aufgetaucht:
- Händler Gregor (grauer Bart, misstrauisch, verkauft Kräuter)
- Stadtwache Mira (kurze Erwähnung)

Soll ich für diese Charaktere Dateien erstellen?
Oder sind sie nur Statisten und brauchen keine Dokumentation?
```

### Fall 4: Worldbuilding-Widerspruch bemerkt

**Während des Schreibens:**
- Notiere es mental, schreibe weiter

**Nach dem Schreiben:**

```
⚠️ WORLDBUILDING-KONFLIKT ENTDECKT:

Beim Schreiben von Kapitel X habe ich bemerkt:
Im Kapitel: [Was ich geschrieben habe]
Laut Worldbuilding/[Datei].md: [Was dort steht]

Optionen:
1. Kapitel anpassen an Worldbuilding
2. Worldbuilding aktualisieren (falls bewusste Änderung)
3. Beides nochmal mit dir durchgehen

Wie möchtest du vorgehen?
```

### Fall 5: Technische Probleme (Datei-Zugriff, etc.)

Falls du eine Datei nicht laden kannst:

```
⚠️ TECHNISCHES PROBLEM:

Ich konnte nicht auf [Datei] zugreifen.

Ich habe trotzdem geschrieben basierend auf:
- [Was ich hatte]

Bitte prüfe nach dem Schreiben:
- [Was gecheckt werden muss]
```

---

## Best Practices beim Schreiben

### ✅ Mache:

- **Bleibe beim POV:** Nur Gedanken/Wahrnehmungen des POV-Charakters
- **Zeige Emotionen:** Durch Handlung, nicht durch "Er war wütend"
- **Variiere Satzlänge:** Für natürlichen Rhythmus
- **Nutze konkrete Details:** "Rostiger Dolch" statt "alte Waffe"
- **Charakteristischer Dialog:** Jeder spricht anders
- **Atmosphäre aufbauen:** Durch sinnliche Details
- **Natürliche Übergänge:** Zwischen Szenen und Gedanken
- **Subtext nutzen:** Was nicht gesagt wird ist oft wichtiger

### ❌ Vermeide:

- **Info-Dumps:** Erkläre nicht alles auf einmal
- **Purple Prose:** Überladene, gekünstelte Sprache
- **Telling statt Showing:** "Sie war traurig" → ZEIGE es
- **Passive Voice übermäßig:** Aktiv ist meist stärker
- **Adverb-Exzess:** "sagte er laut" → zeige es anders
- **Unrealistische Dialoge:** Menschen reden nicht in Aufsätzen
- **POV-Wechsel im Kapitel:** (außer bewusst geplant)
- **Inkonsistenzen:** Achte auf Details die du etabliert hast

### Pacing-Techniken:

**Für Action/Spannung:**
- Kurze Sätze
- Kurze Absätze
- Weniger Beschreibungen
- Schneller Dialog
- Fokus auf Aktion

**Für Ruhe/Reflexion:**
- Längere Sätze
- Ausführliche Beschreibungen
- Innere Monologe
- Atmosphäre
- Charakterentwicklung

---

**Dieser Skill ist aktiv. Du führst ALLE Schritte autonom aus, besonders die Synchronisierung!**
