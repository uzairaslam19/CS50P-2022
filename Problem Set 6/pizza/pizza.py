from tabulate import tabulate
import sys
import csv
pizzas=[]
def main():
    if len(sys.argv)==2:
        if sys.argv[1].endswith('.csv'):
            try:
                with open(sys.argv[1]) as file:
                    reader=csv.DictReader(file)
                    headers=reader.fieldnames
                    for row in reader:
                        pizzas.append(row)
                    print(tabulate(pizzas,headers='keys',tablefmt='grid'))
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a CSV file")

    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")

if __name__=="__main__":
    main()