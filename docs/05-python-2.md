# Module 05 · Python Fundamentals II — Functions, Modules, Errors

**Tier:** Foundations · **Level:** Beginner · **Prerequisites:** M04
**Estimated time:** 90 minutes

---

## Objectives

- Write reusable **functions** with parameters and return values.
- Organise code into **modules** and use `venv` + `pip`.
- Handle errors gracefully with `try/except` so tools don't crash.

---

## 1. Functions

```python
def usable_hosts(cidr):
    import ipaddress
    return [str(h) for h in ipaddress.ip_network(cidr).hosts()]

print(usable_hosts("192.168.56.0/30"))
```

Functions turn a one-off script into a toolkit you can reuse.

## 2. Virtual environments

Keep project dependencies isolated:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests scapy python-nmap
```

## 3. Error handling

Networks fail. Hosts are down. Handle it:

```python
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None
```

---

## Hands-on lab — harden your calculator

!!! example "Lab task"
    Refactor M04's subnet script into a function that validates input and
    returns a friendly message instead of crashing on a bad CIDR.

```python
import ipaddress

def list_hosts(cidr):
    try:
        net = ipaddress.ip_network(cidr, strict=False)
    except ValueError:
        return f"'{cidr}' is not a valid network."
    return [str(h) for h in net.hosts()]

print(list_hosts("not-a-network"))
print(list_hosts("192.168.56.0/30"))
```

### Expected output artefact

```text
$ python3 subnet_safe.py
'not-a-network' is not a valid network.
['192.168.56.1', '192.168.56.2']
```

No traceback on bad input — that's the win.

---

## ✅ Checkpoint

1. Why use a virtual environment? **(Isolate project dependencies.)**
2. What does `try/except` prevent? **(Crashes on errors.)**
3. Why wrap logic in functions? **(Reuse and clarity.)**

## 🏅 Badge unlocked: **Toolsmith** — Module 06 is now open.

[Continue to Module 06 · Python for Files & Data →](06-python-files.md){ .md-button .md-button--primary }
