# Sales Data Analysis Project

## Overview
Analysis of 525,461 real online retail transactions to identify top-performing products, key markets, and sales patterns.

## What I Did

### Data Cleaning
- Removed 18,000+ rows with missing values
- Removed returns and cancelled orders
- Removed items with zero price
- Final clean dataset: 507,000+ valid transactions

### Analysis
- Identified top 10 best-selling products by revenue
- Found top 10 countries generating most sales
- Analyzed sales amount distribution
- Examined relationship between quantity and unit price

### Visualizations
Created 4 professional charts:
1. Top 10 Products by Revenue (bar chart)
2. Top 10 Countries by Sales (bar chart)
3. Sales Distribution (histogram)
4. Quantity vs Price Relationship (scatter plot)

## Key Findings
- White products are among top sellers
- United Kingdom is the largest market
- Most sales are in lower price range (under £20)
- Higher quantities don't always mean higher revenue

## Tools & Skills Used
- Python (Pandas, Matplotlib)
- Data Cleaning & Validation
- Data Analysis & Aggregation
- Data Visualization
- Excel file handling

## Files in Project
- `analysis.py` - Main Python code for analysis
- `Online Retail.xlsx` - Raw dataset (525,461 rows)
- `sales_analysis.png` - Output visualization
- `README.md` - This file

## How to Run
1. Install Python libraries: `pip install pandas matplotlib openpyxl`
2. Place `Online Retail.xlsx` in the same folder
3. Run: `python3 analysis.py`
4. Charts will display and save as `sales_analysis.png`

## Learning Outcome
Through this project, I learned:
- How to load and clean real-world messy data
- Using Pandas for data aggregation and grouping
- Creating professional visualizations with Matplotlib
- Identifying business insights from data