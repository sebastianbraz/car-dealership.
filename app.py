import pandas as pd
import streamlit as st
import plotly.express as px

def load_csv_data(vehicles_us):
    vehicles_us = pd.read_csv('/Users/sebastiangarcia/GitHub/project-/vehicles_us.csv')
    
if __name__ == "__main__":
    load_csv_data('/Users/sebastiangarcia/GitHub/project-/vehicles_us.csv')

st.header("Car Dealership Explorer")

st.markdown("""
This App perfoms a simple comparation in between models and prices
""")
