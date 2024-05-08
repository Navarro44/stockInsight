from sec_edgar_downloader import Downloader
from bs4 import BeautifulSoup



with open("sec-edgar-filings/AAPL/10-K/0000320193-18-000145/full-submission.txt", "r") as f:
    doc = BeautifulSoup(f, 'lxml')

tag = doc.find_all("DocumentFiscalPeriodFocus")

# Print the tag and its content
print(tag)
# context = metadata["contextref"]
# focusYear = metadata.text

#DocumentFiscalYearFocus

    