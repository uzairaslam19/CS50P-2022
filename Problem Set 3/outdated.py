months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        try:
            x = get_input("Date: ")
            if "/" in x:
                formatted_date = split_by_backslash(x)
            else:
                formatted_date = split_by_space(x)

            if formatted_date:
                print(formatted_date.strip())
                break
            else:
                continue
        except KeyboardInterrupt:
            break


def get_input(param: str) -> str:
    return input(param).strip()


def split_by_backslash(s: str) -> str:
    try:
        string1 = s.split("/")
        month, day, year = map(int, string1)
        if 1 <= month <= 12 and 1 <= day <= 31:
            return f"{year:04d}-{month:02d}-{day:02d}"
        else:
            return None
    except ValueError:
        return None


def split_by_space(s: str) -> str:
    parts = s.split()
    if len(parts) == 3 and "," not in s:
        return None
    elif len(parts) == 3:
        try:
            month, day, year = parts
            month = month.title()
            day = day.strip(",")
            month_index = months.index(month) + 1
            if 1 <= month_index <= 12 and 1 <= int(day) <= 31:
                return f"{year:04}-{int(month_index):02}-{int(day):02}"
            else:
                return None
        except ValueError:
            return None
    else:
        return None


main()
