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
    response = model.generate_content("You are a financial specialist and will analyze the following two dictionaries to determine if the user should invest in the " + ticker + " technology company. The first dictionary represents net income across time: " + str(netIncomeDict) +", and the second represents earnings per share across time: " str(earningsPerShareDict) +  ". First, write a paragraph calculating the growth percentage of both metrics across the years. Then write another paragrahph providing insight about the businesses performance, and a suggestion if the user should invest based on current technological news and trends.")
    return response.text





