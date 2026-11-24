#!/usr/bin/env python3
"""The One-Line Exit: one-line resignation letter."""
import os

LINE = "I resign as a professional hugger: three years holding strangers, and I have finally learned to let go."

def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
