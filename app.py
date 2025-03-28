import pandas as pd
import streamlit as st
import plotly.express as px

def load_data():
   return pd.read_csv("vehicles_us.csv")
    
vehicles_us = load_data()

st.title("Car Dealership Explorer")

st.markdown("""
This App perfoms a simple comparation in between car models and prices
""")

selected_model = st.selectbox("Select a model:", ['All'] + sorted(vehicles_us['model'].unique()))
selected_condition = st.multiselect("Select condition:", vehicles_us['condition'].unique())
filtered_cars_df = vehicles_us
if selected_model != "All":
    filtered_cars_df = filtered_cars_df[filtered_cars_df['model'] == selected_model]
if selected_condition:
    filtered_cars_df = filtered_cars_df[filtered_cars_df['condition'].isin(selected_condition)]
st.write(filtered_cars_df)

#Histogram: Distribution model_year 
fig_hist_year = px.histogram(
    filtered_cars_df,
    x="model_year",  
    nbins=20,  
    title="Distribution of Vehicles by Model Year",
    labels={"model_year": "Model Year"},
)
st.plotly_chart(fig_hist_year)

#Scatterplot: price vs model
fig_scatter_model = px.scatter(
    filtered_cars_df,
    x="model",  
    y="price",  
    color="condition",  
    title="Price vs Model",
    labels={"price": "Price ($)", "model": "Model", "condition": "Condition"},
    opacity=0.6  
)
st.plotly_chart(fig_scatter_model)

#Histogram: price vs condition 
fig_hist_condition = px.histogram(
    filtered_cars_df, 
    x="price",  
    nbins=30,  
    color="condition",  
    title="Price Distribution by Condition",
    labels={"price": "Price ($)", "condition": "Condition"},
)
st.plotly_chart(fig_hist_condition)

# Scatter Plot: Price vs Condition
fig_scatter = px.scatter(
    filtered_cars_df, 
    x="condition", 
    y="price", 
    color="condition",  
    title="Price vs Condition",
    labels={"price": "Price ($)", "condition": "Condition"},
    opacity=0.6
)
st.plotly_chart(fig_scatter)
