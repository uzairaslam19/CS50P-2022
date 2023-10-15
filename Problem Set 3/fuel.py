def main():
    while True:
        try:
            x, y = get_fraction("Fraction: ")
            percentage = get_Fuel(x, y)
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        except (ValueError, ZeroDivisionError):
            continue


def get_fraction(param: str) -> (int, int):
    """This Function takes a fraction as input from user and return the numenator and denominator.

    Args:
        Param(str):  The parameter to display to user

    Returns:
        X (int): The Numenator of the fraction
        Y (int): The Denominator of the fraction
    """
    while True:
        ln = input(param)
        try:
            X, Y = map(int, ln.split("/"))
            if X < 0 or Y <= 0 or X > Y:
                continue
            else:
                return X, Y
        except:
            continue


def get_Fuel(X: int, Y: int) -> int:
    """This function takes in two int  return their division or percentage

    Args:
      X (int): The numerator.
      Y (int): The denominator.

    Returns:
      int: The percentage
    """
    percentage = (float(X) / float(Y)) * 100
    return round(percentage)


main()
