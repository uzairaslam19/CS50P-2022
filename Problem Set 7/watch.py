import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s=s.strip()
    if matches := re.search(r'["\']https?://(www\.)?(?:\w+\.\w+/\w+/)(\w+)["\']',s):
        return f"https://youtu.be/{matches.group(2)}"
    else:
        return None



if __name__ == "__main__":
    main()