# Module 04 · Python Fundamentals I — Types & Control Flow

**Tier:** Foundations · **Level:** Beginner · **Prerequisites:** M03
**Estimated time:** 90 minutes

---

## Objectives

- Use variables and the core data types (str, int, list, dict, bool).
- Control flow with `if/elif/else` and loops (`for`, `while`).
- Write a small, useful tool — your first security-flavoured script.

---

## 1. Data types you'll use constantly

- **Strings** for hostnames, banners, payloadsafe text.
- **Integers** for ports and counts.
- **Lists** for sets of hosts or ports.
- **Dictionaries** for structured results (`{"host": "10.0.0.5", "ports": [22, 80]}`).
- **Booleans** for "is it open / reachable?".

## 2. Control flow

```python
ports = [22, 80, 443]
for port in ports:
    if port == 443:
        print(f"{port} is HTTPS")
    else:
        print(f"{port} is something else")
```

Loops + conditionals are 80% of scripting. Get comfortable here and the
networking modules become easy.

---

## Hands-on lab — subnet host calculator

!!! example "Lab task"
    Write `subnet.py` that prints all usable host addresses in a small network
    (e.g. `192.168.56.0/29`). Use Python's built-in `ipaddress` module.

```python
import ipaddress

net = ipaddress.ip_network("192.168.56.0/29")
for host in net.hosts():
    print(host)
```

### Expected output artefact

```text
$ python3 subnet.py
192.168.56.1
192.168.56.2
192.168.56.3
192.168.56.4
192.168.56.5
192.168.56.6
```

A /29 has 6 usable hosts — exactly what your script prints. You'll feed lists
like this into your scanner in Module 10.

---

## ✅ Checkpoint

1. Which type holds structured results best? **(Dictionary.)**
2. How many usable hosts in a /29? **(6.)**
3. What two constructs make up most scripts? **(Loops and conditionals.)**

## 🏅 Badge unlocked: **Code Initiate** — Module 05 is now open.

[Continue to Module 05 · Python Fundamentals II →](05-python-2.md){ .md-button .md-button--primary }
