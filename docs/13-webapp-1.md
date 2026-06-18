# Module 13 · Web Application Security I — OWASP Foundations

**Tier:** Offensive Security · **Level:** Intermediate
**Prerequisites:** M12 · **Estimated time:** 100 minutes

---

## Objectives

- Know the **OWASP Top 10 (2021)** and how common web flaws arise.
- Identify an injection and an access-control flaw in **DVWA** (lab).
- Map every finding to its OWASP category.

!!! danger "DVWA / Juice Shop only"
    All testing here targets the deliberately-vulnerable lab apps you ran in
    Module 01. Never test a web app you don't own or aren't authorised to test.

---

## 1. The OWASP Top 10 (2021), briefly

A01 Broken Access Control · A02 Cryptographic Failures · A03 Injection ·
A04 Insecure Design · A05 Security Misconfiguration · A06 Vulnerable Components ·
A07 Identification & Authentication Failures · A08 Software & Data Integrity ·
A09 Logging & Monitoring Failures · A10 Server-Side Request Forgery.

## 2. How flaws arise

Most come from trusting user input or skipping a check. Injection happens when
input is mixed into a command/query. Broken access control happens when the app
doesn't verify you're allowed to do a thing.

## 3. Working in DVWA

DVWA has a security slider (low/medium/high). Start at **low** to see the raw
behaviour, then raise it to see how defences change the outcome — that contrast
is the lesson.

---

## Hands-on lab — find and classify two flaws

!!! example "Lab task"
    In DVWA (low security), observe one **injection** behaviour and one
    **access-control** behaviour. Record each in a findings log mapped to OWASP.

### Expected output artefact

```text
[Findings log — DVWA lab, security=low]
F-01  Input reflected/processed unsafely in 'search' field
      -> OWASP A03 Injection
      Evidence: lab screenshot 01
F-02  Direct page reached without authorisation check
      -> OWASP A01 Broken Access Control
      Evidence: lab screenshot 02
Recommendation: validate/parameterise input; enforce server-side authz
```

The recommendations matter as much as the findings — defenders read those.

---

## ✅ Checkpoint

1. Which OWASP category is injection? **(A03.)**
2. Why start DVWA at low security? **(To see raw behaviour before defences.)**
3. What two things must a finding include? **(Evidence and a recommendation.)**

## 🏅 Badge unlocked: **Web Tester** — Module 14 is now open.

[Continue to Module 14 · Web App Security II →](14-webapp-2.md){ .md-button .md-button--primary }
