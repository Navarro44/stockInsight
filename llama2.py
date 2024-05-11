""" import replicate
import os

os.environ["REPLICATE_API_TOKEN"] = "r8_3NMlH8vBs17DcP9XQmqDibFKjtFZkBa4clYoy"
api = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])

def getOutput(netIncomeDict, earningsPerShareDict, ticker):
    text = ""
    for event in replicate.stream(
        "meta/meta-llama-3-70b-instruct",
        input={
            "prompt": "You are a financial specialist and will analyze the following two dictionaries to determine if the user should invest in the " + ticker + " company. The first dictionary represents net income across time, and the second represents earnings per share across time. Write a paragraph providing insight and calculating the following years net income, and earnings per share." + str(netIncomeDict) + ", " + str(earningsPerShareDict),
        },
        ):
            text += str(event)
    print(text)

income = {2020: 100, 2021: 120, 2022: 200, 2023: 250}
share = {2020: 3, 2021: 2.5, 2022: 3.2, 2023: 3.4}

getOutput(income, share, "JOEL") """



