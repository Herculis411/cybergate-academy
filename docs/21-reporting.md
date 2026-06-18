# Module 21 · Reporting & Professional Communication

**Tier:** Professional Skills & Capstone · **Level:** Advanced
**Prerequisites:** M20 · **Estimated time:** 90 minutes

---

## Objectives

- Turn findings into a clear, actionable, **ethical** report.
- Score risk with **CVSS** and write for two audiences.
- Produce the deliverable that actually creates value.

---

## 1. Why the report is the job

Clients don't pay for scans; they pay for a report that tells them what's wrong,
how bad it is, and what to do. A brilliant finding nobody can act on is worthless.

## 2. Structure of a finding

Each finding needs: a title, a risk rating (CVSS), a plain-English description,
evidence, impact, and a concrete remediation. Keep evidence factual and minimal.

## 3. Two audiences

- **Executive summary:** non-technical, risk-focused, one page.
- **Technical detail:** reproducible steps, evidence, remediation for engineers.

---

## Hands-on lab — write a full finding

!!! example "Lab task"
    Take one finding from any earlier lab module and write it up properly:
    summary, CVSS rating, evidence, and remediation.

### Expected output artefact

```text
[Finding F-01] Outdated FTP service with known backdoor
Severity     : High (CVSS 9.8)
Affected     : lab host 192.168.56.102, port 21 (vsftpd 2.3.4)
Description  : The running version contains a catalogued backdoor (CVE-2011-2523)
               allowing remote access.
Evidence     : M10 scan output; M16 validation log (lab-only)
Impact       : Full compromise of the host.
Remediation  : Upgrade/replace the service; restrict network exposure; monitor.
Exec summary : One internet-facing service is critically outdated and must be
               patched this week; risk of full host takeover.
```

---

## ✅ Checkpoint

1. What do clients actually pay for? **(An actionable report.)**
2. What does every finding need? **(Rating, evidence, remediation.)**
3. Who reads the executive summary? **(Non-technical decision-makers.)**

## 🏅 Badge unlocked: **Communicator** — the Capstone is now open.

[Continue to Module 22 · Capstone Engagement →](22-capstone.md){ .md-button .md-button--primary }
