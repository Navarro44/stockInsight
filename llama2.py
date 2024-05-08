import replicate
import os

os.environ["REPLICATE_API_TOKEN"] = "r8_LrhfU7BnMOC6zZL72pFdiQoEXtZVN932pd8Bn"
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
    return text





