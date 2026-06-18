# Lab sample data

These files are used by the hands-on labs. They are safe and for use **only**
inside your isolated practice lab (see Module 01).

| File | Used in | What it is |
|------|---------|------------|
| `access.log` | Module 06 | A sample Apache-style access log. One source IP (`192.168.56.77`) probes sensitive paths and generates ~40 `404`s — practise spotting it. |
| `lab-demo.pcap` | Module 11 | A tiny capture showing a TCP handshake and an ICMP echo/reply between two lab hosts. Open it with Wireshark or Scapy's `rdpcap()`. |
| `benign-sample.bin` | Module 19 | A **harmless** compiled ELF program that prints "hello from the lab". Use it to practise static triage (`file`, `sha256sum`, `strings`). It contains no malicious code. |

## About the WPA2 sample (Module 18)

Module 18 references a WPA2 handshake capture. For lawful teaching, source a
sample capture from a network **you own** or use a publicly provided educational
capture (for example, the sample captures published on the Wireshark wiki).
Save it here as `sample-wpa2.pcap`. **Never** capture or analyse traffic from a
network you do not own or are not authorised to test.

## Regenerating these files

`access.log`, `lab-demo.pcap` and `benign-sample.bin` can be regenerated with
the helper scripts in `labs/tools/` if you want to customise them.
