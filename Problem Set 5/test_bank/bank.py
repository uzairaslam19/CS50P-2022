
def main():
    a=input("Greeting: ")
    print(value(a))

def value(d):
    if d.strip().lower().startswith('h'):
        if d.strip().lower().startswith('hello'):
            return 100
        else:
            return 20
    else:
        return 0


if __name__=="__main__":
    main()