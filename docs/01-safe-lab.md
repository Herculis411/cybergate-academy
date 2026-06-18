# Module 01 · Building Your Safe Lab

!!! danger "You may not proceed until Module 00 is complete"
    Everything from here on is practical. It only stays legal because you run it
    against the **isolated lab you build in this module** — never against any
    system you don't own or aren't authorised to test.

**Tier:** Foundations · **Level:** Beginner · **Prerequisites:** M00
**Estimated time:** 90–120 minutes

---

## Objectives

By the end of this module you will be able to:

- Build an **isolated** virtual lab with an attacker box and vulnerable targets.
- Explain **host-only networking** and why it keeps your practice safe.
- Spin up deliberately-vulnerable web apps with one command.
- Prove your lab is air-gapped before you run a single attack.

---

## 1. The shape of a safe lab

A practice lab has three parts, all cut off from the internet and your home LAN:

- **Attacker:** a Kali Linux VM with the tooling pre-installed.
- **Full-OS target:** a Metasploitable VM (a whole vulnerable Linux machine).
- **Web targets:** DVWA, OWASP Juice Shop and WebGoat as containers.

The golden rule: traffic flows **attacker → target** inside the lab, and
**nothing** flows out to the real world.

## 2. Host-only networking

VirtualBox/VMware let you put VMs on a **host-only** network: the VMs can see
each other and your host, but have **no route to the internet or your LAN**.
This is what makes "attacking" a target legal — it's a closed system you own.

!!! warning "Never use bridged networking for vulnerable VMs"
    Bridged mode puts a deliberately-broken machine straight onto your real
    network where anyone can reach it. Always use host-only for targets.

## 3. Build steps

1. Install VirtualBox (or VMware).
2. Create a **Host-Only Network** (e.g. `192.168.56.0/24`).
3. Import the **Kali** VM; set its adapter to the host-only network.
4. Import **Metasploitable**; set its adapter to the same host-only network.
5. For the web targets, run the provided `labs/docker-compose.yml` on your host:
   ```bash
   cd labs
   docker compose up -d
   docker compose ps
   ```

---

## Hands-on lab — prove isolation

!!! example "Lab task"
    From your Kali VM:

    1. Show your lab IP: `ip addr`
    2. Confirm you **cannot** reach the internet: `ping -c2 8.8.8.8`
    3. Confirm you **can** reach the target: `ping -c2 192.168.56.x`
       (use Metasploitable's host-only IP)

### Expected output artefact

```text
$ ip addr show eth1
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> ...
    inet 192.168.56.101/24 brd 192.168.56.255 scope global eth1

$ ping -c2 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
--- 8.8.8.8 ping statistics ---
2 packets transmitted, 0 received, 100% packet loss   # ✅ air-gapped

$ ping -c2 192.168.56.102
64 bytes from 192.168.56.102: icmp_seq=1 ttl=64 time=0.43 ms
2 packets transmitted, 2 received, 0% packet loss      # ✅ target reachable
```

The 100% loss to `8.8.8.8` is the result you want — it proves nothing in your
lab can talk to the outside world.

---

## ✅ Checkpoint

1. What does host-only networking prevent? **(Reaching the internet/LAN.)**
2. Why is a *failed* ping to 8.8.8.8 a success here? **(It proves isolation.)**
3. Why never bridge a vulnerable VM? **(It exposes it to your real network.)**

## 🏅 Badge unlocked: **Lab Architect** — Module 02 is now open.

[Continue to Module 02 · Linux & Command-Line Essentials →](02-linux-cli.md){ .md-button .md-button--primary }
