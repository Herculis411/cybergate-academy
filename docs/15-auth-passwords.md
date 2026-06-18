# Module 15 · Authentication & Password Security (Lab-Only)

**Tier:** Offensive Security · **Level:** Intermediate
**Prerequisites:** M14 · **Estimated time:** 90 minutes

!!! danger "Scope of this module"
    This module teaches **why weak authentication fails and how to defend it**.
    It deliberately **stops short of operational credential-attack tooling**.
    You will work only with **your own lab hashes** to understand resistance —
    not to build a tool that targets anyone. Attacking real accounts or
    credentials is a serious offence and is out of scope here, permanently.

---

## Objectives

- Understand how passwords are stored and why some storage fails.
- See, on your **own** lab hashes, why **salting + a slow hash** resists offline
  guessing.
- Recommend strong authentication defences (the deliverable that matters).

---

## 1. How password storage fails

Storing passwords in plain text, or with a single fast hash (like raw MD5/SHA-1),
means a leaked database is trivially reversible. This is **OWASP A07
Identification & Authentication Failures**.

## 2. The defence: salt + slow KDF

A **salt** makes each hash unique (defeating precomputed tables). A **slow**
key-derivation function (scrypt/bcrypt/argon2) makes large-scale guessing
expensive. Together they turn a leak from catastrophic into merely bad.

## 3. Demonstrating resistance (defensive)

The lab compares how a fast hash vs a slow, salted hash respond to a tiny,
self-made list of candidate words against **hashes you generated yourself**.
The point is to *feel* the cost difference, not to produce a cracker.

---

## Hands-on lab — fast vs slow, on your own hashes

!!! example "Lab task"
    Generate two hashes of a known lab password (one fast, one salted+slow).
    Time how a 5-word candidate list compares against each. Conclude with a
    defence recommendation.

```python
import hashlib, time
from hashlib import scrypt
import os

password = b"correct-horse"          # YOUR lab password
candidates = [b"password", b"letmein", b"correct-horse", b"admin", b"123456"]

# Fast hash (BAD practice — shown to illustrate weakness)
fast = hashlib.sha256(password).hexdigest()

# Salted, slow hash (GOOD practice)
salt = os.urandom(16)
slow = scrypt(password, salt=salt, n=2**14, r=8, p=1)

def check_fast(c): return hashlib.sha256(c).hexdigest() == fast
def check_slow(c): return scrypt(c, salt=salt, n=2**14, r=8, p=1) == slow

for label, fn in (("fast", check_fast), ("slow", check_slow)):
    t = time.time()
    hit = next((c.decode() for c in candidates if fn(c)), None)
    print(f"{label}: matched {hit} in {time.time()-t:.3f}s")
```

### Expected output artefact

```text
$ python3 auth_demo.py
fast: matched correct-horse in 0.000s
slow: matched correct-horse in 0.412s
```

Both find the known word (it's *your* password), but the slow KDF is hundreds of
times costlier **per guess** — at scale, that's the difference between a leak
being game-over and being survivable.

---

## Defender's note

- Enforce length over complexity; allow long passphrases.
- Use bcrypt/scrypt/argon2 with a per-user salt — never raw MD5/SHA-1.
- Add MFA; rate-limit and lock out repeated failures; monitor for credential
  stuffing (you'll detect this in Module 20).

---

## ✅ Checkpoint

1. Which OWASP category is this? **(A07.)**
2. What two properties make stored passwords resistant? **(Salt + slow KDF.)**
3. What is out of scope in this module? **(Attacking real credentials / building a cracker.)**

## 🏅 Badge unlocked: **Auth Defender** — Module 16 is now open.

[Continue to Module 16 · Vulnerability ID & Exploitation Concepts →](16-exploitation.md){ .md-button .md-button--primary }
