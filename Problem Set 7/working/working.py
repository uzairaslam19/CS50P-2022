import re

def convert(s):
    s = s.strip()

    # Define regular expression patterns for all possible formats
    patterns = [
        r"^(\d{1,2}(?::[0-5]\d)?)\s(AM|PM)\s\w{2}\s(\d{1,2}(?::[0-5]\d)?)\s(AM|PM)",
        r"^(\d{1,2}(?::[0-5]\d)?)\s(AM|PM)\s+to\s+(\d{1,2}(?::[0-5]\d)?)\s(AM|PM)",
        r"^(\d{1,2})\s(AM|PM)\s+to\s+(\d{1,2}(?::[0-5]\d)?)\s(AM|PM)",
    ]

    for pattern in patterns:
        match = re.match(pattern, s, re.IGNORECASE)
        if match:
            start_time, period, end_time, end_period = match.groups()

            # Split on ":" only if ":" is present in the time components
            if ":" in start_time:
                start_hour, start_minute = map(int, start_time.split(":"))
            else:
                start_hour, start_minute = int(start_time), 0

            if ":" in end_time:
                end_hour, end_minute = map(int, end_time.split(":"))
            else:
                end_hour, end_minute = int(end_time), 0

            # Handle "AM" and "PM" separately
            if period.upper() == 'PM' and start_hour != 12:
                start_hour += 12
            elif period.upper()=='AM' and start_hour ==12:
                start_hour=0
            if end_period.upper() == 'PM' and end_hour != 12:
                end_hour += 12
            elif end_period.upper()=='AM' and end_hour==12:
                end_hour=0
            return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"
        else:
            raise ValueError()
    # Return None for invalid inputs
    return None

def main():
    converted_time = convert(input("Hours: "))
    if converted_time is not None:
        print(converted_time)
    else:
        raise ValueError()

if __name__ == "__main__":
    main()
