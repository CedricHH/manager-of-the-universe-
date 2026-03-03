# Revision Skill - Kapitel überarbeiten

## Zweck
Dieser Skill definiert wie du geschriebene Kapitel überarbeitest. Er wird aktiviert wenn der Autor sagt:
- "Überarbeite Kapitel X"
- "Verbessere Kapitel X"
- "Revision von Kapitel X"
- "Rewrite Kapitel X"

## Workflow: Kapitel überarbeiten

### SCHRITT 1: Kontext laden (automatisch)

**Das Kapitel selbst:**
```
@Chapters/Kapitel-[X].md
```

**Ursprüngliche Planung:**
```
@Plot/Story-Outline.md
```

**Kontext-Informationen:**
```
@Plot/Timeline.md
@WRITING-LOG.md
@Meta/Style-Rules.md  # Falls vorhanden
```

### SCHRITT 2: Charaktere und Settings laden

**Basierend auf dem Kapitel:**
```
@Characters/[POV-Charakter].md
@Characters/[Im Kapitel auftretende Charaktere].md
@Worldbuilding/[Im Kapitel vorkommende Orte].md
@Worldbuilding/[Relevante Systeme].md
```

**Für Kontinuität:**
```
@Chapters/Kapitel-[X-1].md  # Vorheriges
@Chapters/Kapitel-[X+1].md  # Nächstes (falls existiert)
```

### SCHRITT 3: Analyse & Diagnose

**Führe automatische Checks durch:**

#### A) Entspricht es der Outline?
- Vergleiche Kapitel mit Outline in Story-Outline.md
- Wurden geplante Beats umgesetzt?
- Wurden geplante Charaktermomente eingebaut?
- Wichtige Plot-Punkte vorhanden?

**Status:** ✅ Entspricht | ⚠️ Weicht ab | ❌ Stark abgewichen

#### B) Timeline-Konsistenz?
- Stimmt `timeline_date` mit Timeline.md?
- Passen zeitliche Referenzen ("gestern", "vor 3 Tagen")?
- Ist genug/zu viel Zeit für Ereignisse vergangen?

**Status:** ✅ Konsistent | ⚠️ Kleine Probleme | ❌ Widersprüche

#### C) Charakter-Konsistenz?
- Verhalten passend zur Persönlichkeit?
- Wissensstand korrekt für diesen Zeitpunkt?
- Emotionaler Zustand nachvollziehbar?
- Charakterentwicklung graduell?

**Status:** ✅ Konsistent | ⚠️ Kleine OOC-Momente | ❌ Große Probleme

#### D) Pacing?
- Angemessene Länge für die Szenen?
- Wechsel zwischen Action/Dialog/Beschreibung?
- Szenen zu lang/kurz für ihre Funktion?
- Rhythmus funktioniert?

**Status:** ✅ Gut | ⚠️ Stellen langsam/schnell | ❌ Großes Problem

#### E) Show vs Tell Balance?
- Werden Emotionen gezeigt oder nur benannt?
- Info-Dumps vermieden?
- Sinnliche Details vorhanden?
- "As you know, Bob"-Dialoge?

**Status:** ✅ Gute Balance | ⚠️ Einige Telling-Momente | ❌ Zu viel Tell

#### F) Dialog-Qualität?
- Charakteristisch für Sprecher?
- Natürlich klingend?
- Subtext vorhanden?
- Action während Dialog?
- Zu viele/wenige Dialog-Tags?

**Status:** ✅ Stark | ⚠️ Stellenweise steif | ❌ Überarbeitung nötig

#### G) Prosa-Qualität?
- Satzlängen variiert?
- Überflüssige Wörter ("sehr", "wirklich", "etwas")?
- Passive Voice übermäßig?
- Adverbien zu häufig?
- Wiederholungen?

**Status:** ✅ Gut | ⚠️ Kleine Schwächen | ❌ Größere Probleme

#### H) Kontinuität?
- Passt zu vorigem Kapitel?
- Führt logisch zu nächstem Kapitel (falls existiert)?
- Keine widersprechenden Details?

**Status:** ✅ Konsistent | ⚠️ Kleine Lücken | ❌ Widersprüche

### SCHRITT 4: Bericht an Autor

```
📋 REVISIONS-ANALYSE: KAPITEL X

**Kapitel:** [X] - "[Titel]"
**Aktueller Status:** [Entwurf/Revision/etc.]
**Wortanzahl:** [X] Wörter
**Geschrieben am:** [Datum aus Writing-Log]

---

## Automatische Checks:

**Outline-Übereinstimmung:** [✅/⚠️/❌] [Kommentar]
**Timeline-Konsistenz:** [✅/⚠️/❌] [Kommentar]
**Charakter-Konsistenz:** [✅/⚠️/❌] [Kommentar]
**Pacing:** [✅/⚠️/❌] [Kommentar]
**Show vs Tell:** [✅/⚠️/❌] [Kommentar]
**Dialog-Qualität:** [✅/⚠️/❌] [Kommentar]
**Prosa-Qualität:** [✅/⚠️/❌] [Kommentar]
**Kontinuität:** [✅/⚠️/❌] [Kommentar]

---

## Gefundene Probleme:

[Falls vorhanden:]

### Hohe Priorität (❌):
- [Problem 1 mit genauer Beschreibung]
- [Problem 2 mit genauer Beschreibung]

### Mittlere Priorität (⚠️):
- [Problem 1]
- [Problem 2]

### Stärken des Kapitels (✅):
- [Was gut funktioniert]
- [Was gut funktioniert]

---

## Empfohlene Revision:

**Was möchtest du überarbeiten lassen?**

**Option 1: Vollständige Revision**
- Ich überarbeite das gesamte Kapitel
- Fokus auf alle gefundenen Probleme
- Dauer: [Schätzung basierend auf Problemen]

**Option 2: Fokussierte Revision**
Wähle Bereiche:
- [ ] Pacing verbessern
- [ ] Dialog überarbeiten
- [ ] Show vs Tell verbessern
- [ ] Prosa polieren
- [ ] Konsistenz-Probleme beheben
- [ ] Spezifische Szenen neu schreiben

**Option 3: Spezifische Szenen**
- Welche Szene(n) soll ich überarbeiten?
- Was genau soll geändert werden?

**Option 4: Nur Fehler beheben**
- Konsistenz-Probleme (Timeline, Charaktere)
- Keine Stil-Änderungen

**Option 5: Ich will selbst überarbeiten**
- Du nutzt meinen Bericht als Guide
- Ruf mich wenn du Hilfe brauchst

---

Wie möchtest du vorgehen?
```

### SCHRITT 5: Überarbeitung durchführen

**Basierend auf Autor-Input:**

#### A) Vollständige Revision:

1. **Szene für Szene durchgehen**
2. **Für jede Szene prüfen:**
   - Funktion klar?
   - Beats umgesetzt?
   - Pacing richtig?
   - Emotionen gezeigt?
   - Dialog stark?

3. **Überarbeiten:**
   - Schwache Stellen neu schreiben
   - Überflüssiges streichen
   - Fehlende Details ergänzen
   - Dialog verbessern
   - Prosa polieren

4. **Zwischen Szenen:**
   - Übergänge prüfen
   - Kontinuität sichern

#### B) Fokussierte Revision:

**Beispiel: Dialog überarbeiten**

1. Identifiziere alle Dialog-Szenen
2. Für jede:
   - Charakteristisch? → Anpassen
   - Natürlich? → Umformulieren
   - Subtext? → Ergänzen
   - Action dabei? → Hinzufügen
   - Tags variiert? → Verbessern

**Beispiel: Pacing verbessern**

1. Identifiziere zu langsame Stellen:
   - Info-Dumps → Kürzen/Verteilen
   - Überlange Beschreibungen → Straffen
   - Langweilige Passagen → Spannung einbauen

2. Identifiziere zu schnelle Stellen:
   - Wichtige Momente zu kurz → Erweitern
   - Emotionale Beats fehlen → Ergänzen
   - Charakterreaktionen → Hinzufügen

**Beispiel: Show vs Tell**

1. Finde "Tell"-Momente:
   - "Er war wütend" → Zeige wie: geballte Fäuste, etc.
   - "Sie fühlte sich einsam" → Zeige: leeres Zimmer, Stille, etc.

2. Ersetze durch "Show":
   - Körpersprache
   - Handlungen
   - Innere Gedanken (POV)
   - Umgebungsreaktionen

#### C) Spezifische Szenen:

1. Identifiziere die Szene
2. Verstehe was nicht funktioniert
3. Schreibe Szene neu
4. Prüfe Übergänge zur vorherigen/nächsten Szene

#### D) Nur Fehler beheben:

1. Timeline-Widersprüche korrigieren
2. Charakter-Inkonsistenzen beheben
3. Worldbuilding-Fehler anpassen
4. Keine Stil-Änderungen

### SCHRITT 6: Kapitel-Datei aktualisieren

**Überschreibe `/Chapters/Kapitel-[X].md`:**

```markdown
---
type: chapter
number: [X]
title: "[Titel - eventuell geändert]"
pov: "[POV-Charakter]"
status: "Revision"  # Oder "Fertig" wenn final
word_count: [Neue Wortanzahl]
timeline_date: "[timeline_date]"
---

[Der überarbeitete Text]
```

### SCHRITT 7: Updates nach Revision

#### 7.1 Story-Outline.md

```
@Plot/Story-Outline.md
```

- Status update: ✅ Geschrieben → ✏️ Revision → ✅ Überarbeitet
- Falls Wortanzahl signifikant geändert: Update
- In **Notizen** ergänzen:
  - "Überarbeitet am [Datum]"
  - "Änderungen: [Kurz was gemacht wurde]"

#### 7.2 Chapters/_INDEX.md

```
@Chapters/_INDEX.md
```

- Status update: ✅ Entwurf → ✏️ Revision (oder ✅ Fertig)
- Wortanzahl update (falls geändert)
- Gesamt-Statistik neu berechnen (falls Wortanzahl geändert)

#### 7.3 WRITING-LOG.md

```
@WRITING-LOG.md
```

Neuer Eintrag:

```markdown
## [Datum]

### Kapitel X: "[Titel]" - Überarbeitet ✏️

**Revisions-Fokus:** [Vollständig/Dialog/Pacing/etc.]
**Wortanzahl:** [Alt] → [Neu] ([+/-X] Wörter)

**Durchgeführte Änderungen:**
- [Änderung 1, z.B. "Dialog zwischen Elena und Jakob natürlicher gemacht"]
- [Änderung 2, z.B. "Szene 2 gestrafft - 200 Wörter gekürzt"]
- [Änderung 3, z.B. "Show statt Tell in emotionalen Momenten"]

**Behobene Probleme:**
- [Problem 1, z.B. "Timeline-Widerspruch mit Kap 4 korrigiert"]
- [Problem 2]

**Was noch zu tun ist (falls nicht fertig):**
- [ ] [Offener Punkt 1]
- [ ] [Offener Punkt 2]

**Status:** [Revision abgeschlossen/Weitere Überarbeitung geplant]
```

#### 7.4 Falls Charaktere/Timeline/Worldbuilding betroffen:

**Nur wenn durch Revision Fakten geändert wurden:**
- Charakterdateien anpassen
- Timeline korrigieren
- Worldbuilding aktualisieren

### SCHRITT 8: Abschlussbericht

```
✅ KAPITEL X ÜBERARBEITET

**Kapitel:** [X] - "[Titel]"
**Revisions-Typ:** [Vollständig/Fokussiert/etc.]
**Neue Wortanzahl:** [X] Wörter (vorher: [Y], [+/-Z])

---

## Durchgeführte Änderungen:

**Hauptfokus:**
- [Was wurde hauptsächlich überarbeitet]

**Detaillierte Änderungen:**
- [Liste von 3-5 wichtigsten Änderungen]

**Behobene Probleme:**
- [Liste der korrigierten Probleme]

---

## Verbesserungen:

**Vorher → Nachher:**
- **Pacing:** [Status vorher] → [Status nachher]
- **Dialog:** [Status vorher] → [Status nachher]
- **Show vs Tell:** [Status vorher] → [Status nachher]
- **Konsistenz:** [Status vorher] → [Status nachher]

---

## 📊 Updates durchgeführt:

✅ Kapitel-Datei überschrieben
✅ Story-Outline.md: Status auf ✏️ Revision gesetzt
✅ Chapters/_INDEX.md: [Wortanzahl/Status] aktualisiert
✅ WRITING-LOG.md: Revision dokumentiert
[Falls relevant:] ✅ [Andere Dateien]: [Was geändert]

---

## 🎯 Nächste Schritte:

**Empfehlungen:**
- Weitere Revision nötig? (Sage: "Überarbeite Kapitel X nochmal")
- Nächstes Kapitel schreiben? (Sage: "Schreibe Kapitel [X+1]")
- Mehrere Kapitel im Zusammenhang prüfen? (Sage: "Konsistenzprüfung Kapitel [X-1] bis [X+1]")

**Kapitel-Status:** [z.B. "Entwurf gut, aber noch nicht final" oder "Revision abgeschlossen, bereit für finalen Check"]
```

---

## Revisions-Strategien

### Strategie 1: Der "Strippen"-Pass
**Fokus:** Kürzen, straffen, entrümpeln

1. Identifiziere überflüssige Wörter/Sätze
2. Streiche redundante Informationen
3. Kürze langatmige Beschreibungen
4. Entferne unnötige Dialoge

**Gut für:** Kapitel die zu lang/langsam sind

### Strategie 2: Der "Deepen"-Pass
**Fokus:** Vertiefen, ausbauen, ergänzen

1. Identifiziere oberflächliche Momente
2. Füge emotionale Tiefe hinzu
3. Erweitere wichtige Szenen
4. Ergänze sinnliche Details

**Gut für:** Kapitel die zu schnell/oberflächlich sind

### Strategie 3: Der "Dialog"-Pass
**Fokus:** Nur Dialoge überarbeiten

1. Jeden Dialog-Block isoliert betrachten
2. Charakteristische Sprechweise verstärken
3. Subtext ergänzen
4. Action während Dialog hinzufügen
5. Tags variieren

**Gut für:** Dialog-lastige Kapitel die sich steif anfühlen

### Strategie 4: Der "Emotion"-Pass
**Fokus:** Show statt Tell für Emotionen

1. Suche "Telling"-Momente (war traurig, fühlte sich...)
2. Ersetze durch:
   - Körpersprache
   - Handlungen
   - Innere Gedanken
   - Sinnliche Wahrnehmungen
3. Zeige emotionale Übergänge

**Gut für:** Kapitel mit flachen Emotionen

### Strategie 5: Der "Pacing"-Pass
**Fokus:** Rhythmus und Tempo

1. Identifiziere Tempo-Probleme:
   - Zu langsam: Kürzen, straffen
   - Zu schnell: Moments erweitern
2. Variiere Satzlängen
3. Action/Ruhe-Balance prüfen
4. Szenen-Längen anpassen

**Gut für:** Ungleichmäßiges Tempo

### Strategie 6: Der "Konsistenz"-Pass
**Fokus:** Fakten und Kontinuität

1. Timeline-Check
2. Charakter-Wissen-Check
3. Worldbuilding-Regeln-Check
4. Detail-Konsistenz (Augenfarbe, etc.)

**Gut für:** Nach langer Schreibpause oder bei vielen Kapiteln

---

## Häufige Revisions-Probleme

### Problem: Zu viel Info-Dump

**Symptom:** Lange Absätze die Hintergrund erklären

**Lösung:**
1. Verteile Info über mehrere Szenen
2. Zeige durch Handlung statt Erklärung
3. Nutze Dialog (aber natürlich)
4. Cut radikal - braucht Leser das jetzt wirklich?

### Problem: Passive Voice übermäßig

**Symptom:** Viele "wurde", "war worden", etc.

**Lösung:**
1. Identifiziere Passiv-Konstruktionen
2. Umformuliere zu Aktiv
3. Beispiel: "Der Dolch wurde gezogen" → "Er zog den Dolch"

### Problem: Adverb-Exzess

**Symptom:** "sagte er laut", "ging schnell", "sehr groß"

**Lösung:**
1. Finde Adverbien (auf -ly/-lich)
2. Streiche oder ersetze durch stärkeres Verb
3. "ging schnell" → "hastete"
4. "sagte laut" → "rief" oder zeige Lautstärke anders

### Problem: Wiederholungen

**Symptom:** Gleiche Wörter/Phrasen zu oft

**Lösung:**
1. Suche häufige Wörter
2. Variiere (aber nicht gekünstelt)
3. Manchmal ist Wiederholung OK (Stil-Mittel)

### Problem: Steifer Dialog

**Symptom:** Charaktere reden wie Lehrbücher

**Lösung:**
1. Lies Dialog laut vor
2. Klingt es wie echter Mensch?
3. Füge Filler ein ("ähm", "also", "weißt du")
4. Unterbreche Sätze
5. Charakteristische Sprechweisen

### Problem: "As you know, Bob"

**Symptom:** Charaktere erklären sich gegenseitig Dinge die sie beide wissen

**Lösung:**
1. Finde unnatürliche Exposition
2. Streiche oder finde anderen Weg
3. Lasse Leser manche Dinge selbst verstehen

---

## Wann ist Revision fertig?

**Ein Kapitel ist fertig wenn:**

✅ Alle Check-Punkte mit ✅ (oder höchstens kleine ⚠️)
✅ Outline-Beats umgesetzt
✅ Keine Konsistenz-Probleme
✅ Prosa flüssig und stark
✅ Dialog natürlich
✅ Emotionen gezeigt, nicht benannt
✅ Pacing funktioniert
✅ Du (der Autor) bist zufrieden

**Perfektion ist unmöglich!** Irgendwann muss man loslassen.

**Faustregel:** Nach 2-3 Revisions-Pässen ist ein Kapitel gut genug für Entwurf.

---

**Dieser Skill ist aktiv. Du führst Revision-Analysen autonom durch und bietest verschiedene Überarbeitungs-Optionen an.**
