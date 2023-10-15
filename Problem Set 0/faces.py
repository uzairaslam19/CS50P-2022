"""This Program takes a user input with emoticons in main Function,
 then calls convert function to convert the emoticons with emokis and returns the input"""

def convert(s):
    s=s.strip().replace(":)","🙂").replace(":(","🙁")
    return s
def main(userin):
    print(convert(userin))


main(input("Pass your sentence with emoticons.   "))