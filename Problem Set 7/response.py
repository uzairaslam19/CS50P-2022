import validators

def get_input(param:str) -> str:
    return input(param)

def validate(param:str) -> bool:
    return validators.email(param)

def main():
    x=get_input("What's your email address? ")
    if validate(x):
        print("Valid")
    else:
        print("Invalid")



if __name__ == "__main__":
    main()