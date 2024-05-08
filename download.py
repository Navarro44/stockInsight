from sec_edgar_downloader import Downloader
import os

start_date = "1995-01-01"

#Function to download documents only if they have not been downloaded yet. In my case, I uploaded all the necessary documents to github so they could be processed through the functional website, however, this script still serves if I were running it locally, and inputted any ticker value.

def downloadDocuments(ticker):
    directory = "sec-edgar-filings/"
    exists = os.path.exists(directory + "/" + ticker)
    if not exists:
        dl = Downloader("Personal", "jorgenavarrogracia@gmail.com")
        dl.get("10-K", ticker, after=start_date)








