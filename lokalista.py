import streamlit as st
import pandas as pd
from streamlit_extras.tags import tagger_component
from streamlit_gsheets import GSheetsConnection
import streamlit_scrollable_textbox as stx

def main_interface():
    plaintext = st.text_input(label="Enter your budget amount", value="600")
    budget = int(plaintext)


    st.markdown("---")
    st.header("Local Produce")
    categories = ["canned goods", "dairy products", "meat", "fish", "vegetables", "fruits", "beverages", "snacks", "condiments", "frozen foods", "baking supplies", "cleaning supplies", "personal care"]
    
    rows = 5
    cols = st.columns(3)
    selected_categories = {}
    for i in range(rows):
        for j in range(3):
            index = i * 3 + j
            if index < len(categories):
                selected_categories[categories[index]] = cols[j].checkbox(categories[index])

    st.button("Submit", key="btn1")

    st.markdown("---")
    st.header("Recommended")
    
    df = gsheet()
    recommended_list = ""
    total_price = 0
    for row in df.itertuples():
        if total_price + int(row.price) <= budget:
            recommended_list += f"{row.market}  ||  {row.commodity}  ||  {row.price}\n"
            total_price += int(row.price)
    stx.scrollableTextbox(recommended_list, height=300)

    st.subheader("Total Price: " + str(total_price))

    

    st.button("Save", key="btn2")
    
def gsheet():   
    url = "https://docs.google.com/spreadsheets/d/1h2MKH4nEekEWF_Ad3sbhhVPQC8UCQ-m9lVLkDyfaa0s/edit#gid=0"
    conn = st.connection("gsheets", type=GSheetsConnection)
    data = conn.read(spreadsheet=url)
    return data

def notion():
    pass

def generate():
    pass
    
main_interface()

