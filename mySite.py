import streamlit as st
import os
import pandas as pd
import numpy as np
import altair as alt
import shift
import download
import llama2

def menu(name):
    st.title(name) # NEW
    if name == "Explanation":
        st.header("_Process and Research_")
        filing_image = os.path.join("images/10k.png")
        st.image(filing_image, width=600)
        st.write("A 10-K filing is an annual report that publicly traded companies are required to submit to the U.S. Securities and Exchange Commission (SEC). The 10-K provides a comprehensive overview of the company's business, financial performance, and operations for the previous fiscal year. It serves as a crucial source of information for investors, analysts, and other stakeholders, offering valuable insights into the company's financial health, competitive position, and future prospects. The 10-K filing provides value to investors and other stakeholders by offering transparency into the company's operations, financial performance, and risk factors. It serves as a comprehensive source of information for making informed investment decisions, assessing the company's competitive position, and evaluating its long-term prospects.")

        st.divider()
        st.header("_Analytical Decisions_")
        analysis_image = os.path.join("images/analysis.png")
        st.image(analysis_image, width=600)
        st.write("In this project, I decided to specifically take a look at the net income and basic earnings per share metrics. To me, these were the most important factors into taking consideration whether to invest on a company or not. Net income representes the amount of money left over after the business: invested into research, generated its products, paid its providers, rewarded its workers, financed its banks, and dished out government taxes. This amount is the money that belongs to the company and its shareholders, thus, based on this number, shareholders make the decision to reinvest or distribute dividends. Earnings per share represents the company's profitability by showing how much money a business makes for each share of its stock, in other words, how much the investor benefits from having a stock in the business. In the Start tab to the left, you will be able to see the progression of these two for a company of your choosing, and be provided with a LLM response providing insight into the matter.")

    elif name == "Start":
        llmtext = "LLM Token Limit Reached"
        st.header("Get Started")
        with st.form("my_form"):
            st.write("Calculation:")
            chosenTicker = st.radio("Choose your desired stock: ",["TSLA", "AAPL", "MSFT"])
            submitted = st.form_submit_button("Submit")
            if submitted:
                download.downloadDocuments(chosenTicker)
                shift.traversal(chosenTicker)
                #llmtext += llama2.getOutput(shift.netIncome, shift.earningsPerShare, chosenTicker)

            
        incomeData = shift.netIncome
        # Convert the dictionary to a DataFrame
        data = pd.DataFrame.from_dict(incomeData, orient='index', columns=['Amount'])
        data.index.name = 'Year'
        data.reset_index(inplace=True)
        # Plot the chart
        st.bar_chart(data.set_index('Year'))
        st.subheader('Net Income Across Time')

        earningsData = shift.earningsPerShare
        # Convert the dictionary to a DataFrame
        data2 = pd.DataFrame.from_dict(earningsData, orient='index', columns=['Amount'])
        data2.index.name = 'Year'
        data2.reset_index(inplace=True)
        # Plot the chart
        st.bar_chart(data2.set_index('Year'))
        st.subheader('Earnings Per Share Across Time')

        st.divider()
        st.subheader("Insight from LLM")
        st.write(llmtext)
        
# Create navigation sidebar
st.sidebar.title("Stock Insight")

# NEW
menuChoice = st.sidebar.radio("Learn about the process and get started.", ["Explanation", "Start"], key = "<uniquevalueofsomesort>")
if menuChoice == "Explanation":
    menu("Explanation")
elif menuChoice == "Start":
    menu("Start")