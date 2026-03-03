# Modulares Rules & Skills System für Romanprojekte

## 📚 Übersicht

Dieses System besteht aus **modularen Rules und Skills** die Claude helfen, dein Romanprojekt zu strukturieren, zu planen, zu schreiben und konsistent zu halten.

### Die Module:

```
/Meta
├── CORE-RULES.md           # ⭐ Kern - IMMER laden
├── Structure-Rules.md      # 📁 Detaillierte Struktur-Definitionen
├── Consistency-Rules.md    # ✓ Konsistenz-Check-Regeln
├── Style-Rules.md          # ✎ Erzählstil (vom Autor anzupassen)
├── Planning-Skill.md       # 🎯 Skill: Kapitel planen
├── Writing-Skill.md        # ✍️ Skill: Kapitel schreiben
├── Revision-Skill.md       # ✏️ Skill: Überarbeiten
└── Analysis-Skill.md       # 📊 Skill: Struktur-/Konsistenz-Checks
```

---

## 🚀 Quick Start

### 1. Initial Setup

**Erste Konversation mit Claude:**

```
@Meta/CORE-RULES.md @Meta/Structure-Rules.md

Lies diese Rules und führe einen initialen Strukturcheck durch. 
Erstelle alle fehlenden Basis-Komponenten.
```

**Was passiert:**
- Claude scannt deine Projekt-Struktur
- Erstellt fehlende Kern-Dateien (PROJECT-CONTEXT, Story-Outline, etc.)
- Gibt dir einen Status-Bericht

### 2. Style-Rules anpassen

**Wichtig:** Passe `Style-Rules.md` an deinen persönlichen Schreibstil an!

```
@Meta/Style-Rules.md

Ich möchte meinen Erzählstil definieren. 
Hilf mir die Style-Rules anzupassen.
```

### 3. Story planen

```
@Meta/CORE-RULES.md @Meta/Planning-Skill.md

Plane Kapitel 1 bis 5
```

### 4. Schreiben beginnen

```
@Meta/CORE-RULES.md @Meta/Writing-Skill.md

Schreibe Kapitel 1
```

**Claude wird automatisch:**
- Die Outline laden
- Das Kapitel schreiben
- ALLE betroffenen Dateien synchronisieren

---

## 📖 Welche Rules/Skills wann laden?

### Bei jeder Session (Minimum):
```
@Meta/CORE-RULES.md
```
Dann je nach Aufgabe zusätzliche Skills.

### Vollständige Lade-Matrix:

| Aufgabe | Dateien zum Laden |
|---------|-------------------|
| **Strukturcheck** | `@CORE-RULES.md @Structure-Rules.md @Analysis-Skill.md` |
| **Kapitel planen** | `@CORE-RULES.md @Planning-Skill.md` |
| **Kapitel schreiben** | `@CORE-RULES.md @Writing-Skill.md @Style-Rules.md` |
| **Kapitel überarbeiten** | `@CORE-RULES.md @Revision-Skill.md @Style-Rules.md` |
| **Konsistenzprüfung** | `@CORE-RULES.md @Consistency-Rules.md @Analysis-Skill.md` |
| **Neue Struktur erstellen** | `@CORE-RULES.md @Structure-Rules.md` |

**Aber:** CORE-RULES.md zeigt Claude welche Skills zu laden sind, also oft reicht:

```
@Meta/CORE-RULES.md

[Deine Anfrage]
```

Und Claude lädt die passenden zusätzlichen Skills selbst!

---

## 🎯 Typische Workflows

### Workflow 1: Mehrere Kapitel planen und schreiben

```
# Session Start
@Meta/CORE-RULES.md

# Batch-Planung
Plane Kapitel 5 bis 10

# Schreiben (nacheinander oder über mehrere Sessions)
Schreibe Kapitel 5
Schreibe Kapitel 6
Schreibe Kapitel 7
...

# Zwischendurch Konsistenz-Check
Konsistenzprüfung Kapitel 5 bis 7
```

### Workflow 2: Revision eines Kapitels

```
@Meta/CORE-RULES.md

Überarbeite Kapitel 3 - Fokus auf Dialog und Pacing
```

### Workflow 3: Große Struktur-Analyse

```
@Meta/CORE-RULES.md @Meta/Analysis-Skill.md

Führe einen vollständigen Strukturcheck und Konsistenzprüfung durch
```

### Workflow 4: Neue Charaktere/Worldbuilding hinzufügen

```
@Meta/CORE-RULES.md @Meta/Structure-Rules.md

Erstelle eine Charakterdatei für [Name] mit folgenden Infos: [...]

# Oder

Erstelle ein Worldbuilding-Dokument für das Magiesystem
```

---

## ✅ Vorteile des modularen Systems

### Effizienz:
- Nur relevante Rules laden → weniger Token
- Fokussierter Kontext → bessere Ergebnisse

### Wartbarkeit:
- Einzelne Module updaten statt alles
- Übersichtlicher für dich als Autor

### Flexibilität:
- Style-Rules leicht anpassbar
- Skills einzeln erweiterbar
- Neue Skills hinzufügen ohne Rest zu ändern

### Klarheit:
- Jedes Modul hat klaren Zweck
- Einfacher zu verstehen was Claude macht

---

## 🔄 System-Updates

### Wenn du Rules ändern willst:

1. **Öffne die relevante Datei** (z.B. `Style-Rules.md`)
2. **Passe an** was du ändern willst
3. **Beim nächsten Schreiben** lädt Claude die aktualisierten Rules

**Keine Sorge:** Claude passt sich automatisch an.

### Wenn du neue Skills hinzufügen willst:

1. **Erstelle neue `.md` Datei** in `/Meta/`
2. **Folge dem Format** der bestehenden Skills
3. **Referenziere sie** in CORE-RULES.md unter "Spezielle Kommandos"

---

## 📝 Best Practices

### ✅ Mache:

1. **CORE-RULES immer laden** (mindestens einmal pro Session)
2. **Style-Rules personalisieren** für deinen Stil
3. **Einen Skill nach dem anderen** nutzen (nicht alles auf einmal laden)
4. **Konsistenz-Checks regelmäßig** (z.B. nach jedem 5. Kapitel)
5. **WRITING-LOG.md lesen** vor neuer Session (um Kontext zu haben)

### ❌ Vermeide:

1. **Alle Skills gleichzeitig laden** (zu viel Kontext)
2. **Rules widersprechen lassen** (wenn du was änderst, sei konsistent)
3. **CORE-RULES überspringen** (enthält kritische Basis-Info)
4. **Style-Rules ignorieren** (definiere deinen Stil!)
5. **Sync-Updates manuell machen** (lass Claude das automatisch machen)

---

## 🛠️ Troubleshooting

### Problem: Claude vergisst Updates nach Schreiben

**Lösung:**
```
@Meta/CORE-RULES.md @Meta/Writing-Skill.md

Erinnerung: Nach dem Schreiben ALLE Sync-Updates durchführen:
1. Story-Outline.md
2. Chapters/_INDEX.md
3. Timeline.md
4. WRITING-LOG.md
5. Ggf. Charakterdateien
```

### Problem: Inkonsistenzen zwischen Dateien

**Lösung:**
```
@Meta/CORE-RULES.md @Meta/Consistency-Rules.md

Vollständige Konsistenzprüfung durchführen
```

### Problem: Struktur ist durcheinander

**Lösung:**
```
@Meta/CORE-RULES.md @Meta/Structure-Rules.md @Meta/Analysis-Skill.md

Strukturcheck durchführen und alle Probleme beheben
```

### Problem: Claude lädt nicht die richtigen Dateien

**Lösung:** 
Du musst sie explizit laden. Claude kann nur auf Dateien zugreifen die mit `@` geladen werden.

```
@Meta/CORE-RULES.md @Plot/Story-Outline.md @Characters/Elena.md

Schreibe Kapitel 5
```

---

## 📊 System-Übersicht Diagramm

```
┌─────────────────────────────────────────────────────────┐
│                     CORE-RULES.md                       │
│         (Immer laden - Zentrale Koordination)           │
└────────────────┬────────────────────────────────────────┘
                 │
        ┌────────┴─────────┐
        │                  │
   ┌────▼─────┐      ┌────▼─────────┐
   │  RULES   │      │    SKILLS    │
   └────┬─────┘      └────┬─────────┘
        │                 │
   ┌────┼─────┬─────┐    ├────┬─────┬─────┐
   │    │     │     │    │    │     │     │
   ▼    ▼     ▼     ▼    ▼    ▼     ▼     ▼
 Structure  Consistency  Planning Writing Revision Analysis
  Rules      Rules       Skill    Skill   Skill    Skill
   │          │            │        │       │        │
   │          │            │        │       │        │
   └──────────┴────────────┴────────┴───────┴────────┘
                          │
            ┌─────────────┴──────────────┐
            │                            │
        ┌───▼────┐                  ┌───▼───────┐
        │ PROJECT │                 │  KAPITEL  │
        │ FILES   │                 │  WRITING  │
        └─────────┘                 └───────────┘
```

---

## 🎓 Erweiterte Nutzung

### Custom Skills erstellen

**Beispiel: Review-Skill für Beta-Reader-Feedback**

1. Erstelle `Meta/Beta-Review-Skill.md`
2. Definiere Workflow wie in anderen Skills
3. Lade bei Bedarf:

```
@Meta/CORE-RULES.md @Meta/Beta-Review-Skill.md

Bereite Kapitel 1-5 für Beta-Reader vor
```

### Projekt-spezifische Rules

**Beispiel: Magic-System-Rules für komplexes Magiesystem**

```
/Meta
└── Project-Specific
    └── Magic-Rules.md
```

Lade bei magic-heavy Kapiteln zusätzlich.

---

## 🎉 System-Ziele erreicht!

✅ **Modular:** Einzelne Skills/Rules unabhängig
✅ **Effizient:** Nur laden was gebraucht wird
✅ **Wartbar:** Einzelne Module leicht zu updaten
✅ **Klar:** Jedes Modul hat klaren Zweck
✅ **Autonom:** Claude weiß was zu laden ist
✅ **Vollständig:** Alle Aspekte abgedeckt

---

## 📞 Schnellreferenz

**Ich will...** | **Lade...**
--- | ---
Projekt aufsetzen | `CORE-RULES + Structure-Rules`
Kapitel planen | `CORE-RULES + Planning-Skill`
Kapitel schreiben | `CORE-RULES + Writing-Skill + Style-Rules`
Kapitel überarbeiten | `CORE-RULES + Revision-Skill`
Konsistenz prüfen | `CORE-RULES + Consistency-Rules`
Struktur checken | `CORE-RULES + Analysis-Skill`
Stil anpassen | `Style-Rules` (editieren)

---

**Viel Erfolg mit deinem Romanprojekt! 📖✨**
