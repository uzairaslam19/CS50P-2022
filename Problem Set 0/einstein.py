"""This program takes an input of Mass in kilograms from user and output the repectove energy using Einsteins formula E=mc2"""
def convert(mass):
    mass=int(mass)
    Energy=mass*300000000**2
    return Energy

def main(mass):
    energy=convert(mass)
    print(f"E:  {energy}")


main(input("m:  "))
