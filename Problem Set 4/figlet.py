from pyfiglet import Figlet
import sys
import random
figlet=Figlet()

def main():
    Fonts=figlet.getFonts()
    if len(sys.argv)<2:
        x=input("Input: ")
        y=random.choice(Fonts)
        figlet.setFont(font=y)
        print(figlet.renderText(x))
    elif len(sys.argv)>=2:
        if sys.argv[1] in ['-f','--font'] and sys.argv[2] in Fonts:
            x=input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(x))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit()
if __name__=="__main__":
    main()



