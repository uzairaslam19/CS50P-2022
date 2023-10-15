import random

def main():
    level=get_level()
    score=0
    for _ in range(10):
        x=generate_integer(level)
        y=generate_integer(level)
        correct =x + y

        tries =0
        while tries<3:
            try:
                user_answer=int(input(f"{x} + {y} = "))
                if user_answer==correct:
                    score+=1
                    break
                else:
                    print('EEE')
                    tries+=1
            except ValueError:
                print('EEE')
                tries+=1
        if tries==3:
            print(f"{x} + {y} = {correct}")
    print(f"Score{score}")

def get_level()->int:
    while True:
        x=input("Level: ")
        if x.isdigit() and x in ('1','2','3'):
            return int(x)
        else:
            continue
def generate_integer(level):
    if level==1:
        return random.randint(0,9)
    elif level==2:
        return random.randint(10,99)
    elif level==3:
        return random.randint(100,999)
    else:
        raise ValueError('EEE')

if __name__=="__main__":
    main()
