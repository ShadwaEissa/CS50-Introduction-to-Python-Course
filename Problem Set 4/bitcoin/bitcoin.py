import sys
import requests

if len(sys.argv) == 1:
    sys.exit("Missing command line argument")
elif len(sys.argv) == 2 and sys.argv[1].isalpha():
        sys.exit("Command line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    file = response.json()
    rate = file["bpi"]["USD"]["rate_float"]
    amount = float(rate) * float(sys.argv[1])
    print(f"${amount:,.4f}")
except requests.RequestException:
    print("RequestException")
    sys.exit()
