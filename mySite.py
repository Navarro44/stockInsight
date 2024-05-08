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
        st.write("Brazil is the most successful team in World Cup history, having won the tournament a record five times (1958, 1962, 1970, 1994, and 2002). Their style of play has often been characterized by flair, creativity, and technical skill. Brazil is known for its 'jogo bonito' (beautiful game) approach, emphasizing skillful dribbling, quick passing, and attacking football.")
        st.divider()
        st.header("_Analytical Decisions_")
        analysis_image = os.path.join("images/analysis.png")
        st.image(analysis_image, width=600)
        st.write("Brazil is the most successful team in World Cup history, having won the tournament a record five times (1958, 1962, 1970, 1994, and 2002). Their style of play has often been characterized by flair, creativity, and technical skill. Brazil is known for its 'jogo bonito' (beautiful game) approach, emphasizing skillful dribbling, quick passing, and attacking football.")

    elif name == "Start":
        st.header("Get Started")
        with st.form("my_form"):
            st.write("Calculation:")
            chosenTicker = st.radio("Choose your desired stock: ",["TSLA", "AAPL", "MSFT"])
            submitted = st.form_submit_button("Submit")
            if submitted:
                download.downloadDocuments(chosenTicker)
                shift.traversal(chosenTicker)
            
        stock_data = shift.grossProfit
        # Convert the dictionary to a DataFrame
        data = pd.DataFrame.from_dict(stock_data, orient='index', columns=['Price'])
        data.index.name = 'Year'
        data.reset_index(inplace=True)
        # Plot the chart
        st.subheader('Stock Price by Year')
        st.bar_chart(data.set_index('Year'))


        
# Create navigation sidebar
st.sidebar.title("Stock Insight")

# NEW
menuChoice = st.sidebar.radio("Learn about the process and get started.", ["Explanation", "Start"], key = "<uniquevalueofsomesort>")
if menuChoice == "Explanation":
    menu("Explanation")
elif menuChoice == "Start":
    menu("Start")