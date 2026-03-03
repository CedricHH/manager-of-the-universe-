# Consistency Rules - Konsistenz-Checks

## Zweck
Diese Datei definiert alle Konsistenz-Checks die du durchführst. Lade sie bei:
- Expliziter Konsistenzprüfung
- Beim Planen neuer Kapitel
- Beim Schreiben (implizit)
- Bei Struktur-Analysen

## Automatische Checks die du IMMER durchführst

### 1. Charakter-Konsistenz

#### Bei Planung/Schreiben prüfen:

**A) Existenz:**
- Ist jeder erwähnte Charakter in `/Characters/` dokumentiert?
- Falls NEIN: Warnung + Angebot neue Charakterdatei anzulegen

**B) Wissens-Konsistenz:**
- Was weiß dieser Charakter zu diesem Zeitpunkt?
- Hat der Charakter in früheren Kapiteln relevante Info erhalten?
- Beispiel: "Elena kann nicht über die Prophezeiung wissen, die wurde erst in Kap 7 enthüllt (aktuell Kap 5)"

**C) Status-Konsistenz:**
- Ist der Charakter zu diesem Zeitpunkt lebendig/tot/verwundet?
- Wo befindet sich der Charakter (Reisezeit realistisch)?
- Emotionaler Zustand: Passt zur vorherigen Entwicklung?

**D) Trait-Konsistenz:**
- Handelt der Charakter entsprechend seiner Persönlichkeit?
- Falls OOC (Out of Character): Gibt es guten Grund? (Entwicklung, Druck, etc.)
- Beispiel: "Jakob ist normalerweise zurückhaltend, warum handelt er hier impulsiv?"

**E) Beziehungs-Konsistenz:**
- Stimmt die Dynamik mit `/Characters/_Relationships.md`?
- Haben sich Beziehungen seit letztem Kapitel entwickelt?
- Dokumentiere Änderungen!

**F) Alters-Konsistenz:**
- Prüfe bei Timeline-Sprüngen: Stimmt das Alter noch?
- Besonders wichtig bei langen Zeitspannen

#### Warnung ausgeben bei:
```
⚠️ CHARAKTER-KONSISTENZ:
Problem: [Beschreibung]
Charakter: [Name]
Gefunden in: [Kapitel/Szene]
Konflikt mit: [Charakterdatei/früheres Kapitel]

Mögliche Lösungen:
1. [Option 1]
2. [Option 2]

Wie soll ich fortfahren?
```

### 2. Timeline-Konsistenz

#### Bei Planung/Schreiben prüfen:

**A) Chronologie:**
- Sind Ereignisse in richtiger Reihenfolge?
- Check gegen `/Plot/Timeline.md`
- Beispiel: "In Kap 3 ist es Tag 5, in Kap 4 plötzlich Tag 3?"

**B) Zeitspannen:**
- Passen Zeitangaben zwischen Kapiteln?
- Ist genug Zeit vergangen für Reisen/Heilung/Entwicklung?
- Beispiel: "Von Shadowvale nach Nordland dauert 3 Tage laut Worldbuilding, aber nur 1 Tag vergangen"

**C) Datum-Konsistenz:**
- Stimmt `timeline_date` im Kapitel-YAML mit Plot/Timeline.md?
- Chronologisch eingeordnet?

**D) Jahreszeiten/Wetter:**
- Falls relevant: Passt das Wetter zur Jahreszeit?
- Sind Jahreszeiten-Übergänge realistisch?

**E) Ereignis-Kontinuität:**
- Werden frühere Ereignisse korrekt referenziert?
- "Vor 2 Wochen" - stimmt das mit Timeline?

#### Warnung ausgeben bei:
```
⚠️ TIMELINE-KONSISTENZ:
Problem: [Beschreibung]
Aktuelles Kapitel: [X] (Datum: [Y])
Konflikt mit: [Kapitel/Timeline-Eintrag]

Timeline zeigt:
- [Ereignis A] am [Datum]
- [Ereignis B] am [Datum]

Vorschlag: [Lösung]
```

### 3. Worldbuilding-Konsistenz

#### Bei Planung/Schreiben prüfen:

**A) Orts-Konsistenz:**
- Stimmt Ortsbeschreibung mit `/Worldbuilding/Orte.md`?
- Beispiel: "Shadowvale hat laut Worldbuilding keinen Fluss, aber hier wird einer erwähnt"

**B) System-Konsistenz (Magie/Technologie):**
- Halten sich Charaktere an die Regeln?
- Check gegen `/Worldbuilding/Magiesystem.md` (oder ähnlich)
- Beispiel: "Magie kostet Lebensenergie, aber hier wird das nicht erwähnt"

**C) Kulturelle Konsistenz:**
- Verhalten passend zur Kultur?
- Gesellschaftliche Regeln beachtet?
- Check gegen `/Worldbuilding/Gesellschaft.md` oder `/Worldbuilding/Kultur.md`

**D) Historische Konsistenz:**
- Werden historische Ereignisse korrekt referenziert?
- Check gegen `/Worldbuilding/Geschichte.md`

**E) Technologie-Level:**
- Passt verwendete Technologie zum Setting?
- Keine Anachronismen

#### Warnung ausgeben bei:
```
⚠️ WORLDBUILDING-KONSISTENZ:
Problem: [Beschreibung]
Im Kapitel: [Was steht da]
Laut Worldbuilding: [Was sollte es sein]
Datei: [Worldbuilding/X.md]

Optionen:
1. Kapitel anpassen
2. Worldbuilding aktualisieren (wenn bewusste Änderung)

Wie soll ich vorgehen?
```

### 4. Plot-Konsistenz

#### Bei Planung/Schreiben prüfen:

**A) Handlungsstrang-Kontinuität:**
- Werden alle aktiven Threads bedient oder bewusst pausiert?
- Check gegen `/Plot/Handlungsstränge.md`
- Beispiel: "A-Plot wurde seit 3 Kapiteln nicht erwähnt"

**B) Foreshadowing-Tracking:**
- Wurde etwas angedeutet das hier aufgelöst werden sollte?
- Oder: Wird hier etwas eingeführt das Foreshadowing brauchte?

**C) Motivation-Konsistenz:**
- Warum tun Charaktere was sie tun?
- Passt zur etablierten Motivation?

**D) Konflikt-Eskalation:**
- Entwickelt sich der Konflikt logisch?
- Keine Sprünge in Intensität ohne Grund

**E) Checkov's Gun:**
- Werden eingeführte Elemente später genutzt?
- Oder: Werden hier Elemente genutzt die nie etabliert wurden?

#### Warnung ausgeben bei:
```
⚠️ PLOT-KONSISTENZ:
Problem: [Beschreibung]
Handlungsstrang: [A/B/C-Plot]
Letztes Vorkommen: [Kapitel X]
Status: [Was fehlt/nicht passt]

Empfehlung: [Lösung]
```

### 5. Kontinuität zwischen Kapiteln

#### Bei Planung/Schreiben prüfen:

**A) Kapitel-Übergänge:**
- Wie endete das vorherige Kapitel?
- Beginnt dieses Kapitel logisch danach?
- Check: `@Chapters/Kapitel-[X-1].md`

**B) POV-Wechsel:**
- Falls POV wechselt: Ist das konsistent mit Muster?
- Weiß der neue POV-Charakter was im letzten Kapitel passiert ist?

**C) Emotionaler Zustand:**
- Charaktere beginnen mit emotionalem Zustand vom Ende des letzten Kapitels
- Außer: Zeit ist vergangen (dann dokumentieren)

**D) Offene Fragen:**
- Check `/Plot/Offene-Fragen.md`
- Werden hier Fragen beantwortet?
- Entstehen neue Fragen? → Dokumentieren!

#### Warnung ausgeben bei:
```
⚠️ KONTINUITÄTS-PROBLEM:
Zwischen: Kapitel [X] und [Y]
Problem: [Beschreibung]

Kapitel [X] endete: [Zustand]
Kapitel [Y] beginnt: [Zustand]
Konflikt: [Was passt nicht]

Lösung: [Vorschlag]
```

### 6. Statistische Konsistenz

#### Bei Updates prüfen:

**A) Wortanzahl:**
- Stimmt word_count im YAML mit tatsächlicher Länge?
- Update in `/Chapters/_INDEX.md` korrekt?

**B) Kapitel-Nummerierung:**
- Keine Lücken oder Dopplungen
- Fortlaufend

**C) Gesamt-Fortschritt:**
- Prozent-Berechnung in `_INDEX.md` korrekt?
- Ziel-Wortanzahl im Blick

## Proaktive Warnsysteme

### Du warnst proaktiv wenn:

**1. Fehlende Dokumentation:**
```
💡 EMPFEHLUNG:
[Charakter X] wird in Kapitel Y erwähnt, aber ich finde keine Charakterdatei.

Soll ich eine Basis-Charakterdatei erstellen?
Oder wird dieser Charakter nur erwähnt und tritt nicht auf?
```

**2. Timeline-Lücken:**
```
💡 HINWEIS:
Zwischen Kapitel X (Tag 5) und Kapitel Y (Tag 12) liegen 7 Tage.

Willst du diese Zeit in der Timeline dokumentieren?
Oder passiert in dieser Zeit nichts relevantes?
```

**3. Lose Fäden:**
```
💡 PLOT-TRACKING:
In Kapitel X wurde [Element] eingeführt, aber seit 5 Kapiteln nicht mehr erwähnt.

Ist das bewusst (kommt später)?
Oder soll ich in Offene-Fragen.md notieren?
```

**4. Mögliche Widersprüche:**
```
⚠️ MÖGLICHER WIDERSPRUCH:
In Kapitel X: [Aussage A]
In Kapitel Y (aktuell): [Aussage B]

Ist das ein Widerspruch oder bewusste Entwicklung?
```

**5. Pacing-Hinweise:**
```
💡 PACING-HINWEIS:
Die letzten 3 Kapitel waren Action-lastig (hohe Intensität).

Ist ein ruhigerer Moment geplant zur Charakterentwicklung?
Oder soll die Spannung weiter steigen?
```

## Konsistenz-Prüfung auf Anfrage

### "Konsistenzprüfung" Kommando:

Wenn Autor sagt: "Konsistenzprüfung" oder "Prüfe Konsistenz"

**Du führst durch:**

1. Lade alle relevanten Dateien:
```
@PROJECT-CONTEXT.md
@Plot/Story-Outline.md
@Plot/Timeline.md
@Plot/Handlungsstränge.md
@Characters/_INDEX.md
@Characters/_Relationships.md
@Worldbuilding/_INDEX.md
@Chapters/_INDEX.md
@WRITING-LOG.md
```

2. Prüfe systematisch:
   - Timeline: Chronologie, Datumskonsistenz
   - Charaktere: Status, Wissen, Beziehungen
   - Plot: Handlungsstränge, offene Fragen
   - Worldbuilding: Systemregeln eingehalten?
   - Statistik: Zahlen stimmen?

3. Erstelle Bericht:
```
📊 KONSISTENZ-BERICHT

**Projekt:** [Titel]
**Geprüft:** [Datum]
**Umfang:** [X] Kapitel geschrieben

---

## ✅ Konsistent

**Timeline:** Keine Probleme gefunden
**Charaktere:** Alle dokumentiert und konsistent
**Plot:** Handlungsstränge verfolgt

---

## ⚠️ Potenzielle Probleme

### Timeline
- [Problem 1 mit Details]
- [Problem 2 mit Details]

### Charaktere
- [Problem 1 mit Details]

### Worldbuilding
- [Problem 1 mit Details]

---

## 💡 Empfehlungen

- [Empfehlung 1]
- [Empfehlung 2]

---

Soll ich eines dieser Probleme genauer untersuchen?
```

### "Konsistenzprüfung [Bereich]" Kommando:

Fokussierte Prüfung:
- "Konsistenzprüfung Timeline" → Nur Timeline
- "Konsistenzprüfung Charaktere" → Nur Charaktere
- "Konsistenzprüfung Plot" → Nur Handlungsstränge
- "Konsistenzprüfung Kapitel X" → Nur dieses Kapitel vs. Rest

## Häufige Inkonsistenzen & Lösungen

### Problem: Charakter kennt Info die er nicht haben sollte
**Lösung:**
1. Prüfe: Wann wurde Info enthüllt?
2. War Charakter anwesend/hat davon erfahren?
3. Falls NEIN: Entweder Kapitel anpassen ODER frühere Szene hinzufügen wo Charakter es erfährt

### Problem: Zeitliche Unmöglichkeit
**Lösung:**
1. Prüfe Timeline: Wie viel Zeit vergangen?
2. Prüfe Worldbuilding: Wie lange dauert Reise/Heilung/etc.?
3. Entweder: Mehr Zeit einfügen ODER Ereignisse anpassen

### Problem: Magiesystem-Regel gebrochen
**Lösung:**
1. Prüfe Worldbuilding/Magiesystem.md
2. Ist das bewusste Ausnahme? (Dann dokumentieren!)
3. Oder Fehler? (Dann Kapitel anpassen)

### Problem: Handlungsstrang vergessen
**Lösung:**
1. Prüfe Handlungsstränge.md: Wann zuletzt erwähnt?
2. War Pause bewusst? (Gut für Pacing)
3. Oder vergessen? → In nächstes Kapitel einbauen oder in Offene-Fragen.md notieren

## Dokumentation von bewussten Inkonsistenzen

**Manchmal sind "Inkonsistenzen" bewusst:**
- Unreliable Narrator
- Charakter irrt sich
- Widersprüchliche Quellen in der Welt
- Plot Twist Vorbereitung

**In diesen Fällen:**
1. In WRITING-LOG.md dokumentieren: "Bewusste Inkonsistenz in Kap X wegen [Grund]"
2. In Story-Outline.md bei relevantem Kapitel notieren
3. Optional: In Plot/Offene-Fragen.md als "Später auflösen"

---

**Bei Konsistenz-Fragen oder -Problemen: Diese Datei konsultieren!**
