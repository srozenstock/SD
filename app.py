import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Preprocessing
# Fill missing values
df['model_year'] = df['model_year'].fillna(df['model_year'].median())
df['cylinders'] = df['cylinders'].fillna(df['cylinders'].median())
df['odometer'] = df['odometer'].fillna(df['odometer'].median())

# Drop duplicates
df = df.drop_duplicates()

# Create the manufacturer column
df['manufacturer'] = df['model'].apply(lambda x: x.split(' ')[0])

# Now you can proceed to create your visualizations and app components
st.title('Vehicle Data Viewer')

# Example of displaying the data
st.write(df.head())

# Vehicle types by manufacturer
manufacturers = st.multiselect('Select Manufacturers', df['manufacturer'].unique())
filtered_df = df[df['manufacturer'].isin(manufacturers)]
fig = px.histogram(filtered_df, x='type', color='manufacturer', title='Vehicle Types by Manufacturer')
st.plotly_chart(fig)

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



