# CyberGate Academy

> Free, beginner-to-advanced, **ethics-first** training in cybersecurity and ethical-hacking automation.

[![Deploy](https://github.com/Herculis411/cyberquest-academy/actions/workflows/deploy.yml/badge.svg)](https://github.com/Herculis411/cyberquest-academy/actions)
&nbsp;|&nbsp; **Live site:** https://herculis411.github.io/cyberquest-academy/

CyberQuest Academy is a structured, 24-module learning platform that teaches modern cybersecurity and security automation the right way: **authorisation and ethics first, offence only in service of defence, everything in an isolated lab.** It is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and deploys automatically to GitHub Pages.

## Who it's for

Beginners who want a safe, legal on-ramp into cybersecurity, and self-learners who want a complete path from fundamentals through to a professional capstone engagement — without ever touching a system they don't own.

## How it's structured

The curriculum runs across five tiers, gated by a mandatory ethics-and-law module:

- **Module 00 — Ethics, Law & Authorisation** (hard gate; the Computer Misuse Act, scope, and rules of engagement)
- **Tier 1 — Foundations** (safe lab setup, Linux, networking, scripting)
- **Tier 2 — Defensive Security** (logging, detection, blue-team fundamentals)
- **Tier 3 — Offensive Security** (lab-only, defensively framed, paired with detection)
- **Tier 4 — Professional & Capstone** (reporting, and a full authorised engagement simulation)

Every practical exercise runs against intentionally vulnerable targets in an **isolated, host-only lab** — never against real or third-party systems.

## Run it locally

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Then open http://127.0.0.1:8000.

## Project layout

```
cyberquest-academy/
├── mkdocs.yml                 # site config + navigation
├── requirements.txt           # MkDocs Material and plugins
├── docs/                      # all module pages (00 … 22)
├── labs/                      # lab environment
│   ├── docker-compose.yml     # vulnerable web targets (lab-only, 127.0.0.1-bound)
│   └── data/                  # sample lab data + the detector
└── .github/workflows/         # GitHub Actions deploy pipeline
```

## Ethos

> Same skills, different ethics. The ethics, the evidence, and the report are what make you a professional.

All offensive content is capped to lab use, framed defensively, and paired with detection. Where skills can be applied for real, the course points only to **legal** outlets: bug bounty programmes, CTFs, certifications, and your own lab.

## Author

Built by **Stephen Odunze** — cybersecurity & DevSecOps practitioner.
Portfolio: https://stephenodunze.online &nbsp;·&nbsp; GitHub: https://github.com/Herculis411

## Licence

Educational use. See the repository for details.
