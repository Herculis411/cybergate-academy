# Module 06 · Python for Files & Data

**Tier:** Foundations · **Level:** Beginner · **Prerequisites:** M05
**Estimated time:** 90 minutes

---

## Objectives

- Read and write files safely.
- Parse JSON and CSV.
- Use **regular expressions** to extract structured data from messy text.
- Produce your first log-analysis report (a blue-team skill).

---

## 1. Files

```python
with open("access.log") as f:
    for line in f:
        process(line)
```

The `with` block closes the file for you, even on error.

## 2. Structured data

`json.load` / `json.dumps` for JSON; the `csv` module for spreadsheets. Most
security tools speak one of these, so parsing them is essential glue.

## 3. Regular expressions

Regex extracts patterns — IPs, timestamps, status codes — from raw logs:

```python
import re
ip_pattern = re.compile(r"\d{1,3}(?:\.\d{1,3}){3}")
```

---

## Hands-on lab — log triage report

!!! example "Lab task"
    Given a sample `access.log`, report the **top 10 source IPs** and count any
    `404` responses. (A sample log ships in `labs/data/access.log`.)

```python
import re
from collections import Counter

ip_re = re.compile(r"\d{1,3}(?:\.\d{1,3}){3}")
ips, errors = Counter(), 0

with open("access.log") as f:
    for line in f:
        m = ip_re.search(line)
        if m:
            ips[m.group()] += 1
        if " 404 " in line:
            errors += 1

print("Top source IPs:")
for ip, count in ips.most_common(10):
    print(f"  {ip:<16} {count}")
print(f"Total 404s: {errors}")
```

### Expected output artefact

```text
$ python3 logtriage.py
Top source IPs:
  192.168.56.50    142
  192.168.56.51     88
  192.168.56.77     12
Total 404s: 37
```

A spike from one IP with many 404s is exactly the pattern you'll later detect
as scanning in Module 20.

---

## ✅ Checkpoint

1. Why use a `with` block to open files? **(It always closes the file.)**
2. What does regex give you over plain string search? **(Pattern extraction.)**
3. What might many 404s from one IP indicate? **(Scanning/enumeration.)**

## 🏅 Badge unlocked: **Data Wrangler** — Tier 1 (Operator) is now open.

[Continue to Module 07 · Networking Fundamentals →](07-networking.md){ .md-button .md-button--primary }
