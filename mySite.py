import streamlit as st
import os
import pandas as pd
import numpy as np
import altair as alt
import shift
import download
import googleapi

def menu(name):
    if name == "Explanation":
        st.title("Explanation") 
        # Explanation Section
        st.header("_Process and Research_")
        filing_image = os.path.join("images/10k.png")
        st.image(filing_image, width=600)
        st.write("A 10-K filing is an annual report that publicly traded companies are required to submit to the U.S. Securities and Exchange Commission (SEC). The 10-K provides a comprehensive overview of the company's business, financial performance, and operations for the previous fiscal year. It serves as a crucial source of information for investors, analysts, and other stakeholders, offering valuable insights into the company's financial health, competitive position, and future prospects. The 10-K filing provides value to investors and other stakeholders by offering transparency into the company's operations, financial performance, and risk factors. It serves as a comprehensive source of information for making informed investment decisions, assessing the company's competitive position, and evaluating its long-term prospects.")

        st.divider()

        #Analytical Decisions Section
        st.header("_Analytical Decisions_")
        analysis_image = os.path.join("images/analysis.png")
        st.image(analysis_image, width=600)
        st.write("In this project, I decided to specifically take a look at the net income and basic earnings per share metrics. To me, these were the most important factors into taking consideration whether to invest on a company or not. Net income representes the amount of money left over after the business: invested into research, generated its products, paid its providers, rewarded its workers, financed its banks, and dished out government taxes. This amount is the money that belongs to the company and its shareholders, thus, based on this number, shareholders make the decision to reinvest or distribute dividends. Earnings per share represents the company's profitability by showing how much money a business makes for each share of its stock, in other words, how much the investor benefits from having a stock in the business. In the Start tab to the left, you will be able to see the progression of these two for a company of your choosing, and be provided with a LLM response providing insight into the matter.")

    elif name == "Start":
        st.title("Get Started")
        st.subheader("Steps to function:")
        st.write("1.) Input your stock, and click submit.")
        st.write("2.) Wait until program stops running and graphs are published below (It may take some time).")
        st.write("3.) After graphs are published, go to: https://aistudio.google.com/app/apikey, to get your api key and input it to recieve additional insight from Google's Gemini Pro LLM.")
        with st.form("my_form"):
            #Radio buttons so user can choose desired stock.
            chosenTicker = st.radio("Choose your stock: ",["TSLA", "AAPL", "MSFT"])
            submitted = st.form_submit_button("Submit")
            if submitted:
                #If user clicks submit the script will do the following.

                #1.) Download the necessary documents with the ticker input
                download.downloadDocuments(chosenTicker)

                #2.) Traverse throught the companies folders, retrieving the necessary info to build the dictionaries.
                shift.traversal(chosenTicker)

            # Net income across years
            incomeData = shift.netIncome

            # Convert the dictionary to a DataFrame
            data = pd.DataFrame.from_dict(incomeData, orient='index')
            data.index.name = 'Year'
            data.reset_index(inplace=True)
            # Plot the chart
            st.subheader('Net Income Across Time')
            st.bar_chart(data.set_index('Year'))

            #Earning per share across years
            earningsData = shift.earningsPerShare

            # Convert the dictionary to a DataFrame
            data2 = pd.DataFrame.from_dict(earningsData, orient='index', columns=['Amount in USD'])
            data2.index.name = 'Year'
            data2.reset_index(inplace=True)
            # Plot the chart
            st.subheader('Earnings Per Share Across Time')
            st.bar_chart(data2.set_index('Year'))

        st.divider()

        #LLM Output not functional due to tokens
        st.subheader("Insight from LLM")
        llmText = ""
        with st.form("llmForm"):
            #Text input for API key.
            apiKey = st.text_input("Input your API Key: ")
            llmsubmit = st.form_submit_button("Submit")
            if llmsubmit:
                #3.) Use the dictionaries to create llm insight output based on the recollected data.
                llmText = googleapi.getText(apiKey, chosenTicker, incomeData, earningsData)
                st.write(llmText)
        
# Create navigation sidebar
st.sidebar.title("Stock Insight")

#Create choices in sidebar to allow user to switch between tabs.
menuChoice = st.sidebar.radio("Learn about the process and get started.", ["Explanation", "Start"], key = "<uniquevalueofsomesort>")
if menuChoice == "Explanation":
    menu("Explanation")
elif menuChoice == "Start":
    menu("Start")