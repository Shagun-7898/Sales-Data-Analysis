import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel('Online Retail.xlsx')

print("Original dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

# Data Cleaning
# Remove rows with missing values
df_clean = df.dropna()

# Remove rows with quantity less than 1 (returns/cancellations)
df_clean = df_clean[df_clean['Quantity'] > 0]

# Remove rows with price of 0
df_clean = df_clean[df_clean['Price'] > 0]

# Calculate total sales for each row
df_clean['TotalSales'] = df_clean['Quantity'] * df_clean['Price']

print("\n✓ Data Cleaned!")
print(f"Original rows: {len(df)}")
print(f"Cleaned rows: {len(df_clean)}")
print(f"Removed: {len(df) - len(df_clean)} bad rows")

# Analysis 1: Top 10 Products by Revenue
print("\n" + "="*50)
print("TOP 10 PRODUCTS BY REVENUE")
print("="*50)
top_products = df_clean.groupby('Description')['TotalSales'].sum().sort_values(ascending=False).head(10)
print(top_products)

# Analysis 2: Total Sales by Country
print("\n" + "="*50)
print("TOP 10 COUNTRIES BY SALES")
print("="*50)
top_countries = df_clean.groupby('Country')['TotalSales'].sum().sort_values(ascending=False).head(10)
print(top_countries)

# Create Visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Chart 1: Top 10 Products
top_products.plot(kind='barh', ax=axes[0, 0], color='steelblue')
axes[0, 0].set_title('Top 10 Products by Revenue', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Total Sales')

# Chart 2: Top 10 Countries
top_countries.plot(kind='bar', ax=axes[0, 1], color='coral')
axes[0, 1].set_title('Top 10 Countries by Sales', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Country')
axes[0, 1].tick_params(axis='x', rotation=45)

# Chart 3: Sales Distribution
axes[1, 0].hist(df_clean['TotalSales'], bins=50, color='purple', alpha=0.7)
axes[1, 0].set_title('Sales Amount Distribution', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Sale Amount')
axes[1, 0].set_ylabel('Frequency')

# Chart 4: Quantity vs Price Scatter
axes[1, 1].scatter(df_clean['Quantity'], df_clean['Price'], alpha=0.5, s=10, color='green')
axes[1, 1].set_title('Quantity vs Price', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Quantity')
axes[1, 1].set_ylabel('Price')

plt.tight_layout()
plt.savefig('sales_analysis.png', dpi=300, bbox_inches='tight')
print("\n✓ Visualization saved as 'sales_analysis.png'")
plt.show()