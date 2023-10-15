def main():
    Name= str(input("camelcase "))
    get_snakecase(Name)

def get_snakecase(Name):
    for a in Name:
        if a.isupper():
            print('_',a.lower(),sep=(""),end="")
        else:
            print(a,end="")
    print()

main()