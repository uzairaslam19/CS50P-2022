def get_string():
    return str(input("Input: "))

def shorten(a):
    li=['A','E','I','O','U']
    s=""
    for alphabet in a:
        if alphabet.upper() not in li:
            s+=alphabet
    return s
def main():
    x=get_string()
    s=shorten(x)
    print(s)

if __name__=="__main__":
    main()