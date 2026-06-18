#!/usr/bin/env python3
"""
detector.py  —  CyberQuest Academy, Module 20 / Capstone Phase 6 (Blue Team)

A small, defensive log detector. It reads a connection/IDS log and raises an
alert when a single source IP touches many distinct ports in a short time
window — the classic fingerprint of a port scan.

This is a DEFENSIVE tool: it detects activity, it does not perform any. Run it
against the provided lab sample log to see your earlier lab scan get caught.

Usage:
    python3 detector.py lab-ids.log

Log line format (key=value), e.g.:
    2026-06-11T14:21:00 src=192.168.56.101 dst=192.168.56.102 dport=21 proto=TCP action=ACCEPT
"""

import sys
from collections import defaultdict, deque
from datetime import datetime

# --- Detection thresholds (tune these to change sensitivity) ---------------
THRESHOLD = 15        # distinct destination ports...
WINDOW_SECONDS = 5    # ...seen from one source within this many seconds = scan


def parse_line(line):
    """Turn one log line into (timestamp, fields dict). Returns None if it
    isn't a well-formed line."""
    parts = line.split()
    if not parts:
        return None
    try:
        ts = datetime.strptime(parts[0], "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        return None  # not a timestamped line, skip it
    fields = {}
    for token in parts[1:]:
        if "=" in token:
            key, _, value = token.partition("=")
            fields[key] = value
    return ts, fields


def detect(path):
    """Stream the log and raise an alert the first time any source IP crosses
    the scan threshold. Uses a per-source sliding window of recent ports."""
    # For each source IP: a deque of (timestamp, port) within the window.
    recent = defaultdict(deque)
    alerted = set()        # don't alert on the same source repeatedly
    alerts = []

    with open(path) as f:
        for raw in f:
            parsed = parse_line(raw.strip())
            if not parsed:
                continue
            ts, fields = parsed

            src = fields.get("src")
            dport = fields.get("dport")
            if not src or not dport:
                continue

            q = recent[src]
            q.append((ts, dport))

            # Drop anything older than the window from the front of the deque.
            while q and (ts - q[0][0]).total_seconds() > WINDOW_SECONDS:
                q.popleft()

            distinct_ports = {p for _, p in q}

            if len(distinct_ports) >= THRESHOLD and src not in alerted:
                alerted.add(src)
                first_ts = q[0][0]
                alerts.append({
                    "src": src,
                    "dst": fields.get("dst", "?"),
                    "ports": len(distinct_ports),
                    "window_start": first_ts,
                    "window_end": ts,
                })

    return alerts


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 detector.py <logfile>")
        sys.exit(1)

    path = sys.argv[1]
    try:
        alerts = detect(path)
    except FileNotFoundError:
        print(f"[!] Log file not found: {path}")
        sys.exit(1)

    print(f"Scanning {path} for port-scan activity "
          f"(>= {THRESHOLD} ports in {WINDOW_SECONDS}s)...\n")

    if not alerts:
        print("No port-scan activity detected.")
        return

    for a in alerts:
        span = (a["window_end"] - a["window_start"]).total_seconds()
        print(f"ALERT  possible port scan from {a['src']} -> {a['dst']}")
        print(f"       {a['ports']} distinct ports in ~{span:.1f}s "
              f"(first seen {a['window_start'].strftime('%H:%M:%S')})")
        print(f"       Correlate with your enumeration phase (Module 10 / "
              f"Capstone Phase 2).\n")

    print(f"{len(alerts)} alert(s) raised. "
          f"Save this output to 06_detection/ as engagement evidence.")


if __name__ == "__main__":
    main()
