# Module 10 · Scanning & Enumeration

**Tier:** Networking & Automation Core · **Level:** Intermediate
**Prerequisites:** M09 · **Estimated time:** 100 minutes

---

## Objectives

- Discover live hosts and open services with **Nmap**.
- Automate and parse scans in Python.
- Interpret results responsibly and turn them into notes.

!!! danger "Lab subnet only"
    Scanning a network you don't own is an offence under the Computer Misuse
    Act. Every scan here targets your **host-only lab subnet**
    (`192.168.56.0/24`) and nothing else.

---

## 1. What scanning does

A scan asks each host which ports are open and what's listening. It's the
active follow-up to recon (M09) and maps to ATT&CK *Discovery*.

## 2. Nmap basics

```bash
nmap -sV 192.168.56.0/24      # service/version detection, lab subnet
```

## 3. Automating with python-nmap

```python
import nmap
scanner = nmap.PortScanner()
scanner.scan("192.168.56.102", "1-1024", arguments="-sV")

for host in scanner.all_hosts():
    for proto in scanner[host].all_protocols():
        for port in sorted(scanner[host][proto]):
            svc = scanner[host][proto][port]
            print(f"{host}:{port} {svc['state']} {svc.get('name')} {svc.get('version')}")
```

---

## Hands-on lab — automated service scan

!!! example "Lab task"
    Scan your Metasploitable host, parse the results in Python, and print a
    tidy table of open services.

### Expected output artefact

```text
$ python3 scan.py
192.168.56.102:21   open  ftp    vsftpd 2.3.4
192.168.56.102:22   open  ssh    OpenSSH 4.7p1
192.168.56.102:80   open  http   Apache 2.2.8
192.168.56.102:3306 open  mysql  MySQL 5.0.51a
```

Save this table — it's the input to vulnerability identification in Module 16.

---

## ✅ Checkpoint

1. Which subnet may you scan? **(The lab `192.168.56.0/24` only.)**
2. What ATT&CK phase is scanning? **(Discovery.)**
3. What does `-sV` add? **(Service/version detection.)**

## 🏅 Badge unlocked: **Enumerator** — Module 11 is now open.

[Continue to Module 11 · Packet Crafting with Scapy →](11-scapy.md){ .md-button .md-button--primary }
