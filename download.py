from sec_edgar_downloader import Downloader
import os

start_date = "1995-01-01"

def downloadDocuments(ticker):
    directory = "sec-edgar-filings/"
    exists = os.path.exists(directory + "/" + ticker)
    if not exists:
        dl = Downloader("Personal", "jorgenavarrogracia@gmail.com")
        dl.get("10-K", ticker, after=start_date)








