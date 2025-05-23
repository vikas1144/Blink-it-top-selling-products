# 🛒 Blinkit – Top Selling Products Analysis

An interactive dashboard built using **Python**, **Pandas**, **Plotly**, and **Streamlit** to analyze and visualize the top-selling products on Blinkit, a popular quick-commerce grocery delivery platform in India.

## 📌 Project Overview

This project transforms Blinkit's product dataset into actionable insights through dynamic visualizations. Customers can explore trending products, while businesses can use the dashboard for inventory planning, promotional strategies, and performance tracking.

The dashboard includes features such as:
- Ranking of top-selling and highest-rated products
- Category-wise sales distribution
- Price vs Rating Count analysis
- Interactive filters for personalized exploration

## 📊 Features

- View top-selling products based on rating count (used as a sales proxy)
- Discover the highest-rated products across categories
- Explore sales distribution with pie charts and bar graphs
- Understand the relationship between price and product popularity
- Filter products by category through an intuitive sidebar

## 🧰 Tools and Technologies

| Tool           | Purpose                                      |
|----------------|----------------------------------------------|
| Python         | Core programming language                    |
| Pandas         | Data loading, cleaning, and manipulation     |
| Plotly         | Interactive data visualizations              |
| Streamlit      | Dashboard development and deployment         |
| CSV            | Data source format                           |
| Git & GitHub   | Version control and collaboration            |

## 📁 Dataset Description

The dataset includes product-level information scraped or simulated from Blinkit listings:

| Column Name        | Description                                      |
|--------------------|--------------------------------------------------|
| `product_id`       | Unique product identifier                        |
| `product_name`     | Name of the product                              |
| `category`         | Product category (Snacks, Beverages, etc.)       |
| `discounted_price` | Final selling price                              |
| `actual_price`     | Original price before discount                   |
| `discount_percentage` | % Discount on product                        |
| `rating`           | Average user rating (0–5 scale)                  |
| `rating_count`     | Number of user ratings (used as a sales metric)  |
| `about_product`    | Description of the product                       |

## 🧪 Methodology

1. **Data Cleaning** – Missing values and type conversions handled with Pandas.
2. **Exploratory Analysis** – Summary stats and value distributions examined.
3. **Data Aggregation** – Products ranked by rating count and average rating.
4. **Visualization** – Plotly used to create:
   - Bar charts for top products
   - Pie charts for category analysis
   - Scatter plots for price–rating relationships
5. **Dashboard Deployment** – Built with Streamlit and deployed locally/cloud.

## 🚀 Running the App Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/blinkit-top-products.git
   cd blinkit-top-products

pip install -r requirements.txt


streamlit run main.py

📈 Sample Visualizations
🏆 Top 10 products by sales (rating count)
🌟 Highest-rated products
📦 Category-wise distribution
💰 Price vs. rating count scatter plot
