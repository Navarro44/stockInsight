import pathlib
import textwrap
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def getText(userKey, ticker, netIncomeDict, earningsPerShareDict):
    genai.configure(api_key=userKey)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("You are a financial specialist and will analyze the following two dictionaries to determine if the user should invest in the " + ticker + " company. The first dictionary represents net income across time, and the second represents earnings per share across time. Write a paragraph providing insight and calculating the following years net income, and earnings per share." + str(netIncomeDict) + ", " + str(earningsPerShareDict))
    return to_markdown(response.rext)





