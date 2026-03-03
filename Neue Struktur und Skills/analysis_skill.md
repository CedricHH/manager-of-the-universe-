# Analysis Skill - Struktur- & Konsistenz-Checks

## Zweck
Dieser Skill definiert wie du Struktur-Checks und Konsistenz-Analysen durchführst. Er wird aktiviert bei:
- "Strukturcheck"
- "Konsistenzprüfung"
- "Analysiere [Bereich]"
- Automatisch bei jeder Interaktion (leichter Check im Hintergrund)

## Workflow: Vollständiger Strukturcheck

### Aktivierung
Wenn Autor sagt: "Strukturcheck" oder "Prüfe die Struktur"

### SCHRITT 1: Dateien laden (automatisch)

```
@Meta/CORE-RULES.md
@PROJECT-CONTEXT.md
@Plot/_INDEX.md
@Plot/Story-Outline.md
@Characters/_INDEX.md
@Chapters/_INDEX.md
@Worldbuilding/_INDEX.md
@WRITING-LOG.md
```

### SCHRITT 2: Struktur-Scan durchführen

**Prüfe Existenz aller Kern-Komponenten:**

#### Absolut notwendig:
- [ ] `PROJECT-CONTEXT.md` existiert
- [ ] `Meta/CORE-RULES.md` existiert
- [ ] `Plot/Story-Outline.md` existiert (KRITISCH!)
- [ ] `Chapters/_INDEX.md` existiert

#### Sehr empfohlen:
- [ ] `Characters/_INDEX.md` existiert
- [ ] `Plot/Timeline.md` existiert
- [ ] `WRITING-LOG.md` existiert
- [ ] `Plot/Handlungsstränge.md` existiert

#### Optional aber nützlich:
- [ ] `Characters/_Relationships.md` existiert
- [ ] `Plot/Konflikte.md` existiert
- [ ] `Plot/Offene-Fragen.md` existiert
- [ ] `Worldbuilding/_INDEX.md` existiert
- [ ] Alle Rule-/Skill-Dateien in `/Meta/` vorhanden

### SCHRITT 3: Zähle vorhandene Elemente

**Scanne Verzeichnisse:**
- Anzahl Charaktere in `/Characters/`
- Anzahl Kapitel in `/Chapters/`
- Anzahl Worldbuilding-Elemente in `/Worldbuilding/`

**Vergleiche mit INDEX-Dateien:**
- Sind alle Charaktere in `Characters/_INDEX.md` aufgelistet?
- Sind alle Kapitel in `Chapters/_INDEX.md` aufgelistet?
- Sind alle Worldbuilding-Elemente in `Worldbuilding/_INDEX.md`?

### SCHRITT 4: Status-Übersicht aus Story-Outline

**Zähle Kapitel nach Status:**
- 📝 Geplant: [X]
- 🎯 Zu planen: [X]
- 🔄 In Arbeit: [X]
- ✅ Geschrieben: [X]
- ✏️ Revision: [X]
- 🎉 Fertig: [X]

### SCHRITT 5: Strukturcheck-Bericht

```
📋 STRUKTURCHECK ABGESCHLOSSEN

**Projekt:** [Titel aus PROJECT-CONTEXT]
**Geprüft am:** [Datum]
**Letztes Update:** [Aus WRITING-LOG oder Story-Outline]

═══════════════════════════════════════════════════════

## 📊 STRUKTUR-STATUS

### Kern-Dateien:
✅ PROJECT-CONTEXT.md - Vorhanden
✅ Meta/CORE-RULES.md - Vorhanden
✅ Plot/Story-Outline.md - Vorhanden
✅ Chapters/_INDEX.md - Vorhanden

### Empfohlene Dateien:
[✅/⚠️/❌] Characters/_INDEX.md - [Status]
[✅/⚠️/❌] Plot/Timeline.md - [Status]
[✅/⚠️/❌] WRITING-LOG.md - [Status]
[✅/⚠️/❌] Plot/Handlungsstränge.md - [Status]

### Optional:
[✅/❌] Characters/_Relationships.md
[✅/❌] Plot/Offene-Fragen.md
[✅/❌] Worldbuilding/_INDEX.md

---

## 📈 PROJEKT-ÜBERSICHT

**Ziel:** [X] Kapitel, [Y] Wörter
**Status:** [Planung/Entwurf/Revision/etc.]

### Kapitel-Status:
- 🎉 Fertig: [X] Kapitel
- ✅ Geschrieben: [X] Kapitel
- ✏️ Revision: [X] Kapitel
- 🔄 In Arbeit: [X] Kapitel
- 📝 Geplant: [X] Kapitel
- 🎯 Zu planen: [X] Kapitel

**Gesamt geschrieben:** [X]/[Ziel] Kapitel ([%])
**Wortanzahl:** [X]/[Ziel] Wörter ([%])

### Akt-Fortschritt:
- **Akt 1** (Kap 1-X): [Status, % fertig]
- **Akt 2** (Kap Y-Z): [Status, % fertig]
- **Akt 3** (Kap A-B): [Status, % fertig]

---

## 📚 INHALTS-ÜBERSICHT

**Charaktere:** [X] dokumentiert
- Hauptcharaktere: [X]
- Nebencharaktere: [X]
- Antagonisten: [X]

**Worldbuilding-Elemente:** [X] dokumentiert
- Orte: [X]
- Systeme: [X]
- Geschichte: [X]
- Kultur: [X]

**Handlungsstränge:** [X] definiert
- A-Plot: [Status]
- B-Plot: [Status]
- C-Plot: [Status]

---

## [Falls Probleme gefunden:]

⚠️ GEFUNDENE PROBLEME

### Fehlende Komponenten:
- [Liste fehlender wichtiger Dateien]

### Inkonsistenzen:
- [Liste von Inkonsistenzen zwischen Dateien]

### Verwaiste Elemente:
- [Dateien die existieren aber nicht in INDEX gelistet]
- [INDEX-Einträge ohne entsprechende Dateien]

---

## 💡 EMPFEHLUNGEN

[Basierend auf Befunden:]

**Hohe Priorität:**
- [Empfehlung 1]
- [Empfehlung 2]

**Mittlere Priorität:**
- [Empfehlung 1]

**Optional:**
- [Empfehlung 1]

═══════════════════════════════════════════════════════

**Soll ich eines der Probleme beheben?**
Oder möchtest du mit deiner ursprünglichen Anfrage fortfahren?
```

---

## Workflow: Vollständige Konsistenz-Prüfung

### Aktivierung
Wenn Autor sagt: "Konsistenzprüfung" oder "Prüfe Konsistenz"

### SCHRITT 1: Dateien laden (automatisch)

```
@Meta/CORE-RULES.md
@Meta/Consistency-Rules.md
@PROJECT-CONTEXT.md
@Plot/Story-Outline.md
@Plot/Timeline.md
@Plot/Handlungsstränge.md
@Characters/_INDEX.md
@Characters/_Relationships.md
@Worldbuilding/_INDEX.md
@Chapters/_INDEX.md
@WRITING-LOG.md
@Chapters/[Alle geschriebenen Kapitel]  # Oder zumindest Sample
```

### SCHRITT 2: Timeline-Konsistenz prüfen

**Prüfe:**
1. **Chronologische Reihenfolge:**
   - Sind Ereignisse in Timeline.md chronologisch?
   - Passen `timeline_date` in Kapiteln zu Timeline?

2. **Zeitspannen realistisch:**
   - Genug Zeit für Reisen? (Check gegen Worldbuilding)
   - Genug Zeit für Heilung?
   - Genug Zeit für Charakterentwicklung?

3. **Zeitliche Referenzen:**
   - Stimmen "gestern", "vor 3 Tagen" etc. in Kapiteln?
   - Konsistent mit Timeline?

**Probleme notieren:**
```
⚠️ Timeline-Problem: [Beschreibung]
Gefunden in: [Kapitel/Datei]
Konflikt mit: [Andere Stelle]
```

### SCHRITT 3: Charakter-Konsistenz prüfen

**Für jeden Hauptcharakter:**

1. **Wissens-Konsistenz:**
   - Wann erfährt Charakter wichtige Infos?
   - Handelt Charakter basierend auf seinem Wissensstand?
   - Kennt Charakter Dinge die er nicht wissen sollte?

2. **Status-Konsistenz:**
   - Lebendig/tot/verletzt konsistent?
   - Locations: Kann Charakter dort sein? (Reisezeit?)
   - Emotionaler Zustand nachvollziehbar entwickelt?

3. **Trait-Konsistenz:**
   - Handelt Charakter in Character?
   - Falls OOC: Gibt es guten Grund?

4. **Beziehungs-Konsistenz:**
   - Entwickeln sich Beziehungen graduell?
   - Stimmt mit `_Relationships.md`?

**Probleme notieren:**
```
⚠️ Charakter-Problem: [Beschreibung]
Charakter: [Name]
Gefunden in: [Kapitel]
Konflikt mit: [Charakterdatei/anderes Kapitel]
```

### SCHRITT 4: Plot-Konsistenz prüfen

1. **Handlungsstrang-Tracking:**
   - Wird A-Plot regelmäßig bedient?
   - Wird B-Plot regelmäßig bedient?
   - Wird C-Plot regelmäßig bedient?
   - Lange Pausen zwischen Erwähnungen? (OK wenn bewusst)

2. **Foreshadowing vs Payoff:**
   - Wurde etwas angedeutet das nie aufgegriffen wurde?
   - Wurde etwas aufgelöst das nie etabliert wurde?

3. **Offene Fragen:**
   - Check gegen `Plot/Offene-Fragen.md`
   - Wurden Fragen beantwortet und aus Liste entfernt?
   - Neue Fragen entstanden und dokumentiert?

**Probleme notieren:**
```
⚠️ Plot-Problem: [Beschreibung]
Thread: [A/B/C-Plot]
Letztes Vorkommen: [Kapitel]
```

### SCHRITT 5: Worldbuilding-Konsistenz prüfen

1. **System-Regeln:**
   - Wird Magiesystem/Technologie konsistent genutzt?
   - Werden Regeln aus Worldbuilding-Dateien befolgt?

2. **Orts-Details:**
   - Stimmen Beschreibungen mit Worldbuilding/Orte.md?
   - Neue Orte dokumentiert?

3. **Kulturelle Konsistenz:**
   - Verhalten passend zur Kultur?
   - Gesellschaftliche Regeln beachtet?

**Probleme notieren:**
```
⚠️ Worldbuilding-Problem: [Beschreibung]
Im Kapitel: [Was steht da]
Laut Worldbuilding: [Was sollte es sein]
```

### SCHRITT 6: Statistik-Konsistenz prüfen

1. **Wortanzahlen:**
   - Stimmen word_count in Kapiteln mit tatsächlicher Länge?
   - Stimmen Summen in `Chapters/_INDEX.md`?

2. **Kapitel-Nummern:**
   - Fortlaufend, keine Lücken?
   - Stimmen mit Story-Outline.md?

3. **Status-Symbole:**
   - Konsistent zwischen Story-Outline und _INDEX?

### SCHRITT 7: Konsistenz-Bericht

```
📊 KONSISTENZ-BERICHT

**Projekt:** [Titel]
**Geprüft am:** [Datum]
**Umfang:** [X] Kapitel geschrieben, [Y] geplant

═══════════════════════════════════════════════════════

## ✅ KONSISTENTE BEREICHE

**Timeline:** [Status - z.B. "Keine Probleme gefunden"]
**Charaktere:** [Status - z.B. "Alle dokumentiert und konsistent"]
**Plot-Threads:** [Status - z.B. "Alle Stränge verfolgt"]
**Worldbuilding:** [Status - z.B. "Regeln eingehalten"]
**Statistik:** [Status - z.B. "Alle Zahlen korrekt"]

---

## ⚠️ POTENZIELLE PROBLEME

[Falls gefunden:]

### Timeline-Probleme ([X] gefunden):
1. **[Problem-Titel]**
   - **Beschreibung:** [Detail]
   - **Gefunden in:** [Kapitel X, Zeile Y]
   - **Konflikt mit:** [Timeline.md / anderes Kapitel]
   - **Vorschlag:** [Lösung]

2. [Weitere...]

### Charakter-Probleme ([X] gefunden):
1. **[Problem-Titel]**
   - **Charakter:** [Name]
   - **Beschreibung:** [Detail]
   - **Gefunden in:** [Kapitel X]
   - **Konflikt mit:** [Charakterdatei / anderes Kapitel]
   - **Vorschlag:** [Lösung]

### Plot-Probleme ([X] gefunden):
[Analog...]

### Worldbuilding-Probleme ([X] gefunden):
[Analog...]

### Statistik-Probleme ([X] gefunden):
[Analog...]

---

## 💡 EMPFEHLUNGEN

**Hohe Priorität (beheben vor weiterem Schreiben):**
- [Empfehlung 1]
- [Empfehlung 2]

**Mittlere Priorität (bald beheben):**
- [Empfehlung 1]

**Niedrige Priorität (kann warten):**
- [Empfehlung 1]

---

## 📈 POSITIVE BEOBACHTUNGEN

[Was gut läuft:]
- [Stärke 1]
- [Stärke 2]

═══════════════════════════════════════════════════════

**Möchtest du eines dieser Probleme genauer untersuchen?**
Oder soll ich eines direkt beheben?
```

---

## Workflow: Fokussierte Konsistenz-Prüfung

### Aktivierung
Wenn Autor sagt:
- "Konsistenzprüfung Timeline"
- "Konsistenzprüfung Charaktere"
- "Konsistenzprüfung Plot"
- "Konsistenzprüfung Kapitel X"

### Führe nur den entsprechenden Teil aus

**Beispiel "Konsistenzprüfung Timeline":**
- Nur Timeline-Checks (Schritt 2 von oben)
- Detaillierter als in vollständiger Prüfung
- Jeden einzelnen Zeitpunkt validieren

**Beispiel "Konsistenzprüfung Kapitel X":**
- Lade nur Kapitel X + Kontext
- Prüfe nur dieses Kapitel gegen:
  - Timeline
  - Charaktere
  - Worldbuilding
  - Vorheriges/Nächstes Kapitel

---

## Workflow: Leichter Background-Check

### Bei jeder Interaktion (automatisch, still)

**Schnell-Check (nicht melden außer bei Problemen):**

1. **Kern-Dateien vorhanden?**
   - PROJECT-CONTEXT.md ✓
   - Story-Outline.md ✓
   - Chapters/_INDEX.md ✓

2. **Offensichtliche Probleme?**
   - Kapitel in INDEX aber nicht vorhanden?
   - Story-Outline stark veraltet (last_updated lange her)?
   - Kapitel-Nummern mit Lücken?

**Falls Problem gefunden:**
```
⚠️ STRUKTURPROBLEM ENTDECKT:
[Kurze Beschreibung]

Möchtest du dass ich das jetzt behebe?
Oder soll ich mit deiner Anfrage fortfahren?
```

**Falls alles OK:**
- Nichts sagen, einfach weiterarbeiten
- Nur bei explizitem "Strukturcheck" berichten

---

## Spezial-Analysen

### Pacing-Analyse

**Wenn explizit angefordert:**

1. **Lade alle geschriebenen Kapitel**
2. **Analysiere:**
   - Wortanzahl pro Kapitel (Varianz)
   - Szenen-Anzahl pro Kapitel
   - Action vs. Ruhe (aus Kapitelinhalten schätzen)
   - Dialog vs. Beschreibung (Verhältnis)

3. **Erstelle Pacing-Bericht:**
```
📊 PACING-ANALYSE

**Durchschnittliche Kapitellänge:** [X] Wörter
**Kürzestes Kapitel:** Kap [X] ([Y] Wörter)
**Längstes Kapitel:** Kap [X] ([Y] Wörter)
**Varianz:** [Beschreibung]

**Pacing-Muster:**
- Kap 1-3: [Ruhig/Action/Mix]
- Kap 4-6: [Ruhig/Action/Mix]
- Kap 7-9: [Ruhig/Action/Mix]

**Beobachtungen:**
- [z.B. "Lange Action-Sequenz ohne Charaktermomente"]
- [z.B. "Gute Variation zwischen Intensität"]

**Empfehlungen:**
- [Vorschläge für besseres Pacing]
```

### Charakterentwicklungs-Tracking

**Wenn explizit angefordert (für einen Charakter):**

1. **Lade Charakterdatei + alle Kapitel wo Charakter auftritt**
2. **Tracke Entwicklung:**
   - Traits in frühen Kapiteln
   - Traits in späteren Kapiteln
   - Schlüsselmomente der Entwicklung
   - Beziehungsänderungen

3. **Erstelle Entwicklungs-Bericht:**
```
📈 CHARAKTERENTWICKLUNG: [Name]

**Kapitel 1 (Start):**
- Traits: [Liste]
- Status: [Beschreibung]
- Beziehungen: [Zustand]

**Schlüsselmomente:**
- Kap X: [Ereignis] → [Auswirkung]
- Kap Y: [Ereignis] → [Auswirkung]

**Aktuell (Kap [X]):**
- Traits: [Liste] [Änderungen markiert]
- Status: [Beschreibung]
- Beziehungen: [Zustand]

**Entwicklungs-Bogen:**
[Beschreibung der Gesamtentwicklung]

**Konsistenz:** [✅ Graduell / ⚠️ Sprunghaft]
```

---

## Automatisierte Fix-Vorschläge

### Wenn du ein Problem findest, biete Lösung an:

**Beispiel Timeline-Problem:**
```
⚠️ TIMELINE-WIDERSPRUCH GEFUNDEN:

**Problem:**
Kapitel 3: Elena ist in Shadowvale (Tag 5)
Kapitel 5: Elena ist in Nordland (Tag 6)

Laut Worldbuilding/Orte.md: Reise dauert 3 Tage

**Lösungsvorschläge:**

Option 1: Kapitel 5 Datum ändern
- Ändere timeline_date in Kap 5 auf "Tag 8"
- Update Timeline.md entsprechend
- Prüfe ob Folgekapitel betroffen

Option 2: Reise-Zeit anpassen
- Update Worldbuilding/Orte.md: Reise dauert 1 Tag (z.B. durch Magie)
- Konsistent mit neuer Regel weiterschreiben

Option 3: Kapitel 4 erweitern
- Füge Reise-Kapitel zwischen 3 und 5 ein
- Zeige die 3-tägige Reise

Welche Option bevorzugst du?
Oder hast du eine andere Lösung?
```

---

## Best Practices für Analysen

### ✅ Gute Analysen:

- **Konkret:** Zeige genau wo Problem ist (Kapitel, Zeile)
- **Konstruktiv:** Biete Lösungen an, nicht nur Kritik
- **Priorisiert:** Wichtige Probleme zuerst
- **Kontext-bewusst:** Verstehe die Story, nicht nur Regeln
- **Ausgewogen:** Zeige auch was gut funktioniert

### ❌ Vermeide:

- **Pedantisch:** Nicht jede Kleinigkeit ist ein Problem
- **Vage:** "Irgendwas stimmt nicht" hilft nicht
- **Überwältigend:** Nicht 50 Probleme auf einmal
- **Regelbesessen:** Manchmal sind bewusste Abweichungen OK
- **Negativ:** Nur Kritik ohne Anerkennung

---

**Dieser Skill ist aktiv. Du führst automatische Background-Checks bei jeder Interaktion durch und detaillierte Analysen auf Anfrage.**
