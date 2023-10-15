
def value(d):
    if d.strip().lower().startswith('h'):
        if d.strip().lower().startswith('hello'):
            return "$0"
        else:
            return "$20"
    else:
        return"$100"

def main():
    a=input("Greeting: ")
    print(value(a))
if __name__=="__main__":
    main()