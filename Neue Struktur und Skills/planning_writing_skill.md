# Planning Skill - Kapitel planen

## Zweck
Dieser Skill definiert wie du Kapitel planst. Er wird aktiviert wenn der Autor sagt:
- "Plane Kapitel X"
- "Erstelle Outline für Kapitel X"
- "Plane Kapitel X bis Y" (Batch-Planung)

## Workflow: EINZELNES Kapitel planen

### SCHRITT 1: Kontext laden (automatisch, ohne zu fragen)

**Basis-Kontext:**
```
@Meta/CORE-RULES.md
@PROJECT-CONTEXT.md
@Plot/Story-Outline.md
@Plot/Timeline.md
@Plot/Handlungsstränge.md
@Characters/_Relationships.md
```

### SCHRITT 2: Kapitel analysieren

1. **Finde das Kapitel in Story-Outline.md**
   - Suche nach "### Kapitel X:"
   - Prüfe aktuellen Status (📝/🎯/✅/etc.)

2. **Identifiziere:**
   - POV-Charakter (aus Outline oder zu bestimmen)
   - Akt-Zugehörigkeit (1, 2, oder 3)
   - Hauptort/Setting
   - Beteiligte Charaktere
   - Relevante Handlungsstränge (A/B/C-Plot)
   - Funktion im größeren Story-Bogen

3. **Prüfe Kontext:**
   - Was passierte im vorherigen Kapitel?
   - Wo steht die Story zu diesem Zeitpunkt?
   - Welche Fragen/Konflikte sind offen?

### SCHRITT 3: Zusätzliche Dateien laden (automatisch)

**Basierend auf deiner Analyse:**

```
@Characters/[POV-Charakter].md
@Characters/[Alle beteiligten Charaktere].md
@Worldbuilding/[Haupt-Setting].md
@Worldbuilding/[Relevante Systeme wie Magiesystem].md
```

**Falls vorheriges Kapitel existiert:**
```
@Chapters/Kapitel-[X-1].md
```

**Falls späteres Kapitel existiert (bei Rückwärts-Planung):**
```
@Chapters/Kapitel-[X+1].md
```

### SCHRITT 4: Konsistenz-Check

**Prüfe mit Consistency-Rules.md Prinzipien:**

- **Timeline:** Wann spielt dieses Kapitel? Passt es chronologisch?
- **Charaktere:** Wo sind die Charaktere? Was wissen sie? Wie geht es ihnen?
- **Handlungsstränge:** Welche Threads müssen vorangebracht werden?
- **Kontinuität:** Wie endet Kap X-1? Wo beginnen wir in Kap X?
- **Akt-Struktur:** Welche Funktion hat dieses Kapitel im Akt?
- **Worldbuilding:** Welche Setting-Details sind wichtig?

**Bei Problemen:** Warnung ausgeben und klären bevor du planst!

### SCHRITT 5: Detaillierte Outline erstellen

**Erweitere die grobe Outline in Story-Outline.md:**

#### Format für detaillierte Kapitel-Outline:

```markdown
### Kapitel X: "[Arbeitstitel]"
- **Akt:** [1/2/3] | **POV:** [Charaktername] | **Ort:** [Hauptort]
- **Funktion:** [Was soll dieses Kapitel erreichen? 1-2 Sätze]
- **Status:** 📝 Geplant (detailliert)

**Outline:**

1. **Szene 1: [Beschreibender Titel]** (ca. 700-1000 Wörter)
   - **Setting:** [Ort, Tageszeit, Wetter, Atmosphäre]
   - **Anwesend:** [Liste der Charaktere]
   - **Beats:**
     * [POV-Charakter] [macht/denkt/fühlt X]
     * [Ereignis Y passiert]
     * [Reaktion darauf führt zu Z]
     * [Wie endet die Szene - Transition zur nächsten]
   - **Zeigt:** [Charakter-Traits, Worldbuilding-Details]
   - **Foreshadowing:** [Was wird angedeutet für spätere Kapitel]
   - **Emotionaler Ton:** [Angespannt, hoffnungsvoll, düster, etc.]

2. **Szene 2: [Beschreibender Titel]** (ca. 800-1200 Wörter)
   - **Setting:** [Neuer Ort oder Zeitsprung]
   - **Anwesend:** [Liste der Charaktere]
   - **Beats:**
     * [Detaillierte Abfolge von Ereignissen]
     * [...]
   - **Dialog-Highlights:**
     * [Charakter A]: "[Wichtige Zeile die den Kern trifft]"
     * [Charakter B]: "[Wichtige Antwort/Reaktion]"
   - **Entwickelt:** [Was ändert sich? Plot/Charakter/Beziehung]
   - **Konflikte:** [Äußere und innere Konflikte in dieser Szene]

3. **Szene 3: [Beschreibender Titel]** (ca. 600-800 Wörter)
   - [Analog zu Szenen 1-2]
   - [So viele Szenen wie nötig für das Kapitel]

**Emotionaler Bogen des Kapitels:**
[Start-Emotion] → [Mittel-Emotion] → [End-Emotion]
(z.B. "Hoffnung → Zweifel → Entschlossenheit")

**Kapitel-Ende (Hook):**
[Beschreibung wie das Kapitel enden soll]
- Cliffhanger? Ruhiger Moment? Revelation? Entscheidung?
- Ungefährer letzter Satz: "[Beispiel oder Stimmung]"

**Wichtig für Plot:**
- [Ereignis 1 das in Timeline eingetragen werden muss]
- [Ereignis 2 das spätere Kapitel aufgreift]
- [Wendepunkt / Entwicklung für Handlungsstrang X]

**Wichtig für Charaktere:**
- **[POV-Charakter]:** [Entwicklung/Erkenntnis in diesem Kapitel]
- **[Anderer Charakter]:** [Wie ändert sich Beziehung/Status/Wissen]

**Checkliste vor dem Schreiben:**
- [ ] Timeline gecheckt? (Zeitpunkt: [Datum/Tag])
- [ ] Charaktere konsistent? (Traits, Motivation, Wissen, Status)
- [ ] Setting-Details aus Worldbuilding/[Datei].md verfügbar?
- [ ] Kontinuität zu Kapitel [X-1] klar?
- [ ] Handlungsstränge [A/B/C] berücksichtigt?
- [ ] Magiesystem/Technologie-Regeln im Blick?

**Notizen für den Schreibprozess:**
- **Zu recherchieren:** [Fehlende Details]
- **Zu beachten:** [Besondere Herausforderungen]
- **Flexibilität erlaubt bei:** [Wo der Schreibprozess abweichen darf]
- **Besonders wichtig:** [Worauf besonders zu achten ist]
```

#### Detailgrad anpassen:

**Für nächstes zu schreibendes Kapitel:**
- Sehr detailliert (wie oben)
- Alle Szenen durchgeplant
- Dialog-Highlights vorbereitet

**Für Kapitel in naher Zukunft (1-3 Kapitel voraus):**
- Mittel detailliert
- Haupt-Beats klar
- Szenen skizziert

**Für Kapitel in ferner Zukunft:**
- Grob
- Funktion + wichtigste Ereignisse
- Details später ergänzen

### SCHRITT 6: Story-Outline.md aktualisieren

1. **Öffne** `@Plot/Story-Outline.md`
2. **Finde** das entsprechende Kapitel
3. **Ersetze** die grobe/alte Outline durch deine neue detaillierte Version
4. **Update Status:**
   - 🎯 (Zu planen) → 📝 (Geplant)
   - Oder 📝 (grob geplant) → 📝 (detailliert geplant)
5. **Update YAML:** `last_updated: [Aktuelles Datum]`

### SCHRITT 7: Konsistenz-Check nach Planung

**Prüfe nochmal:**
- Passt die Planung zur Timeline?
- Sind alle Charaktere verfügbar/an richtigen Orten?
- Werden Handlungsstränge logisch fortgeführt?
- Gibt es Konflikte mit Worldbuilding-Regeln?

**Bei Problemen:** Notiere in Outline unter "Notizen" oder in `/Plot/Offene-Fragen.md`

### SCHRITT 8: Bestätigung an Autor

```
✅ KAPITEL X DETAILLIERT GEPLANT

**Kapitel:** [X] - "[Titel]"
**POV:** [Charaktername]
**Akt:** [1/2/3]
**Hauptort:** [Ort]

**Szenen:** [Anzahl] Szenen geplant
**Geschätzte Länge:** ca. [X] Wörter

---

**Kern dieses Kapitels:**
[2-3 Sätze was passieren wird]

**Emotionaler Bogen:**
[Start] → [Mitte] → [Ende]

**Wichtig für die Story:**
- [Plot-Punkt 1]
- [Plot-Punkt 2]

---

**Status-Updates durchgeführt:**
- ✅ Story-Outline.md aktualisiert (Status: 📝 Geplant)
- ✅ Konsistenz geprüft (Timeline ✓, Charaktere ✓, Handlungsstränge ✓)
- ✅ Checkliste für Schreibprozess erstellt

**Bereit zum Schreiben!**
Sage "Schreibe Kapitel X" wenn du bereit bist.

[Falls Warnungen/Hinweise:]
⚠️ **Hinweise:**
- [Hinweis 1]
- [Hinweis 2]
```

---

## Workflow: BATCH-PLANUNG (Mehrere Kapitel)

### Aktivierung
Wenn Autor sagt:
- "Plane Kapitel X bis Y"
- "Erstelle Outlines für die nächsten [N] Kapitel"
- "Plane [Akt 2]" (alle Kapitel eines Akts)

### SCHRITT 1: Kontext laden (automatisch)

```
@Meta/CORE-RULES.md
@PROJECT-CONTEXT.md
@Plot/Story-Outline.md
@Plot/Timeline.md
@Plot/Handlungsstränge.md
@Characters/_Relationships.md
@Characters/_INDEX.md
@Worldbuilding/_INDEX.md
```

### SCHRITT 2: Bereich analysieren

1. **Identifiziere Kapitel-Bereich:** [X] bis [Y]
2. **Prüfe Status** jedes Kapitels in Story-Outline.md
3. **Identifiziere Akt-Zugehörigkeit:**
   - Alle im selben Akt?
   - Übergang zwischen Akten?
4. **Identifiziere Story-Phase:**
   - Setup, Konfrontation, Auflösung?
   - Steigende Aktion, Midpoint, Climax?

### SCHRITT 3: Übersichts-Planung

**Erstelle mentale Roadmap:**
- Wie entwickeln sich Handlungsstränge über diese Kapitel?
- Welche Charakterentwicklung findet statt?
- Wo sind Wendepunkte?
- Wie ist das Pacing? (Action/Ruhe-Wechsel)
- Emotionaler Bogen über mehrere Kapitel?

### SCHRITT 4: Einzelne Kapitel planen

**Für jedes Kapitel (X, X+1, X+2, ... bis Y):**

Führe den normalen Planning-Workflow durch (Schritte 3-5 von oben):
- Lade relevante Charaktere/Settings
- Erstelle detaillierte Outline
- **ABER:** Achte besonders auf Kontinuität zwischen den Kapiteln!

**Zwischen Kapiteln checken:**
- Endet Kap X sinnvoll für Start von Kap X+1?
- Entwickeln sich Charaktere graduell?
- Handlungsstränge kohärent?
- Pacing variiert (nicht alle Action oder alle Ruhe)?

### SCHRITT 5: Kohärenz-Check über alle Kapitel

**Nach allen Planungen prüfen:**

1. **Liest sich die Sequenz logisch?**
   - Kapitel für Kapitel durchgehen
   - Übergänge sinnvoll?

2. **Charakterentwicklung graduell?**
   - Keine Sprünge in Persönlichkeit
   - Entwicklung nachvollziehbar über Zeit

3. **Pacing und Spannungsbögen gut?**
   - Wechsel zwischen Intensität
   - Ruhige Momente für Charakterentwicklung
   - Aufbau zu Wendepunkten

4. **Timeline macht Sinn?**
   - Realistische Zeitspannen
   - Events chronologisch

5. **Handlungsstränge verfolgt?**
   - A/B/C-Plots alle bedient
   - Keiner vergessen über lange Zeit

### SCHRITT 6: Story-Outline.md aktualisieren

**Alle geplanten Kapitel auf einmal:**
1. Durchgehe Story-Outline.md
2. Update jedes geplante Kapitel mit detaillierter Outline
3. Update alle Status auf 📝 Geplant
4. Update `last_updated` im YAML

### SCHRITT 7: Zusammenfassung an Autor

```
✅ KAPITEL X BIS Y GEPLANT

**Bereich:** Kapitel [X]-[Y] ([N] Kapitel)
**Akt:** [X] (oder "Übergang von Akt X zu Akt Y")
**Story-Phase:** [Setup/Konfrontation/Auflösung]

**Gesamt geschätzte Wortanzahl:** ca. [X] Wörter

---

## Kapitel-Übersicht:

**Kapitel [X]:** "[Titel]"
- POV: [Name]
- Kern: [1 Satz Zusammenfassung]

**Kapitel [X+1]:** "[Titel]"
- POV: [Name]
- Kern: [1 Satz Zusammenfassung]

[... alle Kapitel ...]

**Kapitel [Y]:** "[Titel]"
- POV: [Name]
- Kern: [1 Satz Zusammenfassung]

---

## Handlungsstrang-Entwicklung:

**A-Plot:** [Wie entwickelt er sich von Kap X zu Y]
**B-Plot:** [Wie entwickelt er sich von Kap X zu Y]
**C-Plot:** [Wie entwickelt er sich von Kap X zu Y]

**Wichtige Wendepunkte:**
- Kapitel [Z]: [Ereignis]
- Kapitel [W]: [Ereignis]

---

**Status-Updates durchgeführt:**
- ✅ Story-Outline.md: [N] Kapitel detailliert geplant
- ✅ Konsistenz zwischen Kapiteln geprüft
- ✅ Timeline-Kompatibilität bestätigt
- ✅ Handlungsstrang-Kohärenz sichergestellt
- ✅ Pacing-Balance geprüft

**Alle Kapitel sind bereit zum Schreiben!**
Du kannst nun jedes dieser Kapitel einzeln schreiben.
```

---

## Spezialfälle

### Fall 1: Kapitel ist schon geschrieben

Wenn Status = ✅ Geschrieben:

```
ℹ️ HINWEIS:
Kapitel X ist bereits geschrieben (Status: ✅).

Möchtest du:
1. Das Kapitel überarbeiten? (Sage: "Überarbeite Kapitel X")
2. Die Outline anpassen an was geschrieben wurde?
3. Einen Konsistenz-Check durchführen?
```

### Fall 2: Outline existiert schon (detailliert)

Wenn Status = 📝 und Outline ist detailliert:

```
ℹ️ HINWEIS:
Kapitel X hat bereits eine detaillierte Outline.

Möchtest du:
1. Die bestehende Outline überarbeiten?
2. Eine neue Planung erstellen (überschreibt alte)?
3. Die bestehende Outline anschauen und dann schreiben?
```

### Fall 3: Fehlende Informationen

Wenn wichtige Charaktere/Settings nicht dokumentiert sind:

```
⚠️ FEHLENDE DOKUMENTATION:

Für die Planung von Kapitel X brauche ich:
- Charakter: [Name] - Keine Charakterdatei gefunden
- Setting: [Ort] - Keine Worldbuilding-Datei gefunden

Optionen:
1. Ich erstelle Basis-Dateien mit Platzhaltern
2. Du gibst mir die Info, ich plane dann weiter
3. Wir überspringen diese Details erstmal

Wie sollen wir vorgehen?
```

### Fall 4: Timeline-Konflikt erkannt

```
⚠️ TIMELINE-KONFLIKT:

Bei der Planung von Kapitel X habe ich ein Problem gefunden:
[Beschreibung des Konflikts]

Laut Timeline: [Was steht da]
Geplant für Kap X: [Was wir vorhaben]

Soll ich:
1. Das Kapitel anpassen?
2. Die Timeline korrigieren?
3. Beides nochmal mit dir durchgehen?
```

---

## Best Practices für Planung

### Gute Kapitel-Outlines haben:

✅ **Klare Struktur:** 2-4 Szenen pro Kapitel
✅ **Spezifische Beats:** Nicht "Sie reden", sondern "Elena gesteht Jakob ihr Geheimnis"
✅ **Emotionaler Bogen:** Kapitel beginnt und endet in unterschiedlichem emotionalen Zustand
✅ **Plot-Voranbringung:** Mindestens ein Ereignis das die Story bewegt
✅ **Charakter-Moment:** Zeigt oder entwickelt Charakter
✅ **Sinnvolle Länge:** 2000-4000 Wörter (variiert je nach Pacing)

### Vermeide:

❌ **Zu vage:** "Etwas Wichtiges passiert"
❌ **Zu starr:** Jedes Detail festgelegt (lässt keinen Raum beim Schreiben)
❌ **Isoliert:** Kapitel ohne Bezug zu Rest der Story
❌ **Funktionslos:** Kapitel die nichts bewegen (Plot oder Charakter)

### Pacing-Balance über mehrere Kapitel:

- **Action → Ruhe → Action** Rhythmus
- Nach intensiven Kapiteln: Charaktermomente
- Vor Climax: Ruhe vor dem Sturm
- Nach Wendepunkt: Zeit für Reaktion/Verarbeitung

---

**Dieser Skill ist aktiv. Du führst ihn autonom aus bei entsprechenden Kommandos.**
