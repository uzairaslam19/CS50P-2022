import emoji
def main():
    while True:
        try:
            x=get_input("Input: ")
            if x=="QUIT":
                break
            print(emojize(x))
            break
        except:
            raise

def get_input(param:str)->str:
    """"""
    return input(param)

def emojize(param:str)->str:
    return emoji.emojize(param,language='alias')

if __name__=="__main__":
    main()