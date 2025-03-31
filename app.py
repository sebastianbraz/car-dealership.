import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

def load_data():
   return pd.read_csv("vehicles_us.csv")
    
vehicles_us = load_data()

#Filling missing values: 
#Model_year
vehicles_us['model_year'] = vehicles_us.groupby('model')['model_year'].transform(lambda x: x.fillna(x.median()))
vehicles_us['model_year'].fillna(vehicles_us['model_year'].median(), inplace=True)
#Removing Outliers Model_year.
Q1 = vehicles_us['model_year'].quantile(0.25)
Q3 = vehicles_us['model_year'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

vehicles_us = vehicles_us[(vehicles_us['model_year'] >= lower_bound) & (vehicles_us['model_year'] <= upper_bound)]

#Removing Outliers Price
Q1 = vehicles_us['price'].quantile(0.25)
Q3 = vehicles_us['price'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

vehicles_us = vehicles_us[(vehicles_us['price'] >= lower_bound) & (vehicles_us['price'] <= upper_bound)]

#Cylinders
vehicles_us['cylinders'] = vehicles_us.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.median()))
vehicles_us['cylinders'].fillna(vehicles_us['cylinders'].median(), inplace=True)

#Odometer
vehicles_us['odometer'] = vehicles_us.groupby(['model_year', 'model'])['odometer'].transform(lambda x: x.fillna(x.mean()))
vehicles_us["odometer"].fillna(vehicles_us["odometer"].mean(), inplace=True)

#Color 
vehicles_us['paint_color'] = vehicles_us['paint_color'].fillna('No info')

#4wd
vehicles_us['is_4wd'] = vehicles_us.groupby('model')['is_4wd'].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else 0))

st.title("Car Dealership Explorer")

st.markdown("""
This App perfoms a simple comparation in between car models and prices base on certain conditions
""")

#selected_model = st.selectbox("Select a model:", ['All'] + sorted(vehicles_us['model'].unique()))
#selected_condition = st.multiselect("Select condition:", vehicles_us['condition'].unique())
#filtered_cars_df = vehicles_us
#if selected_model != "All":
#    filtered_cars_df = filtered_cars_df[filtered_cars_df['model'] == selected_model]
#if selected_condition:
#    filtered_cars_df = filtered_cars_df[filtered_cars_df['condition'].isin(selected_condition)]
#st.write(filtered_cars_df.astype(str))

st.header("Price per Model")
#Scatterplot: price vs model
fig_scatter_model = px.scatter(
    filtered_cars_df,
    x="model",  
    y="price",  
    color="condition",  
    labels={"price": "Price ($)", "model": "Model", "condition": "Condition"},
    opacity=0.6  
)
st.plotly_chart(fig_scatter_model)

st.header("Distribution of Vehicles by Year of Manufacture")
#Histogram: Distribution model_year 
fig_hist_year = px.histogram(
    filtered_cars_df,
    x="model_year",  
    nbins=20,  
    labels={"model_year": "Model Year"},
)
st.plotly_chart(fig_hist_year)


st.header("Price Distribution by Condition")
#Histogram: price vs condition 
fig_hist_condition = px.histogram(
    filtered_cars_df, 
    x="price",  
    nbins=30,  
    color="condition",  
    labels={"price": "Price ($)", "condition": "Condition"},
)
st.plotly_chart(fig_hist_condition)

st.header("Price per condition")
# Scatter Plot: Price vs Condition
fig_scatter = px.scatter(
    filtered_cars_df, 
    x="condition", 
    y="price", 
    color="condition",  
    labels={"price": "Price ($)", "condition": "Condition"},
    opacity=0.6
)
st.plotly_chart(fig_scatter)
