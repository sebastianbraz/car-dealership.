import pandas as pd
import streamlit as st
import plotly.express as px

def load_csv_data(vehicles_us):
    vehicles_us = pd.read_csv('vehicles_us.csv')
    
load_csv_data('vehicles_us.csv')


st.title("Car Dealership Explorer")

st.markdown("""
This App perfoms a simple comparation in between car models and prices
""")
