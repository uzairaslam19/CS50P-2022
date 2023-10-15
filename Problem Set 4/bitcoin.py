import requests
import sys
import json
def main():
    if len(sys.argv)==2:
        try:
            n=float(sys.argv[1])
            r=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            rate=r.json()['bpi']['USD']['rate']
            amount=float(rate.replace(',',''))*float(n)
            print(f"${amount:,.4f}")
        except ValueError:
            sys.exit('Command-line argument is not a number')
        ...
    elif len(sys.argv)<2:
        sys.exit('Missing Command-Line Argument')
    else:
        sys.exit()

main()