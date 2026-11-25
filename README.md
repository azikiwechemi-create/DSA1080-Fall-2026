# DSA1080 — Fall 2026 Coursework & Projects

**Author:** Chemi Azikiwe (`azikiwechemi-create`)  
**Course:** DSA1080 (Fall 2026)

## Overview

This repository contains practical assignments, Jupyter notebooks, Python scripts, and an interactive web simulation completed for **DSA1080**. The work spans foundational Python programming, data structures, algorithmic problem solving, and network-based epidemiological modeling.

---

## Repository Contents

### 1. Interactive Web Simulation
* **`Simulation.html` — SIR Disease Spread Contact Network Simulator**
  * A standalone, browser-based interactive simulation modeling infectious disease spread across a weighted contact graph $G = (V, E)$ using the **Susceptible–Infected–Recovered–Vaccinated (SIR-V)** compartmental model.
  * **Key Features:**
    * **Two Network Presets:** A 6-student worked example (`A–F`) with explicit edge weights and interaction scores, and an 18-student multi-classroom school network featuring cluster hubs and inter-class bridges.
    * **Interactive Controls:** Step through the outbreak day-by-day (`Step +1 Day`), run continuously (`Auto-Run`), adjust the **Transmission Multiplier** (`0.2x–2.0x`) and **Recovery Rate ($\gamma$)** (`0.05–0.80`), or apply a targeted intervention (`Vaccinate Highest-Degree Hub`).
    * **Direct Node Manipulation & Inspection:** Click any node to cycle its state (`S → V → I → R`) or hover to inspect its degree ($k$), weighted degree ($s$), and daily infection probability.
    * **Real-Time Analytics:** Live SVG epidemic curve plotting $S$, $I$, and $R$ population counts alongside a chronological simulation event log.

---

### 2. Python Scripts & Jupyter Notebooks
* **`Campus Wallet assingment.py` — Pesapesa Campus Budget Calculator**
  * A CLI personal finance tracker built in Python for managing daily campus expenses in **KES** (meals, snacks, and transport), projecting 5-day campus budgets, handling unexpected expenses, and providing color-coded balance feedback.
* **Python Functions & Applied Calculators (`.ipynb`)**
  * Modular functions with boundary and edge-case testing for:
    * Exam grade classification (`A`–`F` scale)
    * Shopping bill totals (`KES`)
    * Even/odd integer parity checks
    * Simple interest calculations
    * Weighted student performance reports (40% CAT + 60% Final Exam)
* **Data Structures: Lists, Tuples, Sets & Dictionaries (`.ipynb`)**
  * **List Indexing & Slicing Practical:** Multi-week step-count analysis (14-day dataset) demonstrating positive/negative indexing, step slicing, list reversal, custom index extraction, and weekly average comparisons.
  * **Collections Exploration:** Creation, slicing, mutation, and set/tuple operations across core Python data types.
  * **Football Players Database (Group 2 Assignment):** Comprehensive dictionary manipulation including CRUD operations, shallow copying (`.copy()`), dictionary views (`.keys()`, `.values()`, `.items()`), merging records (`.update()`), and querying nested player dictionaries.
* **Control Flow & Loops (`.ipynb`)**
  * Implementations of conditional branching (`if`/`elif`/`else`, shorthand ternaries, boolean operators), `for` and `while` loops, `break`/`continue` flow control, nested loops, factorial computation, and natural number summation.

---

## How to Run

### Web Simulation
No build tools or dependencies are required:
1. Download or clone the repository.
2. Open `Simulation.html` directly in any modern web browser (Chrome, Firefox, Edge, Safari).

### Python Scripts & Notebooks
* **Prerequisites:** Python 3.x and Jupyter Notebook / JupyterLab (or VS Code with the Jupyter extension).
* **Run the CLI script:**
  ```bash
  python "Campus Wallet assingment.py"
