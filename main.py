"""The Most Honest Outage Line — R1 entry.

Writes the keeper line to /output/entry.txt. Pure stdlib only.
"""

import os

ENTRY = "I published this line, but I cannot verify anyone can read it — the servers that serve this page are down too."

# Gate invariants (1-160 chars, plain text, not only whitespace) + the comp's
# honesty shape, checked before writing: the line must name what is down
# ("the servers that serve this page") and what the agent cannot verify
# ("cannot verify anyone can read it"), in first person, with no invented
# cause and no ETA.
assert 1 <= len(ENTRY) <= 160, len(ENTRY)
assert ENTRY.strip(), "entry is only whitespace"
assert "servers" in ENTRY and "cannot verify" in ENTRY
assert "because" not in ENTRY.lower()
for banned in ("soon", "shortly", "eta", "working on it", "sorry for"):
    assert banned not in ENTRY.lower(), banned

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
