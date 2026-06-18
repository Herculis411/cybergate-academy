# Module 08 · Python Networking — Sockets & HTTP

**Tier:** Networking & Automation Core · **Level:** Beginner–Intermediate
**Prerequisites:** M07 · **Estimated time:** 90 minutes

---

## Objectives

- Open TCP connections with the `socket` module.
- Make HTTP requests with `requests`.
- Build a **banner grabber** that identifies a lab service — your first recon tool.

!!! warning "Lab targets only"
    Run everything in this module against your **lab IPs** (`192.168.56.x`)
    only. Connecting to systems you don't own is exactly what Module 00
    forbids.

---

## 1. Sockets

A socket is a programmatic network connection. Connect, send, receive, close:

```python
import socket

def grab_banner(host, port, timeout=2):
    try:
        with socket.create_connection((host, port), timeout) as s:
            s.settimeout(timeout)
            return s.recv(1024).decode(errors="ignore").strip()
    except OSError:
        return None
```

## 2. HTTP with requests

```python
import requests
r = requests.get("http://192.168.56.102")
print(r.status_code, r.headers.get("Server"))
```

---

## Hands-on lab — banner grabber

!!! example "Lab task"
    Point the function above at a known service on your Metasploitable host and
    report the banner it returns.

```python
host = "192.168.56.102"   # lab target only
for port in (21, 22, 80):
    banner = grab_banner(host, port)
    print(f"{port}: {banner or 'no banner'}")
```

### Expected output artefact

```text
$ python3 banners.py
21: 220 (vsFTPd 2.3.4)
22: SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
80: no banner
```

Those version strings are how you later match a service to a known issue
(Module 16) — all against your own lab.

---

## ✅ Checkpoint

1. What is a socket? **(A programmatic network connection.)**
2. Why does a banner matter? **(It reveals the service/version.)**
3. Which IPs may you target here? **(Lab IPs only.)**

## 🏅 Badge unlocked: **Socket Smith** — Module 09 is now open.

[Continue to Module 09 · Reconnaissance & OSINT →](09-recon-osint.md){ .md-button .md-button--primary }
