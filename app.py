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

# Creating the header
st.header("Car Sales Dashboard")

# Data viewer
st.subheader('Dataset Viewer')
st.write(df)

# 2. Vehicle Types by Manufacturer
st.subheader('Vehicle Types by Manufacturer')

# Multi-select for manufacturers
manufacturers = st.multiselect('Select Manufacturers', df['manufacturer'].unique(), default=df['manufacturer'].unique())

# Filter data based on selected manufacturers
filtered_df = df[df['manufacturer'].isin(manufacturers)]

# Plot vehicle types by manufacturer
fig1 = px.bar(filtered_df, x='manufacturer', color='type', 
              title="Vehicle Types by Manufacturer", 
              category_orders={"type": df['type'].value_counts().index},
              barmode='stack')

# Update layout to make the chart more readable
fig1.update_layout(xaxis={'categoryorder':'total descending'}, 
                   yaxis_title="Count", 
                   xaxis_title="Manufacturer")

st.plotly_chart(fig1)

# 3. Histogram of Condition vs. Model Year
st.subheader('Condition vs. Model Year')

# Create a stacked histogram of condition vs. model year
fig2 = px.histogram(df, x='model_year', color='condition', 
                    title="Histogram of Condition vs. Model Year", 
                    nbins=30,  # Adjust the number of bins if necessary
                    barmode='stack')

# Update layout for better readability
fig2.update_layout(yaxis_title="Count", xaxis_title="Model Year", 
                   xaxis=dict(tickmode='linear'),  # Ensure all model years are shown
                   legend_title_text="Condition")

st.plotly_chart(fig2)

# 4. Price Comparison Between Two Manufacturers
st.subheader('Compare Price Distribution Between Manufacturers')

# Dropdowns for selecting two manufacturers
manufacturer_1 = st.selectbox('Select Manufacturer 1', df['manufacturer'].unique(), key='manufacturer1')
manufacturer_2 = st.selectbox('Select Manufacturer 2', df['manufacturer'].unique(), key='manufacturer2')

# Option to normalize histogram
normalize = st.checkbox('Normalize histogram', value=False)

# Filter data based on selected manufacturers
df_1 = df[df['manufacturer'] == manufacturer_1]
df_2 = df[df['manufacturer'] == manufacturer_2]

# Concatenate data for comparison
df_comparison = pd.concat([df_1.assign(selected_manufacturer=manufacturer_1), df_2.assign(selected_manufacturer=manufacturer_2)])

# Plot histogram comparing prices
fig3 = px.histogram(df_comparison, x='price', color='selected_manufacturer', 
                    title=f"Price Comparison: {manufacturer_1} vs {manufacturer_2}",
                    histnorm='percent' if normalize else None, 
                    nbins=30)

fig3.update_layout(yaxis_title="Percent" if normalize else "Count", 
                   xaxis_title="Price", 
                   barmode='overlay')

st.plotly_chart(fig3)

