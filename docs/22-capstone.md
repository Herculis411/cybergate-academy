# Module 22 · Capstone — Authorised Engagement Simulation

**Tier:** Professional Skills & Capstone · **Level:** Advanced
**Prerequisites:** M00–M21 · **Estimated time:** 4–6 hours

!!! danger "Everything, in the lab, under your own RoE"
    The capstone runs the full lifecycle against your **isolated lab** only,
    under the **rules of engagement you wrote in Module 00**. It assembles
    everything you've learned into one documented engagement — and it stays
    entirely lawful because it never leaves the lab.

---

## Objectives

- Run a complete engagement: recon → scan → identify → validate → post-ex
  concept → detect → report.
- Work to your own scope and RoE.
- Produce a professional engagement package.

---

## The engagement

You are testing the lab environment ("Acme Bakery's test estate") under written
authorisation. Follow the PTES lifecycle:

1. **Pre-engagement (M00):** confirm scope and RoE.
2. **Recon (M09):** footprint the authorised target.
3. **Scanning (M10):** enumerate services on the lab subnet.
4. **Identification (M16):** map findings to CVEs.
5. **Validation (M16):** confirm on lab hosts, with evidence.
6. **Privilege-escalation review (M17):** find and note one misconfiguration.
7. **Detection (M20):** show how your own activity is detected.
8. **Reporting (M21):** write the full report.

---

## Deliverable — engagement package

!!! example "Capstone task"
    Submit a single package containing every artefact below. This is your
    portfolio piece — proof you can do the whole job, ethically.

### Expected output artefact

```text
ENGAGEMENT PACKAGE — Acme Bakery test estate (lab)
├── 00_authorisation/      RoE + scope (signed)
├── 01_recon/              footprint report
├── 02_enumeration/        parsed scan table
├── 03_findings/           findings log w/ CVEs + CVSS
├── 04_validation/         lab evidence (console logs, screenshots)
├── 05_hardening/          privilege-escalation review + fix
├── 06_detection/          blue-team alerts catching the activity
└── 07_report/             executive summary + technical report
Status: COMPLETE — all activity lab-only, within scope ✅
```

---

## 🏅 Final badge: **CyberQuest Lead**

Completing the capstone means you can take a target from authorisation to
final report, attack **and** defend, and document it like a professional.

## Where to go next (legal outlets for your skills)

- **Bug bounty platforms** (HackerOne, Bugcrowd, Intigriti) — get paid, with permission.
- **CTF competitions** — keep sharpening, competitively and legally.
- **Certifications** — eJPT, PNPT, CompTIA PenTest+ map directly to what you've done here.
- **Keep building your lab** — the safest playground there is.

!!! quote "The whole course in one line"
    Same skills, different ethics — and the ethics are what make you a
    professional. Welcome to the field.
