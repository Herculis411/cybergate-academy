# Module 11 · Packet Crafting & Traffic Analysis with Scapy

**Tier:** Networking & Automation Core · **Level:** Intermediate
**Prerequisites:** M10 · **Estimated time:** 100 minutes

---

## Objectives

- Craft and send packets with **Scapy** in the lab.
- Read replies and understand protocols at the packet level.
- Analyse a captured `.pcap` file.

!!! danger "Lab network only"
    Crafting and sending packets on networks you don't own can be illegal and
    disruptive. Stay on the host-only lab.

---

## 1. Scapy in one breath

Scapy lets you build a packet layer by layer and send it:

```python
from scapy.all import IP, ICMP, sr1

pkt = IP(dst="192.168.56.102") / ICMP()
reply = sr1(pkt, timeout=2, verbose=0)
print(reply.summary() if reply else "no reply")
```

## 2. Why craft packets

Understanding scans, protocols and IDS detection (M20) is much deeper when
you've built the packets yourself rather than only running tools.

## 3. Analysing captures

```python
from scapy.all import rdpcap
packets = rdpcap("capture.pcap")
print(len(packets), "packets")
```

---

## Hands-on lab — craft an ICMP echo

!!! example "Lab task"
    Send an ICMP echo to your lab target and confirm the reply, then read back
    a small capture.

### Expected output artefact

```text
$ sudo python3 ping_scapy.py
Sent 1 packet.
Reply: IP / ICMP 192.168.56.102 > 192.168.56.101 echo-reply 0
```

You built that echo request by hand and watched the target answer — entirely
within your lab.

---

## ✅ Checkpoint

1. What does Scapy let you do? **(Craft/send/analyse packets.)**
2. Why craft packets instead of only using tools? **(Deeper protocol understanding.)**
3. Where may you send crafted packets? **(Lab network only.)**

## 🏅 Badge unlocked: **Packet Crafter** — Tier 2 (Analyst) is now open.

[Continue to Module 12 · Cryptography Essentials →](12-cryptography.md){ .md-button .md-button--primary }
