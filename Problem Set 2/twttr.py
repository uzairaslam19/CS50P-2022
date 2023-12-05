def get_string():
    return str(input("Input: "))

def shorten(a):
    li=['A','E','I','O','U']
    for alphabet in a:
        if alphabet.upper() not in li:
            print(alphabet, end="")

def main():
    x=get_string()
    shorten(x)
    print()
main()
