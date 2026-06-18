# Module 03 · Git & GitHub for Security Work

**Tier:** Foundations · **Level:** Beginner · **Prerequisites:** M02
**Estimated time:** 60 minutes

---

## Objectives

- Track your scripts and findings with Git.
- Use branches to work safely on changes.
- Understand **secrets hygiene** — never commit passwords, keys or tokens.

---

## 1. Why version control matters in security

Your tooling, notes and reports all evolve. Git gives you history, the ability
to undo, and a way to collaborate. Equally important: Git is where secrets get
leaked. Knowing how to *keep* secrets out of a repo is a security skill in
itself.

## 2. Core workflow

```bash
git init
git add scanner.py
git commit -m "Add lab subnet scanner"
git branch feature/banner-grab
git checkout feature/banner-grab
```

`git log --oneline` shows your history compactly.

## 3. Secrets hygiene

Add a `.gitignore` for anything sensitive — `.env` files, keys, captured data:

```gitignore
.env
*.key
captures/
loot/
```

Real teams add automated secret scanning so a key never reaches the remote.
Treat any committed secret as compromised — rotate it immediately.

---

## Hands-on lab — catch a secret before it commits

!!! example "Lab task"
    1. Create a repo for your lab scripts.
    2. Create a file `.env` containing a fake key `API_KEY=do-not-commit`.
    3. Add `.env` to `.gitignore` and confirm Git ignores it.

### Expected output artefact

```text
$ echo "API_KEY=do-not-commit" > .env
$ echo ".env" > .gitignore
$ git add .
$ git status
On branch main
Changes to be committed:
  new file:   .gitignore
# .env is NOT listed — it is correctly ignored ✅

$ git log --oneline
a1b2c3d  Add gitignore to protect secrets
```

---

## ✅ Checkpoint

1. What goes in `.gitignore`? **(Secrets, keys, captured/loot data.)**
2. If you accidentally commit a key, what must you do? **(Rotate it — treat it as compromised.)**
3. What does `git log --oneline` show? **(Compact commit history.)**

## 🏅 Badge unlocked: **Version Keeper** — Module 04 is now open.

[Continue to Module 04 · Python Fundamentals I →](04-python-1.md){ .md-button .md-button--primary }
