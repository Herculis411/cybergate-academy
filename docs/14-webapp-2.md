# Module 14 · Web Application Security II — Automating Tests

**Tier:** Offensive Security · **Level:** Intermediate
**Prerequisites:** M13 · **Estimated time:** 100 minutes

---

## Objectives

- Script repeatable, **non-destructive** checks against lab apps.
- Detect missing security headers and reflected input.
- Understand why automation helps coverage (and its limits).

!!! danger "Lab apps only"
    These scripts run against your DVWA/Juice Shop containers on
    `127.0.0.1`. Automated testing of someone else's site without authorisation
    is unlawful.

---

## 1. Security headers check

Missing headers are a quick, safe signal of misconfiguration (OWASP A05):

```python
import requests

WANTED = ["Content-Security-Policy", "X-Frame-Options",
          "X-Content-Type-Options", "Strict-Transport-Security"]

r = requests.get("http://127.0.0.1:8080")
missing = [h for h in WANTED if h not in r.headers]
print("Missing headers:", missing or "none")
```

## 2. Reflected-input check (safe)

Send a harmless marker and see whether it comes back unencoded — a non-damaging
indicator worth manual follow-up. Keep payloads benign; you're detecting, not
exploiting.

---

## Hands-on lab — header + reflection scanner

!!! example "Lab task"
    Run the header check against a lab app and report what's missing, then note
    one form that reflects a benign marker.

### Expected output artefact

```text
$ python3 webcheck.py
Target: http://127.0.0.1:8080 (DVWA lab)
Missing headers: ['Content-Security-Policy', 'X-Frame-Options']
Reflection: marker 'cq123' returned unencoded in 'search' response
Recommendation: add security headers; encode output
```

---

## ✅ Checkpoint

1. Which OWASP category do missing headers signal? **(A05 Misconfiguration.)**
2. Why keep test markers benign? **(You're detecting, not exploiting/damaging.)**
3. Where do these scripts point? **(Localhost lab apps.)**

## 🏅 Badge unlocked: **Automation Analyst** — Module 15 is now open.

[Continue to Module 15 · Authentication & Password Security →](15-auth-passwords.md){ .md-button .md-button--primary }
