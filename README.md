# 📚 CST1510 — Python Course Repository

> A first-year Python programming module: **Week 1 (basics)** → **Week 2 (decisions & loops)**
>
> 📍 *Course code:* CST1510 · 🌿 Branch: `main` · 📨 Remote: `github.com/MtawqeeriQ/CST1510.git`

---

## 🗂️ Repository Structure

```
📦 CST1510
├── 📖 README.md                       ← this file
├── 📂 Week 01 — Your First Program
│   ├── 📄 01 - Your First Program.code-workspace  (VS Code workspace config)
│   ├── 📄 W01T01–T04_walkthrough.ipynb   (topic walkthroughs)
│   ├── 📂 examples/                       (runnable reference scripts)
│   ├── 📄 DEMO/record_check.py           (week 1 demo: input → calc → print)
│   └── 📂 LAB/                           (warm-up, drills, mini-project, git)
├── 📂 Week 02 — Decisions and Loops
│   ├── 📄 README.md                      (this week's layout)
│   ├── 📄 W02T01–T04_walkthrough.ipynb   (topic walkthroughs)
│   ├── 📂 examples/                       (runnable reference scripts)
│   ├── 📄 DEMO/record_check.py           (week 2 demo: decisions + loop)
│   ├── 📄 EXTRA_PROJECTS.md              (optional projects)
│   └── 📂 LAB/                           (warm-up, drills, mini-project, git)
└── 📂 Custom Office Templates           (module templates/files)
```

---

## 🎯 Learning Path: The "Boxes" Model

The course is built around a **four-box model** 👇 that grows week by week:

| Box | Week | What it covers |
|-----|------|----------------|
| 🟦 **INPUT** | Week 1 | Getting data from the user with `input()` |
| 🟦 **OUTPUT** | Week 1 | Showing results with `print()`, f-strings, formatting |
| 🟨 **PROCESS** | Week 2 | Making decisions (`if` / `elif` / `else`) and repeating (`while` / `for`) |
| 🟩 **STORE** | Week 4 | Reading files, lists, arrays (out of scope this week) |

> 💡 The same problem — a **Record Check** — is solved again and again, each week with a bigger toolkit ✨

---

## 📦 Course Files & Folders

### 📁 Week 01 — Your First Program
| File/Folder | What it contains |
|-------------|------------------|
| `W01T01_walkthrough.ipynb` | 🖨️ Topic 1: `print()`, strings, quotes, line breaks, comments |
| `W01T02_walkthrough.ipynb` | 🏷️ Topic 2: variables, types (`str`/`int`/`float`), naming |
| `W01T03_walkthrough.ipynb` | ➕ Topic 3: arithmetic (`+ - * / // % **`), modulo, order of operations |
| `W01T04_walkthrough.ipynb` | 🎯 Topic 4: `input()`, casting, f-strings, formatting & alignment |
| `examples/*.py` | 🧩 8 runnable scripts (~40 lines each) — the "Go deeper" references |
| `DEMO/record_check.py` | 🎬 Week 1 demo program |
| `LAB/W01_Lab.ipynb` | 🧪 Week 1 lab: warm-up, 7 drills (Threshold / Typical / Excellent), mini-project, journal |
| `LAB/template.py` | 📋 Mini-project scaffold with numbered sections |
| `LAB/warmup/*.py` | 🔧 3 deliberately broken programs (NameError / TypeError / ValueError) |

### 📁 Week 02 — Decisions and Loops
| File/Folder | What it contains |
|-------------|------------------|
| `W02T01_walkthrough.ipynb` | 🔍 Topic 1: 6 comparison operators, `==` vs `=`, booleans, `and`/`or`/`not` |
| `W02T02_walkthrough.ipynb` | 👀 Topic 2: `if` / `else` / `elif`, indentation-syntax |
| `W02T03_walkthrough.ipynb` | 🔁 Topic 3: `while` loops, `break`, `continue`, infinite loops |
| `W02T04_walkthrough.ipynb` | 🔢 Topic 4: `for` + `range()`, `enumerate()`, `for` vs `while` |
| `examples/*.py` | 🧩 6 runnable scripts — deeper reference examples |
| `DEMO/record_check.py` | 🎬 Week 2 demo program (decisions + loop) |
| `EXTRA_PROJECTS.md` | 🌟 Optional projects: Python Pizza, Treasure Island, Higher/Lower, Number Guessing |
| `LAB/W02_Lab.ipynb` | 🧪 Week 2 lab: warm-up, drills, mini-project, cheat sheet, git |
| `LAB/template.py` | 📋 Mini-project scaffold with numbered sections |
| `LAB/warmup/*.py` | 🔧 3 deliberately broken programs (IndentationError / SyntaxError / TypeError) |

---

## 📚 Core Python Topics (Week 1)

### 🖨️ Topic 1 — Your First Program
- `print()` — one value, several values (commas = spaces), `sep=`, `end=`
- Strings — single/double quotes, escaping, triple quotes, repetition
- Blank lines, separators: `"=" * 30`
- Comments: `#` (read like instructions, not part of the program)

### 🏷️ Topic 2 — Variables & Types
- `name = value` — "gets", not "equals"
- Three types: `str` (text), `int` (whole number), `float` (decimal)
- The classic trap: `"20"` (text) vs `20` (number) — same print, different type
- Naming rules: lowercase, underscores, no spaces, no Python keywords
- Reassignment: a variable can hold a new value; the old one is gone

### ➕ Topic 3 — Numbers & Arithmetic
All seven operators, plus:

| Operator | Meaning |
|----------|---------|
| `+` | add |
| `-` | subtract |
| `*` | multiply |
| `/` | divide — **always returns a float** (e.g. `5.0`) |
| `//` | integer division — whole part only |
| `%` | modulo — remainder |
| `**` | power |

✨ Chaining splits (big unit first, then work on the remainder):  
```python
hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60
```
📐 Shorthand: `count += 1` is the same as `count = count + 1`

### 🎯 Topic 4 — Input, Casting & f-strings
- `input()` **always** gives you text, even when the user types a number
- Cast in the same line: `value = float(input("Value: "))`
- Always use `float()` unless you're certain the number is whole
- f-strings: `f"Value: {value}"` — put values inside text
- Formatting: `{x:.2f}` (2 decimals), `{x:>10}` (right-aligned), `{x:>10.2f}` (both)

---

## 📚 Core Python Topics (Week 2)

### 🔍 Topic 1 — Comparisons & Boolean Logic
Six operators: `==` `!=` `<` `>` `<=` `>=` — each returns `True` or `False` (`bool`)
- `=` **stores** · `==` **asks**
- Combine with `and` (both), `or` (at least one), `not` (flip)
- Always **bracket each comparison** when combining

### 👀 Topic 2 — if / elif / else
- `if` — block runs only when `True`
- `else` — the alternative, exactly one branch runs
- `elif` — multiple branches, checked top-to-bottom, first `True` wins
- 🔑 **Indentation is syntax**, not style — no `{}` in Python

### 🔁 Topic 3 — while Loops
- `while condition:` — repeat while condition is `True`
- The condition **must change** inside the loop or it runs forever 🔄
- `while True:` + `break` — loop until something inside decides to stop
- `continue` — skip the rest of this pass, go back to the condition

### 🔢 Topic 4 — for Loops & range()
- `for i in range(n):` — repeat exactly `n` times (0, 1, ..., n-1)
- `range(start, stop)` — `stop` is **never included**
- `range(start, stop, step)` — count by steps, or count down with a negative step
- `enumerate()` — get the index and value together: `for i, letter in enumerate("cat"):`
- 🎯 **Choose the right tool:** `for` when you know the count · `while` when you don't

---

## 🧪 Lab Structure (3 hours)

| Time | Part |
|------|------|
| 0:00 | 🔧 Warm-up — fix 3 broken files in `LAB/warmup/` |
| 0:15 | 📋 Drills — short tasks on every topic (Threshold / Typical / Excellent tiers) |
| 0:30 | 🍃 Break |
| 0:45 | 🎯 Mini-project — `LAB/template.py` (3 lanes × 3 tiers) |
| 1:55 | 📸 Wrap-up — cheat sheet notes, photo, git commit + push |

### 🎯 Mini-project tiers
| Tier | What you do |
|------|-------------|
| **Threshold** (pass) | Ask 3 values, print a bordered report |
| **Typical** (mid) | + calculate difference & percentage, 2-decimal, right-aligned |
| **Excellent** (high) | + difference always shows sign, one extra useful line, loop with `quit` + count |

---

## 🌍 "Same Idea, Three Fields" — Domain Examples

Every concept is shown through **AI/Data Science**, **Cyber Security**, and **IT**:

| Concept | AI / Data Science | Cyber Security | IT |
|---------|-------------------|----------------|-----|
| `print()` | `Rows loaded: 1200` | `[ALERT] failed login` | `Backup complete - 4/4 servers` |
| Variables | `reading`, `units` | `source_ip`, `port` | `hostname`, `disk_used` |
| Percentage | `% of rows missing` | `% of failed logins` | `% of disk used` |
| Decision | `if missing_pct > 5` | `if failed_logins >= 3` | `if disk_used_pct >= 90` |

---

## 📊 Assessment (Week 1–2)

| Tier | Standard | Indicative |
|------|----------|------------|
| 🟢 **Threshold** | drills D1–D3 + Threshold mini-project | pass |
| 🟡 **Typical** | + drills D4–D6 + Typical mini-project | mid |
| 🟠 **Excellent** | + drill D7 + Excellent mini-project | high |

*No marks this week — everything is kept, accumulating into CW1.*

---

## 🔍 Common Errors (What to Read First)

> Always read the **last line** of the error, then the line number, then fix one thing

| Error | Usually means | First thing to check |
|-------|---------------|----------------------|
| `NameError` | Used a name Python hasn't seen | Spelling / capital letter in the wrong place |
| `TypeError` | Text + number mixed | Forgot `int()` or `float()`? |
| `ValueError` | Right type, impossible value | `int("23.7")` or `float("abc")` |
| `SyntaxError` | Python can't read the line | Quotes/brackets — often a problem **on the line above** |
| `IndentationError` | Block not indented | Indent the line under `if` / `while` / `for` |

---

## 🛠️ Git Workflow (per week)

```bash
git add .
git commit -m "Week X lab and mini-project"
git push
```

Then check GitHub in the browser. `pwd` tells you where you are if files are missing.

---

## 📖 How to Use This Repository

1. 📘 **Read the walkthrough** (`W0xTx_walkthrough.ipynb`) — it's both teaching and revision
2. 📜 **Run the examples** (`examples/*.py`) — they're the "Go deeper" references
3. 🧪 **Do the drills** in `LAB/W0x_Lab.ipynb`
4. 🎯 **Build the mini-project** in `LAB/template.py`
5. 📸 **Photograph the cheat sheet** and paste it into the journal cell
6. 📤 **Commit & push** to GitHub

---
