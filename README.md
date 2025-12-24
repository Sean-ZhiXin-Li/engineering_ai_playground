# engineering_ai_playground

A **personal engineering training ground** for building solid, long‑term capability in:

* Python engineering (from scratch, not templates)
* Linux-based development workflow (WSL)
* Git discipline and reproducibility
* Debugging as a first-class skill
* Gradual transition toward AI / ML engineering

This repository is **not a product** and **not a research project**.
It is intentionally small, controlled, and process-oriented.

---

## Why This Repository Exists

This repo is designed to answer one question clearly:

> **Can I independently build, debug, and iterate on a Python + AI engineering system in a Linux environment?**

The focus is not on advanced models or performance, but on:

* Writing code from a blank file
* Understanding errors instead of avoiding them
* Forming engineering habits that scale to lab work and research projects

This repository also **supports future lab readiness** by strengthening reproducible engineering and debugging skills that are essential for collaborative research environments.

This repository is meant to stay simple so that **thinking, debugging, and structure** are always visible.

---

## Training Roadmap (High-Level)

The work in this repository follows a fixed, time-bounded plan:

### Phase A — Foundations (12/24 – 1/12)

* Linux / WSL workflow
* Python virtual environments (venv)
* Git fundamentals with small, clean commits
* Writing minimal runnable scripts
* Real debugging (logic, None, NaN, shape issues)

**Deliverables**:

* ≥10 commits
* Minimal config → run → output pipeline
* `metrics.json` output
* `notes/debug_log.md`

---

### Phase B — Engineering Python (1/13 – 2/9)

* Clear project structure
* Config-driven execution (no hard-coded parameters)
* Reproducible experiments
* Metrics and simple plots

**Constraints**:

* Models limited to linear / logistic / very small MLP
* Engineering clarity > model complexity

---

### Phase C — Python AI Engineering (2/10 – 3/23)

* PyTorch basics
* `train` / `eval` separation
* Seed control
* At least one ablation study
* Explicit experiment tracking

**Theory is introduced only through engineering phenomena**, not formulas.

---

### Phase D — Maintenance & Low Frequency (3/24 – 5月)

* Reduced cadence due to AP exams
* Refactoring, documentation, and bug fixes only
* No new features or models

---

## What This Repo Is (and Is Not)

### This repo **is**:

* A transparent engineering learning record
* A place where early-stage code and mistakes are preserved
* A controlled environment to build confidence with Python + Linux

### This repo **is not**:

* A research paper
* A performance benchmark
* A large framework or system
* A place for advanced or fancy models

Those belong in other repositories.

---

## How to Run (Current Stage)

At the current stage, the repository contains minimal runnable scripts.

Example:

```bash
python test.py
```

Follow the prompt to enter a numeric value.

---

## Engineering Principles

This repository values:

* Clarity over cleverness
* Correctness over speed
* Reproducibility over convenience
* Debugging over avoidance

Mistakes are expected and documented as part of the training process.

---

## Status

This repository evolves incrementally.
Each phase has explicit scope limits to prevent uncontrolled growth.

Progress is measured by **engineering confidence and reproducibility**, not by feature count.

---

## License

Personal educational use.
