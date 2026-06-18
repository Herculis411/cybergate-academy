# Module 09 · Reconnaissance & OSINT Automation

**Tier:** Networking & Automation Core · **Level:** Intermediate
**Prerequisites:** M08 · **Estimated time:** 90 minutes

---

## Objectives

- Understand **passive vs active** reconnaissance.
- Gather publicly available information **legally**.
- Automate a footprint report for an **authorised** target.

!!! danger "The ethics checkpoint"
    Recon feels harmless because you're "just looking", but active recon against
    a target you don't own is unauthorised access. In this module you target
    only a domain **you own** or a provided sandbox domain. Passive OSINT on
    public data is fine; pointing tools at someone else's infrastructure is not.

---

## 1. Passive vs active

- **Passive:** reading public sources (search engines, DNS records, public
  social profiles, company websites). No packets to the target's private
  systems.
- **Active:** directly probing the target (scanning, enumeration). Requires
  authorisation — covered in M10.

## 2. What recon collects

Subdomains, public email formats, technologies in use, exposed documents. This
is the attacker's first phase (MITRE ATT&CK *Reconnaissance*), and knowing it
helps defenders reduce their own footprint.

## 3. Tools

`whois`, `dig`/`nslookup`, theHarvester, and simple Python using public APIs.
Keep it passive unless you own the target.

---

## Hands-on lab — footprint an authorised target

!!! example "Lab task"
    For a domain you own (or the provided `sandbox.lab` records), collect:
    DNS records, any subdomains, and the web technologies in use. Compile a
    short footprint report.

### Expected output artefact

```text
$ python3 footprint.py sandbox.lab
[Footprint report: sandbox.lab]
A records      : 192.0.2.10
MX records     : mail.sandbox.lab
Subdomains     : www, dev, mail
Tech detected  : nginx, jQuery
Public emails  : info@sandbox.lab
Notes          : 'dev' subdomain exposed — recommend access restriction
```

The "Notes" line is the value you add as a tester: turning data into advice.

---

## ✅ Checkpoint

1. Passive vs active — which needs authorisation to the target? **(Active.)**
2. Which ATT&CK phase is this? **(Reconnaissance.)**
3. Whose domains may you recon here? **(Your own / provided sandbox.)**

## 🏅 Badge unlocked: **Scout** — Module 10 is now open.

[Continue to Module 10 · Scanning & Enumeration →](10-scanning.md){ .md-button .md-button--primary }
