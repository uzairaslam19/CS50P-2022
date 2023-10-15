import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s=s.strip()
    pattern = r"\bum\b"
    matches=re.findall(pattern, s, re.IGNORECASE)
    if matches:
        return len(matches)
    else:
        return 0



if __name__ == "__main__":
    main()