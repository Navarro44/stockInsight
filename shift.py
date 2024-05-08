from bs4 import BeautifulSoup
import os

# Set the directory where you want to start the traversal

root_dir = '/sec-edgar-filings'

netIncome = {}
earningsPerShare = {}

def getInfo(filePath):
    with open(filePath, "r") as f:
        doc = BeautifulSoup(f, 'lxml')

    metadata = doc.find(attrs={"name": "dei:DocumentFiscalYearFocus"})
    if metadata is not None:
        context = metadata["contextref"]
        focusYear = metadata.text
    else:
        context = ""
        focusYear = 0
    
    tag_list = doc.find_all()
    for tag in tag_list:
        if tag.name == 'us-gaap:earningspersharebasic' and context == tag['contextref']:
            try:
                earningsPerShare[int(focusYear)] = float(tag.text)
            except ValueError:
                print("Error")
        if tag.name == 'us-gaap:netincomeloss' and context == tag['contextref']:
            try:
                netIncome[int(focusYear)] = int(tag.text)
            except ValueError:
                print("Error")



    
    
def traversal(ticker):
    directory = "sec-edgar-filings/" + ticker + "/10-K"
    for path, folders, files in os.walk(directory):
        for fileName in files:
            fileStarter, fileExtension = os.path.splitext(fileName)
            if fileExtension == ".txt":
                getInfo(path + "/" + fileName)
            

#grossprofit
#operatingexpenses
#netincomeloss
#earningspersharebasic
#cash








