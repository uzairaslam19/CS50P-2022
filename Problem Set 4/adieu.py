import inflect
p=inflect.engine()
import sys
def main():
    li=[]
    while True:
        try:
            x=get_input("Name: ")
            update_li(x,li)

        except EOFError:
            print()
            print_lyrics(li)
            sys.exit()
def get_input(param:str)->str:
    """ """
    return input(param)
def update_li(param:str,alist:list)-> None:
    alist=alist.append(param)

def print_lyrics(alist:list)->None:
    print(f"Adieu, adieu, to {p.join(alist)}")

if __name__=="__main__":
    main()