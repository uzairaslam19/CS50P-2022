import sys
import csv
names=[]
def main():
    if len(sys.argv)==3:
        if sys.argv[1].endswith('.csv'):
            try:
                with open(sys.argv[1]) as file:
                    reader=csv.DictReader(file)
                    for row in reader:
                        lastname,firstname=row['name'].split(', ')
                        names.append({"first":firstname,"last":lastname,"house":row['house']})
                with open(sys.argv[2],"w",newline='') as file:
                    writer =csv.DictWriter(file,fieldnames=['first','last','house'])
                    writer.writeheader()
                    for name in names:
                        writer.writerow({'first':name['first'],'last':name['last'],'house':name['house']})

            except FileNotFoundError:
                sys.exit("File does not exsit")
        else:
            sys.exit("File is not a csv")
    elif len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too Many command-line arguments")
main()