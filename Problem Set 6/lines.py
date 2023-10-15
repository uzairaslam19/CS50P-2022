import sys

def main():
    count=0
    if len(sys.argv)==2:
        if sys.argv[1].endswith('.py'):
            try:
                with open(sys.argv[1]) as file:
                    for row in file:
                        if row.lstrip().startswith('#') or row.lstrip()=="":
                            continue
                        else:
                            count+=1
                    print(count)
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a Python file")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")

main()