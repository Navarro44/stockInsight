import replicate
import mySite

def getOutput(myNumber):
    for event in replicate.stream(
        "meta/llama-2-70b-chat",
        input={
            "prompt": "Create a poem about the number" + str(myNumber) + "."
        },
    ):
        print(str(event), end="")


""" def downloadDocuments(ticker):
    directory = "sec-edgar-filings/"
    for path, folders, files in os.walk(directory):
        for folder in folders:
            if folder == ticker:
                return
    dl = Downloader("Personal", "jorgenavarrogracia@gmail.com")
    dl.get("10-K", ticker, after=start_date) """