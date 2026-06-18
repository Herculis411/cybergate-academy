# Capstone Engagement — Complete Lab Procedure

**Module 22 companion guide · CyberQuest Academy**

> ⚠️ **Authorisation gate.** This procedure runs end-to-end against **your own isolated lab only** — the host-only network and intentionally-vulnerable targets you built in Module 01 — under the written rules of engagement you authored in Module 00. Every action here is lawful *because* it stays inside that lab. Running any of it against a system you do not own or are not authorised to test is a criminal offence and is entirely outside the scope of this exercise.

This guide walks you through completing the capstone as a professional would run a real engagement: a clear lifecycle, evidence captured at every step, and a polished deliverable at the end. The capstone is assessed on **process and documentation**, not on "getting in" — so the discipline below is the point, not an afterthought.

---

## What you'll produce

A single, well-organised **engagement package**. By the end you will have built this folder tree and filled every part of it:

```
acme-bakery-engagement/
├── 00_authorisation/      RoE + scope (signed)
├── 01_recon/              footprint report
├── 02_enumeration/        parsed scan results
├── 03_findings/           findings log with CVEs + CVSS
├── 04_validation/         lab evidence (console logs, screenshots)
├── 05_hardening/          privilege-escalation review + fix
├── 06_detection/          blue-team alerts catching the activity
└── 07_report/             executive summary + technical report
```

Create it now so you have somewhere to drop evidence as you go:

```bash
mkdir -p acme-bakery-engagement/{00_authorisation,01_recon,02_enumeration,03_findings,04_validation,05_hardening,06_detection,07_report}
cd acme-bakery-engagement
```

---

## Pre-flight checklist

Confirm all of these before you start. A failed check here is the most common reason a capstone stalls later.

- [ ] **Module 00 passed** — you understand authorisation, scope, and the Computer Misuse Act.
- [ ] **Lab built and isolated (Module 01)** — Kali, Metasploitable, and the web targets are on the host-only network.
- [ ] **Isolation proven** — `ping 8.8.8.8` from Kali fails (no internet route); a ping to your lab target succeeds. Save this proof; it goes in `00_authorisation/`.
- [ ] **Web targets up** — `docker compose ps` in `labs/` shows DVWA, Juice Shop and WebGoat running.
- [ ] **A notes file open** — keep a running timestamped log as you work; it becomes your evidence trail.

> **Evidence habit:** for every command you run, capture the command, its output, and the time. The cleanest way is to record your terminal: `script -a engagement-log.txt` at the start of a session appends everything to a file you can reference later.

---

## Phase 0 — Pre-engagement (Authorisation)

*Draws on Module 00. Output → `00_authorisation/`.*

You are testing the lab, role-played as "Acme Bakery's test estate," under authorisation you grant yourself for the exercise.

1. Write (or reuse from M00) a **scope statement**: the in-scope lab hosts/subnet (`192.168.56.0/24` and the web targets on `127.0.0.1`), what is explicitly out of scope, and the testing window.
2. Write the **rules of engagement**: permitted activities (scanning, enumeration, validation of known issues, hardening review), forbidden activities (anything outside the lab, anything destructive beyond the agreed targets), and how evidence will be stored and later destroyed.
3. Save both as `00_authorisation/scope.md` and `00_authorisation/roe.md`, plus your isolation-proof screenshot.

> This phase has no "hacking" in it — and that is deliberate. A real engagement that skips authorisation is a crime, not a test. Treat this folder as the thing that makes everything after it legitimate.

---

## Phase 1 — Reconnaissance

*Draws on Module 09. Output → `01_recon/`.*

For the lab, reconnaissance is light (you already know the environment), so this phase is about **practising the discipline** of recording what you'd gather about an authorised target.

1. Document the known lab "estate": the target subnet, the web applications, and the services you expect.
2. For the web targets, note the technologies on display (server headers, visible frameworks) — passive observation only.
3. Produce a short `01_recon/footprint.md` summarising the attack surface you'll be assessing, and one line on what a defender should learn from it (e.g. reducing exposed services).

---

## Phase 2 — Scanning & Enumeration

*Draws on Module 10. Output → `02_enumeration/`.*

Now you map what's actually listening on the lab subnet.

1. Run a service/version scan of the **lab subnet only**:

   ```bash
   nmap -sV 192.168.56.0/24 -oN 02_enumeration/nmap-scan.txt
   ```

   The `-oN` flag saves the output straight into your evidence folder.

2. Parse the results into a tidy table — host, port, service, version — using the Python approach from Module 10, and save it as `02_enumeration/services.md`. This table is the input to the next phase.

3. Confirm each interesting service against **Spring Boot Admin / Eureka-style** registries if present, or simply note which hosts are live and what they run.

> **Document the "so what".** A scan output is data; your job is to turn it into a short list of services worth investigating, with a one-line reason for each.

---

## Phase 3 — Vulnerability Identification

*Draws on Module 16. Output → `03_findings/`.*

Take the service list and identify **known** issues — this is research and mapping, not exploitation.

1. For each notable service/version (for example, an outdated FTP or web service on Metasploitable), check whether a catalogued vulnerability affects that exact version using the CVE database.
2. Record each as a finding with: the service, the **CVE**, its **CVSS** severity, and a plain-English description of the risk.
3. Save as `03_findings/findings-log.md`. At this stage each finding is a *hypothesis* — "this lab host appears to run a version with a known issue" — to be confirmed in the next phase.

---

## Phase 4 — Validation

*Draws on Module 16. Output → `04_validation/`.*

Confirm, in the lab, that a finding is real — and capture the evidence. Keep this at the level the module taught: validating a **known** issue on your **own Metasploitable** host using documented, well-known framework modules, purely to prove presence. You are not writing exploits or weaponising anything; you are evidencing that the lab host is affected.

1. Using the documented framework module for the identified known issue, validate against the lab Metasploitable host **only**.
2. Capture the evidence: the console output and a screenshot showing the validation, saved into `04_validation/`.
3. For each validated finding, write a short **engagement note**: service → CVE → validation evidence → impact (scoped to the lab host).

> **Stop at proof.** Validation means "yes, this lab host is affected," with evidence. You do not need to go further — pivoting, data exfiltration, or persistence add nothing to the capstone and would push past its scope. Proof + evidence is the deliverable.

---

## Phase 5 — Privilege-Escalation Review (Hardening)

*Draws on Module 17. Output → `05_hardening/`.*

Switch to the defender's mindset: find one weakness that could enable escalation, then **fix it**.

1. On a lab VM you control, run an enumeration script and read its output for a common misconfiguration (e.g. a world-writable service file, a weak permission, a dangerous SUID binary).
2. Record the **finding** (what, where, why it's risky).
3. Apply the **remediation** and re-check to confirm it's closed.
4. Save the before/after as `05_hardening/privesc-review.md`. The win here is the *fix*, not the foothold.

---

## Phase 6 — Detection (Blue Team)

*Draws on Module 20. Output → `06_detection/`.*

Close the loop: show that the activity you performed earlier is **detectable**. This is what separates a thoughtful security professional from someone who only knows offence.

1. Replay the lab's IDS/log output from your Phase 2 scan through the Python detector you built in Module 20.
2. Confirm it raises an alert correlating to your scan, and capture that output.
3. Save as `06_detection/detection-evidence.md`, with a sentence on how a real SOC would have spotted you and how a defender could tune detection further.

> This is often the most impressive part of the package to a reviewer: you attacked, then you caught yourself. It demonstrates you understand both sides.

---

## Phase 7 — Reporting

*Draws on Module 21. Output → `07_report/`.*

The report is the deliverable that creates value. Write for two audiences.

1. **Executive summary** (one page, non-technical): the overall risk picture, the most important finding, and what to do about it — in plain English a manager could action.
2. **Technical report**: each finding with title, CVSS rating, affected lab host, description, evidence reference (pointing to your `04_validation/` and `05_hardening/` artefacts), impact, and concrete **remediation**.
3. Save as `07_report/executive-summary.md` and `07_report/technical-report.md`.

A solid finding entry looks like this:

```text
[Finding F-01] Outdated service with known vulnerability
Severity     : High (CVSS 9.x)
Affected     : lab host 192.168.56.102 (service/version)
Description  : The running version contains a catalogued vulnerability (CVE-XXXX-XXXX).
Evidence     : 02_enumeration/services.md; 04_validation/ (console log + screenshot)
Impact       : Compromise of the affected lab host.
Remediation  : Upgrade/replace the service; restrict exposure; monitor (see 06_detection/).
```

---

## Final — Assemble and self-assess

1. Confirm every folder `00_`–`07_` contains its artefact:

   ```bash
   find . -type f | sort
   ```

2. Run yourself through this **self-assessment checklist** — it mirrors how a professional package is judged:

   - [ ] Authorisation and scope are written **first** and the lab isolation is proven.
   - [ ] Every offensive step is traceable to evidence (command, output, timestamp).
   - [ ] Findings map services → CVE → CVSS → validated evidence.
   - [ ] At least one weakness is **remediated**, with before/after proof.
   - [ ] The activity is shown being **detected** (blue-team closure).
   - [ ] The report has both an executive summary and a technical section, each with clear remediation.
   - [ ] Nothing in the package references any system outside the lab.

3. Zip the package as your portfolio piece:

   ```bash
   cd ..
   zip -r acme-bakery-engagement.zip acme-bakery-engagement/
   ```

---

## 🏅 Completion

When the package is complete and passes the self-assessment, you've demonstrated the full lifecycle: authorise → recon → enumerate → identify → validate → harden → detect → report — entirely within an isolated lab, documented to a professional standard. That is the **CyberQuest Lead** capstone.

### Where these skills belong next (legal outlets)

- **Bug bounty platforms** (HackerOne, Bugcrowd, Intigriti) — get paid to find issues, with permission.
- **CTF competitions** — keep practising, competitively and legally.
- **Certifications** — eJPT, PNPT, CompTIA PenTest+ map directly to what you just did.
- **Your own lab** — the safest place to keep sharpening.

> The whole course in one line: same skills, different ethics — and the ethics, the evidence, and the report are what make you a professional.
