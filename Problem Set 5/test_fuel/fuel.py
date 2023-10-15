def main():
    while True:
        try:
            fraction=input("Fraction: ")
            percentage=convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError,ZeroDivisionError):
            continue


def convert(fraction):
    while True:
        try:
            X, Y = map(int, fraction.split("/"))
            if X < 0 or Y <= 0 or X > Y:
                raise ValueError()
            else:
                return round((X/Y)*100)
        except (ValueError, ZeroDivisionError):
            raise



def gauge(percentage):
    if percentage <=1:
        return 'E'
    elif percentage >=99:
        return 'F'
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
