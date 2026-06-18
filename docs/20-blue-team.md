# Module 20 · Blue-Team Automation — Logs, IDS & SIEM

**Tier:** Advanced & Specialisation · **Level:** Advanced
**Prerequisites:** M16 · **Estimated time:** 100 minutes

---

## Objectives

- Detect the activity you performed earlier in the course.
- Write a Python detector for scanning behaviour in lab logs.
- Understand IDS (Suricata/Snort) and SIEM (Wazuh/ELK) at an intro level.
- **Catch your own attack** — the satisfying close to the offensive/defensive loop.

---

## 1. Why this module matters most

Every offensive skill in this course has a detection counterpart. A good
defender thinks like an attacker — which you now can. Here you turn that into
alerts.

## 2. Detection logic

The scan you ran in Module 10 leaves a fingerprint: one source IP touching many
ports/paths in a short window. That pattern is detectable in logs:

```python
import re
from collections import defaultdict, deque
import time

# Count distinct ports per source IP in a short window -> scan signal
hits = defaultdict(deque)
THRESHOLD, WINDOW = 15, 5  # 15 ports in 5 seconds

def observe(ip, port, now):
    q = hits[ip]
    q.append((now, port))
    while q and now - q[0][0] > WINDOW:
        q.popleft()
    distinct = len({p for _, p in q})
    if distinct >= THRESHOLD:
        print(f"ALERT possible port scan from {ip} ({distinct} ports/{WINDOW}s)")
```

## 3. IDS & SIEM

Suricata/Snort match traffic against rules; Wazuh/ELK aggregate and alert on
logs at scale. Your Python detector is the concept those tools industrialise.

---

## Hands-on lab — detect your own M10 scan

!!! example "Lab task"
    Replay the lab's IDS/log output from your earlier scan through your detector
    and confirm it raises an alert.

### Expected output artefact

```text
$ python3 detector.py lab-ids.log
ALERT possible port scan from 192.168.56.101 (24 ports/5s)
Correlated with: M10 enumeration run at 14:21
```

Your own earlier attack, caught by your own detector. That's the whole point.

---

## ✅ Checkpoint

1. What pattern signals a port scan? **(One IP, many ports, short window.)**
2. What do SIEM tools add over a single script? **(Scale + aggregation/alerting.)**
3. Why pair every offensive lesson with detection? **(Good defenders think like attackers.)**

## 🏅 Badge unlocked: **Blue-Team Operator** — Tier 4 (Lead) is now open.

[Continue to Module 21 · Reporting & Communication →](21-reporting.md){ .md-button .md-button--primary }
