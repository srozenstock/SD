import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(r'C:\Users\simon\OneDrive\Desktop\project\vehicles_us.csv')

# Creating the header
st.header("Car Sales Dashboard")

# Creating the Histogram
st.subheader("Distribution of Car Prices")
fig = px.histogram(df, x='price', nbins=50)
st.plotly_chart(fig)

# Creating the Scatter Plot
st.subheader("Model Year vs. Price")
fig = px.scatter(df, x='model_year', y='price', color='condition', hover_data=['model'])
st.plotly_chart(fig)

# Checking for filtering
if st.checkbox("Show cars from 2010 onwards"):
    df_filtered = df[df['model_year'] >= 2010]
else:
    df_filtered = df

st.subheader("Filtered Model Year vs. Price")
fig = px.scatter(df_filtered, x='model_year', y='price', color='condition', hover_data=['model'])
st.plotly_chart(fig)

