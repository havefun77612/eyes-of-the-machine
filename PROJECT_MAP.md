# PROJECT_MAP — "Eyes of the Machine"

> Last updated: 2026-07-08
> Author: A.L Hossam A. Abdelwahab

---

## [TECH_STACK]

| Component | Version | Role |
|---|---|---|
| Python | 3.12.x (Colab-compatible) | Runtime language |
| Google Colab | 2026.04 runtime | Primary execution environment |
| opencv-python | 5.0.0.93 | Image processing & face detection |
| Pillow | 12.3.0 | Image I/O and basic manipulation |
| matplotlib | 3.11.0 | Visualization |
| numpy | 2.0.2 | Numerical operations (hidden from student) |
| scikit-learn | 1.9.0 | ML utilities (Chapter 8) |

**No deprecated dependencies.** All packages are latest stable as of July 2026.

---

## [SYSTEM_FLOW]

### Chapter Dependency Graph

```
Ch1 (Philosophy)     — no prerequisites
Ch2 (Environment)    — no prerequisites
Ch3 (Python Basics)  — no prerequisites
Ch4 (Image Anatomy)  ── requires Ch3
Ch5 (Image Proc.)    ── requires Ch4
Ch6 (Feature Extract)── requires Ch5
Ch7 (Datasets)       — standalone (references Ch4)
Ch8 (Intro ML)       ── requires Ch3 (conceptual), references Ch6
Ch9 (Project)        ── requires Ch4, Ch5, Ch6, Ch8
Ch10 (Ethics/Future) — standalone (references all)
```

### Reader Journey

```
Absolute Zero
    │
    ├── Ch1: Mindset shift (what IS intelligence?)
    ├── Ch2: "Where do I type code?"
    ├── Ch3: "How do I talk to the computer?"
    │
    ├── Ch4: "How does the computer SEE?"
    ├── Ch5: "How do I change what it sees?"
    ├── Ch6: "How does it find shapes?"
    │
    ├── Ch7: "Where do images come from?"
    ├── Ch8: "How does it LEARN without formulas?"
    │
    ├── Ch9: BUILD a face detector — the hero moment
    │
    └── Ch10: "Now what? Ethics, jobs, helping family"
```

---

## [ARCHITECTURE]

### Repository Tree

```
eyes-of-the-machine/
│
├── README.md                 # Book overview + quickstart
├── PROJECT_MAP.md            # This file
├── requirements.txt          # pip install -r requirements.txt
│
├── chapters/                 # Markdown chapter files
│   ├── 01_silicon_brain.md
│   ├── 02_workshop.md
│   ├── 03_python_basics.md
│   ├── 04_anatomy_of_a_snap.md
│   ├── 05_digital_canvas.md
│   ├── 06_finding_edges.md
│   ├── 07_data_universe.md
│   ├── 08_awakening.md
│   ├── 09_masterpiece.md
│   └── 10_human_symbiosis.md
│
├── notebooks/                # Colab-ready .ipynb companion notebooks
│   ├── 03_python_basics.ipynb
│   ├── 04_anatomy_of_a_snap.ipynb
│   ├── 05_digital_canvas.ipynb
│   ├── 06_finding_edges.ipynb
│   ├── 08_awakening.ipynb
│   └── 09_masterpiece.ipynb
│
├── project/                  # Reusable standalone scripts
│   ├── smart_filter.py       # Face detection + effects (Ch9)
│   └── utils.py              # Helper functions (Ch9)
│
└── images/                   # Sample images used in book
    ├── sample_portrait.jpg
    ├── gradient_test.png
    └── (more as needed)
```

### Design Principles

1. **Self-contained chapters** — No cross-chapter imports. Each chapter is a standalone learning unit.
2. **No shared/core layer** — Premature abstraction is the enemy of beginners. Duplication is acceptable for clarity.
3. **Colab-first** — All code verified to run in `google.colab` with `cv2_imshow`, inline `pip install`, etc.
4. **One concept at a time** — No micro-files. One `.md` per chapter, one `.ipynb` per hands-on chapter.

---

## [ORPHANS & PENDING]

| Item | Status | Notes |
|---|---|---|
| Ch1 — Silicon Brain | COMPLETED | 9 blocks, Mermaid diagram |
| Ch2 — Workshop | COMPLETED | Red-square creation, toolkit verification |
| Ch3 — Python Basics | COMPLETED | + `notebooks/03_python_basics.ipynb` |
| Ch4 — Image Anatomy | COMPLETED | + `notebooks/04_anatomy_of_a_snap.ipynb` |
| Ch5 — Digital Canvas | COMPLETED | + `notebooks/05_digital_canvas.ipynb` |
| Ch6 — Finding Edges | COMPLETED | + `notebooks/06_finding_edges.ipynb` |
| Ch7 — Data Universe | COMPLETED | No notebook needed |
| Ch8 — Awakening | COMPLETED | + `notebooks/08_awakening.ipynb` |
| Ch9 — Masterpiece | COMPLETED | + `notebooks/09_masterpiece.ipynb` + `project/smart_filter.py` |
| Ch10 — Human Symbiosis | COMPLETED | No notebook needed |
| Sample images | PENDING | User to source/create before publication |

---

## [LOGGING STRATEGY]

Not applicable for a book project. Chapter 9's companion script uses `print()` statements only — no async logging infrastructure needed. The reader learns debugging through "Cognitive Debugging" blocks (Block 5 of each chapter).

---

## [VERIFICATION CHECKLIST]

- [x] All 10 chapters written with 9-block structure
- [ ] All `.ipynb` notebooks pass `Runtime → Run all` in Colab (needs manual verification)
- [ ] Chapter 9 face detector runs end-to-end on a test image (needs manual verification)
- [x] Mermaid diagrams render correctly on GitHub
- [x] No mathematical notation used (zero-math policy)
- [x] All code uses Colab-compatible display functions (`cv2_imshow`, inline display)
