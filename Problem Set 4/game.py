import random
import sys
def main():
    while True:
        try:
            x=int(get_level("Level: "))
            if x<1:
                continue
        except ValueError:
            pass
        else:
            while True:
                y=generate_random(x)
                try:
                    z=int(guess("Guess: "))
                    if 1<=z<y:
                        print("Too Small!")
                        continue
                    elif z>y>=1:
                        print("Too Large!")
                        continue
                    elif z==y:
                        print("Just right!")
                    else:
                        continue
                    sys.exit()
                except ValueError:
                    continue
def get_level(param:str)->str:
    return input(param)

def generate_random(param:int)->int:
    return random.randrange(1,param+1)
def guess(param:str)->int:
    return input(param)

if __name__=="__main__":
    main()