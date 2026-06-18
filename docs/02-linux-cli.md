# Module 02 · Linux & Command-Line Essentials

**Tier:** Foundations · **Level:** Beginner · **Prerequisites:** M01
**Estimated time:** 90 minutes

---

## Objectives

- Navigate the filesystem, manage files and permissions.
- Understand users, processes, and the pipe (`|`).
- Chain commands with `grep`, `sed`, `awk` to extract data.
- Be comfortable enough that later modules feel natural.

---

## 1. Moving around

`pwd` (where am I), `ls -la` (list, including hidden), `cd` (change directory),
`cat`/`less` (read files), `find` (search the tree). Hidden files start with a
dot — attackers and defenders both care about them.

## 2. Permissions

Linux permissions are read/write/execute for owner/group/other. `ls -l` shows
them as `-rwxr-xr--`. `chmod` changes them; `chown` changes ownership.
Misconfigured permissions are a recurring theme in privilege escalation (M17),
so understanding them now pays off later.

## 3. Pipes and filters

The pipe sends one command's output into another. This is the heart of working
fast on the command line:

```bash
cat access.log | grep "404" | awk '{print $1}' | sort | uniq -c | sort -rn
```

That one line: read a log → keep 404 lines → pull the first field (IP) → count
unique IPs → sort by count. You'll reuse this pattern constantly in log
analysis (M06, M20).

---

## Hands-on lab — shell scavenger hunt

!!! example "Lab task"
    In your Kali home directory:

    1. Create a folder `hunt/`, and inside it a hidden file `.flag` containing
       the word `found`.
    2. Set the file so only you can read it (`chmod 600`).
    3. Use a single piped command to find any file in `hunt/` containing
       "found".

### Expected output artefact

```text
$ mkdir hunt && echo "found" > hunt/.flag && chmod 600 hunt/.flag
$ grep -r "found" hunt/ 2>/dev/null
hunt/.flag:found

$ ls -la hunt/
-rw-------  1 kali kali    6 Jun 10 14:02 .flag   # only owner can read
```

---

## ✅ Checkpoint

1. What does `chmod 600` mean? **(Owner read/write; no one else.)**
2. What does the pipe `|` do? **(Sends output of one command into another.)**
3. How do you list hidden files? **(`ls -la` / `ls -a`.)**

## 🏅 Badge unlocked: **Shell Walker** — Module 03 is now open.

[Continue to Module 03 · Git & GitHub for Security Work →](03-git.md){ .md-button .md-button--primary }
