from bs4 import BeautifulSoup
import os

# Set the directory where you want to start the traversal
root_dir = '/sec-edgar-filings'

netIncome = {}
earningsPerShare = {}

#Function to retrieve information
def getInfo(filePath):
    with open(filePath, "r") as f:
        doc = BeautifulSoup(f, 'lxml')

    #Finds the Document Fiscal Year tag to obtain the year, and context data to then compare later on.
    metadata = doc.find(attrs={"name": "dei:DocumentFiscalYearFocus"})
    if metadata is not None:
        context = metadata["contextref"]
        focusYear = metadata.text
    else:
        context = ""
        focusYear = 0
    
    tag_list = doc.find_all()
    for tag in tag_list:
        #For loop that searches for the tags pertaining to the information I wanted: earnings per share, and net income loss, and makes sure they belong to that year by comparing their context tags.
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
    #Traverses through the different folders, and gets the necessary info once it reaches a .txt file.
    directory = "sec-edgar-filings/" + ticker + "/10-K"
    for path, folders, files in os.walk(directory):
        for fileName in files:
            fileStarter, fileExtension = os.path.splitext(fileName)
            if fileExtension == ".txt":
                getInfo(path + "/" + fileName)
            
