# Module 07 · Networking Fundamentals for Hackers

**Tier:** Networking & Automation Core · **Level:** Beginner–Intermediate
**Prerequisites:** M06 · **Estimated time:** 90 minutes

---

## Objectives

- Understand the TCP/IP model, IP addresses, ports and common protocols.
- Read the **TCP three-way handshake** in a packet capture.
- Know what a port scan is actually doing under the hood.

---

## 1. The stack, simply

Data travels in layers: application (HTTP, SSH) → transport (TCP, UDP) →
network (IP) → link (Ethernet). Each adds a header. Understanding this is what
separates someone who runs tools from someone who understands results.

## 2. Ports and protocols

Ports are doors on a host: 22 SSH, 80 HTTP, 443 HTTPS, 53 DNS. A service
"listening" on a port is a door that's open. Scanning (M10) is just knocking on
each door to see which open.

## 3. The TCP handshake

Every TCP connection starts with **SYN → SYN-ACK → ACK**. Many scan types work
by manipulating this handshake. Seeing it in Wireshark makes the abstract real.

---

## Hands-on lab — capture a handshake

!!! example "Lab task"
    Start Wireshark on your Kali lab interface, then `curl http://192.168.56.x`
    (a lab web target). Filter for `tcp` and find the handshake.

### Expected output artefact

```text
No.  Source           Destination      Protocol  Info
1    192.168.56.101   192.168.56.102   TCP       49210 → 80 [SYN]
2    192.168.56.102   192.168.56.101   TCP       80 → 49210 [SYN, ACK]
3    192.168.56.101   192.168.56.102   TCP       49210 → 80 [ACK]
4    192.168.56.101   192.168.56.102   HTTP      GET / HTTP/1.1
```

Packets 1–3 are the handshake; packet 4 is your request. All inside the lab.

---

## ✅ Checkpoint

1. Name the three handshake packets. **(SYN, SYN-ACK, ACK.)**
2. What does an open port mean? **(A service is listening.)**
3. Which transport protocol uses the handshake? **(TCP.)**

## 🏅 Badge unlocked: **Packet Reader** — Module 08 is now open.

[Continue to Module 08 · Python Networking →](08-python-networking.md){ .md-button .md-button--primary }
