from tkinter import *
import requests
import json
import sqlite3

pycrypto = Tk()
pycrypto.title("My Crypto Portfolio")
pycrypto.iconbitmap("favicon.ico")

con = sqlite3.connect("coin.db")
cursorObj = con.cursor()

cursorObj.execute("CREATE TABLE IF NOT EXISTS coin(id INTEGER PRIMARY KEY, symbol TEXT, amount INTEGER, price REAL)")
con.commit()


def my_portfolio():
    # gets the data from the api request
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=089354da-895c-4c75-9fbe-91580125ab3c")

    # converts the data to a parseable format
    api = json.loads(api_request.content)

    cursorObj.execute("SELECT * FROM coin")
    coins = cursorObj.fetchall()

    def font_color(amount):
        if amount >= 0:
            return "green"
        else:
            return "red"

    total_pl = 0
    coin_row=1
    total_current_value = 0
    total_amount_paid = 0

    for i in range(len(api["data"])):
        for coin in coins:
            if api["data"][i]["symbol"] == coin[1]:
                total_paid = coin[2]*coin[3]
                current_value = api["data"][i]["quote"]["USD"]["price"]*coin[2]
                pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin[3]
                total_pl_coin = pl_percoin * coin[2]

                total_pl += total_pl_coin
                total_amount_paid += total_paid
                total_current_value += current_value


                name = Label(pycrypto, text=api["data"][i]["symbol"], bg="white", fg="gray", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
                name.grid(row=coin_row, column=0, sticky=N+S+E+W)

                price = Label(pycrypto, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="white", fg="gray", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
                price.grid(row=coin_row, column=1, sticky=N+S+E+W)

                no_coins = Label(pycrypto, text=coin[2], bg="white", fg="gray", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
                no_coins.grid(row=coin_row, column=2, sticky=N+S+E+W)

                amount_paid = Label(pycrypto, text="${0:.2f}".format(total_paid), bg="white", fg="gray", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
                amount_paid.grid(row=coin_row, column=3, sticky=N+S+E+W)

                current_val = Label(pycrypto, text="${0:.2f}".format(current_value), bg="white", fg="gray", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
                current_val.grid(row=coin_row, column=4, sticky=N+S+E+W)

                pl_coin = Label(pycrypto, text="${0:.2f}".format(pl_percoin), bg="white", fg=font_color(float("{0:.2f}".format(pl_percoin))), font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
                pl_coin.grid(row=coin_row, column=5, sticky=N+S+E+W)

                totalpl = Label(pycrypto, text="${0:.2f}".format(total_pl_coin), bg="white", fg=font_color(float("{0:.2f}".format(total_pl_coin))), font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
                totalpl.grid(row=coin_row, column=6, sticky=N+S+E+W)

                coin_row += 1

    totalap = Label(pycrypto, text="${0:.2f}".format(total_amount_paid), bg="white", fg="gray", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
    totalap.grid(row=coin_row, column=3, sticky=N+S+E+W)


    totalcv = Label(pycrypto, text="${0:.2f}".format(total_current_value), bg="white", fg="gray", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
    totalcv.grid(row=coin_row, column=4, sticky=N+S+E+W)

    totalpl_portfolio = Label(pycrypto, text="${0:.2f}".format(total_pl), bg="white", fg=font_color(float("{0:.2f}".format(total_pl))), font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
    totalpl_portfolio.grid(row=coin_row, column=6, sticky=N+S+E+W)

    api = ""

    refresh = Button(pycrypto, text="Refresh", bg="#152E54", command=my_portfolio, cursor="exchange", fg="white", font="Lato 10", padx="5", pady="5", borderwidth=2, relief="groove")
    refresh.grid(row=coin_row+1, column=6, sticky=N+S+E+W)

def app_header():
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

cursorObj.close()
con.close()
print("Program Completed")
