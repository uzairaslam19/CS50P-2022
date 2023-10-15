import sys


def main():
    di = {}
    try:
        while True:
            x = get_input()
            if x == "QUIT":
                break
            return_grocery(x, di)
    except EOFError:
        print()
        print_grocery(di)


def get_input() -> str:
    while True:
        try:
            x = input()
            return x.upper()
        except EOFError:
            raise
        except:
            pass


def return_grocery(param: str, grocery_dict: dict) -> None:
    grocery_dict[param] = grocery_dict.get(param, 0) + 1


def print_grocery(grocery_dict: dict) -> None:
    for item, count in sorted(grocery_dict.items()):
        print(f"{count} {item}")


if __name__ == "__main__":
    main()
