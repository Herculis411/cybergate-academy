# Module 12 · Cryptography Essentials

**Tier:** Offensive Security · **Level:** Intermediate
**Prerequisites:** M11 · **Estimated time:** 90 minutes

---

## Objectives

- Understand hashing vs encryption, and symmetric vs asymmetric.
- Use the `cryptography` library correctly.
- Hash and verify passwords **the right way** (salted, slow).

---

## 1. Hashing vs encryption

- **Hashing** is one-way (you can't reverse it). Used for integrity and storing
  passwords. Example: SHA-256.
- **Encryption** is two-way with a key. Used for confidentiality. Symmetric uses
  one shared key; asymmetric uses a public/private pair.

## 2. Encrypt with Fernet (symmetric)

```python
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"lab secret")
print(f.decrypt(token).decode())   # -> lab secret
```

## 3. Store passwords correctly

Never store plain or fast-hashed passwords. Use a **salt** and a **slow** KDF
(scrypt/bcrypt/argon2). This is the defensive heart of Module 15.

---

## Hands-on lab — round-trip and verify

!!! example "Lab task"
    Encrypt then decrypt a message with Fernet, and hash + verify a password
    using a salted, slow function.

### Expected output artefact

```text
$ python3 crypto_lab.py
Encrypted: gAAAAABk...   (ciphertext)
Decrypted: lab secret    ✅ round-trip works
Password verify (correct pw): True
Password verify (wrong pw):   False
```

---

## ✅ Checkpoint

1. Is hashing reversible? **(No — one-way.)**
2. Why salt a password hash? **(Defeats precomputed/rainbow attacks.)**
3. Symmetric vs asymmetric — which uses a key pair? **(Asymmetric.)**

This maps to **OWASP A02 Cryptographic Failures**.

## 🏅 Badge unlocked: **Cipher Apprentice** — Module 13 is now open.

[Continue to Module 13 · Web App Security I →](13-webapp-1.md){ .md-button .md-button--primary }
