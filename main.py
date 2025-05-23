import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("blinkit_data.csv")  # Use correct filename
    return df

df = load_data()

# Title and description
st.title("🛒 Blinkit Top Selling Products Dashboard")
st.markdown("""
This dashboard helps customers explore Blinkit's top-selling products.  
Use filters to view insights by category, sales, and ratings.
""")

# Handle missing or inconsistent data
df.dropna(subset=[
    'product_id', 'product_name', 'category', 'discounted_price',
    'actual_price', 'discount_percentage', 'rating', 'rating_count',
    'about_product', 'user_id', 'user_name', 'review_id',
    'review_title', 'review_content', 'img_link', 'product_link'
], inplace=True)

df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce').fillna(0)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce').fillna(0)
df['discounted_price'] = pd.to_numeric(df['discounted_price'], errors='coerce').fillna(0)
df['actual_price'] = pd.to_numeric(df['actual_price'], errors='coerce').fillna(0)

# Data overview
st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# Sidebar filters
st.sidebar.header("🔍 Filter Products")
categories = df['category'].dropna().unique().tolist()
selected_categories = st.sidebar.multiselect("Select Categories", categories, default=categories)

# Filtered dataframe
filtered_df = df[df['category'].isin(selected_categories)]

# Top products by sales (using rating_count as proxy for sales)
st.subheader("🏆 Top Selling Products")
top_sales = df.sort_values(by='rating_count', ascending=False).head(10)
fig1 = px.bar(top_sales, x='rating_count', y='product_name',
              color='category', title="Top 10 Products by Rating Count (Sales Proxy)", orientation='h')
st.plotly_chart(fig1, use_container_width=True)

# Top products by rating
st.subheader("🌟 Highest Rated Products")
top_rated = df.sort_values(by='rating', ascending=False).head(10)
fig2 = px.bar(top_rated, x='rating', y='product_name',
              color='category', title="Top 10 Products by Rating", orientation='h')
st.plotly_chart(fig2, use_container_width=True)

# Category-wise sales distribution
st.subheader("📦 Category-wise Sales Distribution")
category_sales = filtered_df.groupby('category')['rating_count'].sum().reset_index().sort_values(by='rating_count', ascending=False)
fig3 = px.pie(category_sales, names='category', values='rating_count', title="Sales Distribution by Category")
st.plotly_chart(fig3, use_container_width=True)

# Price vs Ratings scatter
st.subheader("💰 Price vs Rating Count")
fig4 = px.scatter(filtered_df, x='discounted_price', y='rating_count',
                  color='category', hover_data=['product_name', 'rating'],
                  title="Discounted Price vs Rating Count")
st.plotly_chart(fig4, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Created for customer insights into Blinkit's best products. 📈")