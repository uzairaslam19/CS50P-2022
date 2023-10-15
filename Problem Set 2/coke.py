def process_change(a):
    while a!=0:
        coin=int(input("Insert Coin: "))
        if coin==30:
            print(f"Amount Due: {a}")
            continue
        if coin <a:
            print(f"Amount Due: {a-coin}")
            a=a-coin
            continue
        elif coin >=a:
            print(f"Change Owed: {coin-a}")
            break


def main():
    x=50
    print(f"Amount Due: {x}")
    process_change(x)
main()