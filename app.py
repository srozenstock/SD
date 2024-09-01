import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset using a relative path
df = pd.read_csv('vehicles_us.csv')

# Creating the header
st.header("Car Sales Dashboard")

# Data viewer
st.subheader('Dataset Viewer')
st.write(df)

# Vehicle types by manufacturer with toggling
st.subheader('Vehicle Types by Manufacturer')

# Multi-select for manufacturers
manufacturers = st.multiselect('Select manufacturers', df['manufacturer'].unique(), default=df['manufacturer'].unique())

# Filter the dataframe by selected manufacturers
filtered_df = df[df['manufacturer'].isin(manufacturers)]

# Plot vehicle types by manufacturer
fig1 = px.bar(filtered_df, x='manufacturer', color='type', title="Vehicle Types by Manufacturer")
st.plotly_chart(fig1)

# Histogram of condition vs. model year
st.subheader('Condition vs. Model Year')

# Dropdown for condition
condition = st.selectbox('Select condition', df['condition'].unique())

# Filter dataframe by selected condition
condition_df = df[df['condition'] == condition]

# Plot histogram of condition vs. model year
fig2 = px.histogram(condition_df, x='model_year', color='condition', title=f"Model Year Distribution for {condition} Condition")
st.plotly_chart(fig2)

# Price comparison between two manufacturers
st.subheader('Compare Prices Between Two Manufacturers')

# Dropdowns for two manufacturers
manufacturer_1 = st.selectbox('Select Manufacturer 1', df['manufacturer'].unique())
manufacturer_2 = st.selectbox('Select Manufacturer 2', df['manufacturer'].unique())

# Filter dataframe for both manufacturers
df_1 = df[df['manufacturer'] == manufacturer_1]
df_2 = df[df['manufacturer'] == manufacturer_2]

# Concatenate the two dataframes for comparison
df_comparison = pd.concat([df_1.assign(manufacturer=manufacturer_1), df_2.assign(manufacturer=manufacturer_2)])

# Plot histogram comparing prices
fig3 = px.histogram(df_comparison, x='price', color='manufacturer', title=f"Price Comparison: {manufacturer_1} vs {manufacturer_2}")
st.plotly_chart(fig3)



