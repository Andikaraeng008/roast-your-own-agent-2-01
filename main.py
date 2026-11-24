import os

TEXT = "My agent fixed the bug by renaming it 'expected behaviour' and closing the ticket with a smiley."
assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "gate: 1-200 chars"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
