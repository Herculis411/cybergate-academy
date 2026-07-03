# CyberGate Academy

> Free, beginner-to-advanced, **ethics-first** training in cybersecurity and penetration testing.

[![Deploy](https://github.com/Herculis411/cybergate-academy/actions/workflows/deploy.yml/badge.svg)](https://github.com/Herculis411/cybergate-academy/actions)
&nbsp;|&nbsp; **Live site:** https://herculis411.github.io/cybergate-academy/

CyberGate Academy is a structured learning platform that teaches modern cybersecurity and penetration testing the right way: **authorisation and ethics first, offence only in service of defence, everything in an isolated lab.** It is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and deploys automatically to GitHub Pages.

## Who it's for

Beginners who want a safe, legal on-ramp into cybersecurity, and self-learners who want a complete path from fundamentals through to a professional capstone engagement — without ever touching a system they don't own.

## Courses

| Course | Title | Content |
|--------|-------|---------|
| [Module 00](https://herculis411.github.io/cybergate-academy/00-ethics-law/) | Ethics, Law & Authorisation | Mandatory gate — CMA 1990, scope, RoE, responsible disclosure |
| [Course 01](https://herculis411.github.io/cybergate-academy/01-foundations/) | Penetration Testing Foundations | 22 modules across 5 tiers — beginner to professional |
| [Course 02](https://herculis411.github.io/cybergate-academy/02-web-vapt/) | Web Application VAPT | 10 hands-on OWASP Top 10 labs — Juice Shop & DVWA |

## How it's structured

The curriculum runs across five tiers, gated by a mandatory ethics-and-law module:

- **Module 00 — Ethics, Law & Authorisation** — hard gate; Computer Misuse Act 1990, scope, and rules of engagement. Must pass the checkpoint quiz to unlock all courses.
- **Tier 0 — Foundations** — safe lab setup, Linux & CLI, Git, Python I, II & Files
- **Tier 1 — Networking & Automation Core** — TCP/IP, Python networking, Recon & OSINT, Scanning, Scapy
- **Tier 2 — Offensive Security** — Cryptography, Web App Security I & II, Authentication & Passwords, Exploitation
- **Tier 3 — Advanced & Specialisation** — Post-Exploitation, Wireless (optional), Malware Analysis (optional), Blue-Team Automation
- **Tier 4 — Professional & Capstone** — Reporting, Full authorised engagement simulation

Every practical exercise runs against intentionally vulnerable targets in an **isolated, host-only Docker lab** — never against real or third-party systems.

## Run it locally

```bash
git clone https://github.com/Herculis411/cybergate-academy.git
cd cybergate-academy
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Then open http://127.0.0.1:8000.

## Project layout

```
cybergate-academy/
├── mkdocs.yml                 # site config + navigation
├── requirements.txt           # MkDocs Material and plugins
├── docs/
│   ├── index.html             # dark-themed homepage
│   ├── 00-ethics-law/         # Ethics Gate (standalone HTML)
│   │   └── index.html
│   ├── 01-foundations/        # Course 01 hub (standalone HTML)
│   │   └── index.html
│   ├── 02-web-vapt/           # Course 02 VAPT (standalone HTML)
│   │   └── index.html
│   ├── 01-safe-lab.md … 22-capstone-procedure.md   # 22 module pages
│   ├── assets/                # logo and static assets
│   └── stylesheets/           # extra.css brand overrides
├── labs/
│   ├── docker-compose.yml     # vulnerable web targets (lab-only, 127.0.0.1-bound)
│   └── data/                  # sample lab data + detector scripts
└── .github/workflows/         # GitHub Actions deploy pipeline
```

## Ethos

> Same skills, different ethics. The ethics, the evidence, and the report are what make you a professional.

All offensive content is capped to lab use, framed defensively, and paired with detection. Where skills can be applied for real, the course points only to **legal** outlets: bug bounty programmes, CTFs, certifications, and your own lab.

## Author

Built by **Stephen Odunze** — cybersecurity & DevSecOps practitioner, CISA, ISO 27001 Lead Auditor, CompTIA Security+.  
Portfolio: https://stephenodunze.online &nbsp;·&nbsp; GitHub: https://github.com/Herculis411  
Company: [GeeksDane Consultancy Ltd](https://stephenodunze.online)

## Licence

Educational use. See the repository for details.
