from tkinter import *
import requests
import json

pycrypto = Tk()
pycrypto.title("My Crypto Portfolio")
pycrypto.iconbitmap("favicon.ico")

def my_portfolio():
    # gets the data from the api request
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=089354da-895c-4c75-9fbe-91580125ab3c")

    # converts the data to a parseable format
    api = json.loads(api_request.content)

    coins = [
        {
            "symbol": "BTC",
            "amount_owned": 2,
            "price_per_coin": 56802.29
        },
        {
            "symbol": "ETH",
            "amount_owned": 100,
            "price_per_coin": 2504.06
        },
        {
            "symbol": "USDT",
            "amount_owned": 75,
            "price_per_coin": 1.00
        },
        {
            "symbol": "BNB",
            "amount_owned": 10,
            "price_per_coin": 477.91
        }
    ]

    total_pl = 0
    coin_row=1
    total_current_value = 0

    for i in range(len(api["data"])):
        for coin in coins:
            if api["data"][i]["symbol"] == coin["symbol"]:
                total_paid = coin["amount_owned"]*coin["price_per_coin"]
                current_value = api["data"][i]["quote"]["USD"]["price"]*coin["amount_owned"]
                pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
                total_pl_coin = pl_percoin * coin["amount_owned"]

                total_pl += total_pl_coin

                name = Label(pycrypto, text=api["data"][i]["symbol"], bg="white", fg="gray", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
                name.grid(row=coin_row, column=0, sticky=N+S+E+W)

                price = Label(pycrypto, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="white", fg="gray", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
                price.grid(row=coin_row, column=1, sticky=N+S+E+W)

                no_coins = Label(pycrypto, text=coin["amount_owned"], bg="white", fg="gray", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
                no_coins.grid(row=coin_row, column=2, sticky=N+S+E+W)

                amount_paid = Label(pycrypto, text="${0:.2f}".format(total_paid), bg="white", fg="gray", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
                amount_paid.grid(row=coin_row, column=3, sticky=N+S+E+W)

                current_val = Label(pycrypto, text="${0:.2f}".format(current_value), bg="white", fg="gray", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
                current_val.grid(row=coin_row, column=4, sticky=N+S+E+W)

                pl_coin = Label(pycrypto, text="${0:.2f}".format(pl_percoin), bg="white", fg="gray", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
                pl_coin.grid(row=coin_row, column=5, sticky=N+S+E+W)

                totalpl = Label(pycrypto, text="${0:.2f}".format(total_pl_coin), bg="white", fg="gray", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
                totalpl.grid(row=coin_row, column=6, sticky=N+S+E+W)

                coin_row+=1

    totalcv = Label(pycrypto, text="${0:.2f}".format(total_current_value), bg="white", fg="gray", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
    totalcv.grid(row=coin_row, column=4, sticky=N+S+E+W)

    totalpl_portfolio = Label(pycrypto, text="${0:.2f}".format(total_pl), bg="white", fg="gray", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
    totalpl_portfolio.grid(row=coin_row, column=6, sticky=N+S+E+W)

name = Label(pycrypto, text="Coin Name", bg="#152E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=0, sticky=N+S+E+W)

price = Label(pycrypto, text="Price", bg="#152E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
price.grid(row=0, column=1, sticky=N+S+E+W)

no_coins = Label(pycrypto, text="Coin Owned", bg="#152E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
no_coins.grid(row=0, column=2, sticky=N+S+E+W)

amount_paid = Label(pycrypto, text="Total Amount Paid", bg="#152E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
amount_paid.grid(row=0, column=3, sticky=N+S+E+W)

current_val = Label(pycrypto, text="Current Value", bg="#152E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
current_val.grid(row=0, column=4, sticky=N+S+E+W)

pl_coin = Label(pycrypto, text="P/L Per Coin", bg="#152E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
pl_coin.grid(row=0, column=5, sticky=N+S+E+W)

totalpl = Label(pycrypto, text="Total P/L With Coin", bg="#152E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
totalpl.grid(row=0, column=6, sticky=N+S+E+W)

my_portfolio()

pycrypto.mainloop()
print("Program Completed")
