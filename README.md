# stockInsight

The link to the functioning website is: https://jmnstockanalyzer.streamlit.app

This purpose of this project was to analyze 10k filings from different companies registered in the SEC, extract critical information, and create an insight to that information using a LLM. In my implementation, I chose to look at net income, and revenue per share of Apple, Tesla, and Microsoft. The reason for this decision is included in the webpage.
 
The tools I used where:
1.) Beautiful soup to traverse the XBLR documents and retrieve necessary information.
2.) Streamlit, to facilitate the creation of the front-end website by using python, and the creation of the graphs.
3.) Llama2 as the LLM model to produce the text output, however, I had some trouble since I ran out of the tokens.
4.) Sec-edgar-downloader, to download the needed SEC 10-k filings.
5.) Pandas, to transform the information models into the functioning graphs. 

Notes for future development:
One of the biggest challenges I had was the fact that the SEC changed its format on 2019. I used the xml parser Beautiful Soup to look for specific tags to obtain the fiscal year and context tags. From 2019 to the present day, the tags had an attribute called name="dei:DocumentFiscalYearFocus" which I could look for using the Beautiful Soup functions. With this, I was able to obtain the fiscal year, and context tag information so I could compare and make sure the information belonged to that year. However, from 2019 to the past, the tags did not have the name attribute and were written like the following: <dei:DocumentFiscalYearFocus. Beautiful Soup could not trace this if it did not have an attribute, this is why I was not able to graph the total information previous to 2019. 
Additionally, I also had trouble implementing the LLM based on the fact that Iit was a paid service. It was working perfectly before I used up all of my tokens, and could not succesfully print the insight information. 
