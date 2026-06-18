# Module 00 · Ethics, Law & Authorisation

!!! danger "Start here. This module is the gate."
    No tools, no scans, no labs unlock until you have completed this module and
    passed its checkpoint quiz. Everything you learn on this platform can help
    people — or land you in a courtroom. The only difference is **permission**.
    Read this one properly.

**Tier:** Foundations · **Level:** Beginner · **Prerequisites:** None
**Estimated time:** 60–90 minutes

---

## Why this comes first

Most "learn hacking" resources hand you a port scanner on page one. That is how
beginners end up in trouble without realising they did anything wrong. The
techniques are genuinely useful and genuinely legal — *when you have
authorisation*. Without it, the exact same command is a criminal offence.

By the end of this module you will be able to:

- Explain, in your own words, what makes security testing legal versus illegal.
- Describe the UK **Computer Misuse Act 1990** and what it prohibits.
- Write a **scope** and **rules of engagement (RoE)** document.
- Follow **responsible disclosure** when you find a real vulnerability.
- Recognise where the legal, ethical outlets for your skills are (bug bounties,
  CTFs, your own lab).

---

## 1. The one idea that matters: authorisation

> **Permission is the line between a penetration tester and a criminal.**

A penetration tester runs a port scan against a client's server and gets paid.
A stranger runs the *identical* scan against that same server and commits an
offence. The packets are the same. The law cares about one thing the packets
don't show: **did the owner say yes, in writing, in advance?**

Three questions to ask yourself before *any* action against *any* system:

1. **Do I own this system, or have explicit written permission to test it?**
2. **Is what I'm about to do inside the agreed scope?**
3. **Could this cause harm or disruption I haven't been authorised to cause?**

If the answer to (1) is no, stop. There is no "I was only looking" defence.

---

## 2. The law — UK Computer Misuse Act 1990

The CMA is the core UK law. You are responsible for knowing it. The main
offences, in plain English:

| Section | Offence | Plain-English meaning |
|---------|---------|-----------------------|
| **s.1** | Unauthorised access to computer material | Getting into a system you weren't allowed into — even just looking, even if nothing is damaged. |
| **s.2** | Unauthorised access with intent to commit further offences | As above, but planning to do something else with that access. |
| **s.3** | Unauthorised acts impairing operation | Damaging, disrupting, or degrading a system (e.g. deleting data, denial of service). |
| **s.3A** | Making, supplying or obtaining tools for the above | Creating or distributing hacking tools intended for offences. |

!!! warning "Key points beginners get wrong"
    - **Curiosity is not a defence.** "I just wanted to see if it worked" does not make unauthorised access legal.
    - **Lack of damage is not a defence.** Under s.1, merely accessing without permission is already an offence.
    - **A site being insecure is not an invitation.** An unlocked door is still not yours to walk through.
    - **Testing a friend's site "to help" without written permission is still unauthorised.**

Other laws that interact with security work: the **Data Protection Act 2018 /
UK GDPR** (if you encounter personal data), the **Investigatory Powers Act**,
and equivalent laws wherever the target — or you — are located. Laws differ by
country; if a system is in another jurisdiction, that jurisdiction's law may
also apply to you.

!!! info "This is education, not legal advice"
    This module teaches the principles every practitioner works by. It is not
    legal advice. For real engagements, organisations get sign-off from someone
    legally authorised to grant it, and often legal counsel.

---

## 3. Scope and Rules of Engagement (RoE)

Professionals never test on a handshake. They work to two short documents.

**Scope** answers *what and where*:

- Which systems, IP ranges, domains, or applications are in scope?
- What is explicitly **out** of scope (e.g. production databases, third-party
  services, anything not owned by the client)?
- What time windows are testing allowed in?

**Rules of Engagement** answer *how*:

- Which techniques are permitted and which are forbidden (e.g. "no denial of
  service", "no social engineering of staff")?
- Who are the emergency contacts if something breaks?
- How is sensitive data to be handled, stored, and destroyed afterwards?
- What is the reporting format and deadline?

> If it isn't written in the scope, you are not authorised to touch it.
> "It was right next to something in scope" is not authorisation.

---

## 4. Responsible disclosure

If you find a genuine vulnerability — in a bug bounty, or because you stumbled
on it — **responsible disclosure** is how you act ethically:

1. **Stop.** Do not explore further than needed to confirm the issue. Do not
   access or download other people's data.
2. **Document** what you found, minimally and factually.
3. **Report privately** to the owner (security@ address, bug-bounty platform,
   or a published vulnerability-disclosure policy).
4. **Give them time** to fix it before telling anyone else. Industry norm is
   often around 90 days, but follow the programme's policy.
5. **Never extort.** "Pay me or I'll publish" turns disclosure into a crime.

---

## 5. Where your skills belong (the legal outlets)

You never need to break the law to practise or prove your skills:

- **This platform's isolated lab** (Module 01) — targets built to be attacked.
- **Capture The Flag (CTF)** events — legal, competitive, fun.
- **Bug bounty programmes** (HackerOne, Bugcrowd, Intigriti) — companies pay
  you to find flaws *with permission*.
- **Your own systems** — spin up a VM and go wild.

---

## 6. Hands-on lab — write your first RoE

No commands this time. Your deliverable is paperwork, because paperwork is what
keeps testing legal.

!!! example "Lab task"
    A fictional client, **Acme Bakery Ltd**, asks you to test their website
    `shop.acme-bakery.test` (a domain they own). They do **not** want their
    email server or staff touched.

    Produce two short documents:

    **1. Scope statement** containing:

    - In scope: `shop.acme-bakery.test` and its web application only
    - Out of scope: mail servers, staff, physical premises, any other domain
    - Testing window: weekdays 18:00–22:00
    - Authorised by: (name / role / date)

    **2. Rules of Engagement** containing:

    - Permitted: web application testing, automated scanning of the in-scope host
    - Forbidden: denial of service, social engineering, accessing real customer data
    - Emergency contact: (name / phone)
    - Data handling: findings stored encrypted, destroyed 30 days after report
    - Deliverable: written report within 7 days

### Expected output artefact

When you're done you should have something like the structure below. This is
the "what success looks like" for this module — a completed authorisation pack,
not terminal output.

```text
SCOPE STATEMENT — Acme Bakery Ltd
---------------------------------
In scope      : shop.acme-bakery.test (web application only)
Out of scope  : mail servers, staff, physical sites, all other domains
Window        : Weekdays 18:00–22:00 (client local time)
Authorised by : J. Stephen, Director, Acme Bakery Ltd — 2026-06-10

RULES OF ENGAGEMENT
-------------------
Permitted     : Web app testing; automated scanning of in-scope host
Forbidden     : DoS/DDoS; social engineering; accessing real customer data
Emergency     : Ops on-call, +44 ...
Data handling : Findings encrypted at rest; destroyed 30 days post-report
Deliverable   : Written report within 7 working days
Signed (tester): ______________________   Date: __________
```

---

## ✅ Checkpoint quiz (must pass to unlock Module 01)

Answer these before moving on. The platform records a pass here as the key that
unlocks the practical modules.

1. A website has an obvious flaw and no login. Are you allowed to test it
   without permission? **(Expected: No — insecurity is not authorisation.)**
2. Under the Computer Misuse Act 1990, is merely *accessing* a system without
   permission an offence even if you cause no damage?
   **(Expected: Yes — s.1.)**
3. You find a serious bug in a live site by accident. Give the first two steps
   of responsible disclosure. **(Expected: stop/limit access; report privately
   to the owner.)**
4. Name two legal places to practise offensive skills.
   **(Expected: this lab, CTFs, bug bounties, your own systems — any two.)**
5. Something is "right next to" an in-scope host but isn't listed in the scope.
   May you test it? **(Expected: No.)**

---

## 🏅 Badge unlocked

Completing this module earns the **Licence to Learn** badge and unlocks
**Module 01 · Building Your Safe Lab**, where you'll build the isolated
environment everything else runs in.

!!! quote "Remember"
    Every technique in this course is taught so you can **defend** systems and
    test **with permission**. The skill is the same; the ethics are what make
    you a professional instead of a statistic.

[Continue to Module 01 · Building Your Safe Lab →](01-safe-lab.md){ .md-button .md-button--primary }
