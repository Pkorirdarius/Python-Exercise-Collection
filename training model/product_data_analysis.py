import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Step 1: Web Scraping
def scrape_data(url):
    """Scrapes product data from the specified URL."""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract product data (update selectors based on the retailer's HTML structure)
        products = []
        for product in soup.select(".product-item"):  # Example selector
            name = product.select_one(".product-name").get_text(strip=True) if product.select_one(".product-name") else None
            category = product.select_one(".product-category").get_text(strip=True) if product.select_one(".product-category") else None
            price = product.select_one(".product-price").get_text(strip=True) if product.select_one(".product-price") else None
            availability = product.select_one(".availability-status").get_text(strip=True) if product.select_one(".availability-status") else None
            promotion = product.select_one(".promotion-details").get_text(strip=True) if product.select_one(".promotion-details") else None
            
            products.append({
                "Name": name,
                "Category": category,
                "Price": price,
                "Availability": availability,
                "Promotion": promotion
            })
        
        return pd.DataFrame(products)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return pd.DataFrame()

# URL passing the URL to the function
url = ""
data = scrape_data(url)

# Step 2: Data Cleaning
def clean_data(df):
    """Cleans and standardizes the scraped data."""
    # Drop rows with missing essential data
    df.dropna(subset=["Name", "Price", "Category"], inplace=True)
    
    # Standardize text fields
    df["Name"] = df["Name"].str.strip().str.title()
    df["Category"] = df["Category"].str.strip().str.title()
    
    # Convert price to numeric (assuming price includes a currency symbol)
    df["Price"] = df["Price"].str.replace(r"[^0-9.]", "", regex=True).astype(float)
    
    return df

cleaned_data = clean_data(data)

# Step 3: Data Transformation
def transform_data(df):
    """Transforms data for hierarchical categorization."""
    # Split categories into hierarchical levels and concatenates them to the original DataFrame.
    category_hierarchy = df["Category"].str.split(">", expand=True)
    category_hierarchy.columns = ["Category_Level1", "Category_Level2", "Category_Level3"]
    
    df = pd.concat([df, category_hierarchy], axis=1)
    return df

transformed_data = transform_data(cleaned_data)

# Step 4: Data Analysis and Visualization

def analyze_and_visualize(df):
    """Performs EDA and visualizes the data."""
    # Average pricing per category
    avg_pricing = df.groupby("Category_Level1", as_index= False)["Price"].mean()
    fig1 = px.bar(avg_pricing, x="Category_Level1", y="Price", title="Average Pricing by Category")
    fig1.show()

    # Availability trends
    availability_trends = df["Availability"].value_counts().reset_index()
    availability_trends.columns = ["Availability", "Count"]
    fig2 = px.pie(availability_trends, names="Availability", values="Count", title="Product Availability Distribution")
    fig2.show()

    # Promotional patterns
    promotion_counts = df["Promotion"].value_counts().reset_index()
    promotion_counts.columns = ["Promotion", "Count"]
    fig3 = px.bar(promotion_counts, x="Promotion", y="Count", title="Promotional Pattern Insights")
    fig3.show()

analyze_and_visualize(transformed_data)
