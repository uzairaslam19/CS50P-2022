import sys


def main():
    i = 0
    while True:
        try:
            In = get_input("Item: ")
            x = Get_Amount(In)
            if x:
                i = i + x
                print(f"Total: ${i}0")
        except EOFError:
            sys.exit()


def get_input(param: str) -> str:
    while True:
        try:
            x = input(param).title()
            return x
        except (ValueError, KeyError):
            pass
        except EOFError:
            print()
            sys.exit()


def Get_Amount(param: str) -> float:
    di = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    if param in di:
        return float(di[param])


if __name__ == "__main__":
    main()
