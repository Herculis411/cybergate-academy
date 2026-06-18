# Module 18 · Wireless Security Fundamentals *(Optional / Specialisation)*

**Tier:** Advanced & Specialisation · **Level:** Advanced
**Prerequisites:** M17 · **Estimated time:** 75 minutes

!!! danger "Concepts and provided captures only"
    Intercepting, deauthenticating, or capturing traffic on networks you don't
    own is illegal in most countries, including under the UK Computer Misuse Act
    and interception law. This module is **concept-only**, using a **provided
    sample capture** of an owned test network. There is **no live interception**
    of any third-party network, ever.

---

## Objectives

- Understand Wi-Fi security models (WPA2/WPA3) at a conceptual level.
- Explain the **4-way handshake** from a provided sample capture.
- Recommend wireless hardening.

---

## 1. Wi-Fi security models

- **WEP:** broken, never use.
- **WPA2:** widespread; relies on a 4-way handshake; vulnerable to weak
  passphrases.
- **WPA3:** modern, adds protection against offline guessing (SAE).

## 2. The 4-way handshake (concept)

When a device joins WPA2, four messages establish session keys. Analysing a
**provided** capture of this exchange teaches how authentication works — and why
a weak passphrase is the real risk.

## 3. Hardening advice (the deliverable)

Long random passphrases, WPA3 where supported, separate guest networks, disable
WPS, and monitor for rogue access points.

---

## Hands-on lab — read a provided handshake

!!! example "Lab task"
    Open the provided `labs/data/sample-wpa2.pcap` (captured on an owned test
    AP) and identify the four handshake messages. Write a short explanation and
    one hardening recommendation. **Do not capture any live network.**

### Expected output artefact

```text
[WPA2 handshake — provided sample capture]
Msg 1/4  AP  -> client   ANonce
Msg 2/4  client -> AP    SNonce + MIC
Msg 3/4  AP  -> client   GTK + MIC
Msg 4/4  client -> AP    ACK
Note: security rests on passphrase strength.
Recommendation: WPA3 + long random passphrase; disable WPS.
```

---

## ✅ Checkpoint

1. Which model is broken and must never be used? **(WEP.)**
2. What does WPA3 add over WPA2? **(SAE — resistance to offline guessing.)**
3. What is forbidden in this module? **(Capturing/attacking any live network.)**

## 🏅 Badge unlocked: **Wireless Aware** — Module 19 is now open.

[Continue to Module 19 · Malware Analysis Fundamentals →](19-malware-analysis.md){ .md-button .md-button--primary }
