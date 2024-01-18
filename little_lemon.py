'''
Authored by Tumisang Tshimologo
'''
###################################################################################################################
###################################################################################################################
# IMPORTING LIBRARIES
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
###################################################################################################################
###################################################################################################################
# LOAD DATAFRAME
dataframe = pd.read_csv('C:/Users/cse20-054/Documents/My Projects/DataAnalysis/Python/Little Lemon Project/Little Lemon.csv')
# print(dataframe.head())
###################################################################################################################
###################################################################################################################
# DATA DESCRPTION
print('DATA INFORMATION: ', dataframe.info())
print('DATA DESCPRITION: ', dataframe.describe())
print('DATA SHAPE: ', dataframe.shape)
###################################################################################################################
###################################################################################################################
# DATA CLEANING
no_null_dataframe = dataframe.dropna(axis=0)
# print('Null values dropped!')

no_repeating_dataset = no_null_dataframe.drop_duplicates()
# print('Duplicates dropped!')

no_repeating_dataset_lower = no_repeating_dataset.applymap(lambda x: x.lower() if isinstance(x, str) else x)
# print('String values converted to lower case!')

columns_to_drop = ['Row Number', 'Order ID', 'Delivery Date', 'Customer Name', 'Country', 'Postal Code', 'Country Code', 'Delivery Cost']
no_repeating_dataset_lower.drop(columns=columns_to_drop) # Drop the specified columns
# print('Unused columns dropped!')

my_dataframe = no_repeating_dataset_lower
# print(my_dataframe.head())
###################################################################################################################
####################################################################################################################
#DATA DESCRIPTION OF CLEANED DATA
# print('DATA INFORMATION')
# print(my_dataframe.info())
# print('DATA DESCPRITION')
# print(my_dataframe.describe())
# print('DATA SHAPE')
# print(my_dataframe.shape)
###################################################################################################################
####################################################################################################################
# STATISTICAL ANALYSIS
# 1. SALES
# Descriptive Statistics
stats = my_dataframe['Sales'].describe()

# Additional Statistics
mean = my_dataframe['Sales'].mean()
median = my_dataframe['Sales'].median()
mode = my_dataframe['Sales'].mode().iloc[0]
std_dev = my_dataframe['Sales'].std()
quartiles = my_dataframe['Sales'].quantile([0.25, 0.5, 0.75])

# Printing Results
# print("SALES STATS")
# print("Descriptive Statistics:") 
# print("*************************************")
# print(stats)
# print("*************************************")
# print("*************************************")
# print("\nAdditional Statistics:")
# print("*************************************")
# print("Mean:", mean)
# print("*************************************")
# print("*************************************")
# print("\nMedian:", median)
# print("*************************************")
# print("*************************************")
# print("\nMode:", mode)
# print("*************************************")
# print("*************************************")
# print("\nStandard Deviation:", std_dev)
# print("*************************************")
# print("*************************************")
# print("\nQuartiles:", quartiles)

# 2. CUSTOMERS, CITIES & CUISINES
unique_customer_ids = my_dataframe['Customer ID'].nunique()
unique_cities = my_dataframe['City'].nunique()
unique_courses = my_dataframe['Cuisine Name'].nunique()
# Printing Results
# print("Customer ID Count:", unique_customer_ids)
# print("Cities Count:", unique_cities)
# print("Cuisine Count:", unique_courses)
###################################################################################################################
####################################################################################################################
# # DATA VISUALIZATION
# 1. Customers who ordered each cuisine
# cuisine_counts = my_dataframe['Cuisine Name'].value_counts()
# # Plotting the bar graph
# colors = plt.cm.Paired(range(len(cuisine_counts)))
# cuisine_counts.plot(kind='bar', color=colors, edgecolor='black')
# # Adding labels and title
# plt.xlabel('Cuisine')
# plt.ylabel('Number of Customers')
# plt.title('Number of Customers Ordering Each Cuisine')

# plt.show()
#####################################################################################################################
# 2. Top 5 cities with the highest sales
# city_sales = my_dataframe.groupby('City')['Sales'].sum().sort_values(ascending=False) #Grouping by city and calculating total sales

# top5_cities = city_sales.head(5) #Selecting the top 5 cities
# # Plotting the pie chart
# colors = plt.cm.Paired(range(len(top5_cities)))
# explode = (0.1, 0, 0, 0, 0)  # Explode the city with the highest sales
# plt.pie(top5_cities, labels=top5_cities.index, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
# plt.title('Top 5 Cities with Highest Sales')

# plt.show()

#####################################################################################################################
# 3. Top 5 cities with the lowest sales 
# city_sales = my_dataframe.groupby('City')['Sales'].sum().sort_values(ascending=True) #Grouping by city and calculating total sales
# bottom5_cities = city_sales.head(5)

# # Plotting the horizontal bar graph
# colors = plt.cm.Paired(range(len(bottom5_cities)))
# bottom5_cities.plot(kind='barh', color=colors, edgecolor='black')
# # Adding labels and title
# plt.xlabel('Total Sales')
# plt.ylabel('City')
# plt.title('Cities with Lowest Sales')

# plt.show()
#####################################################################################################################
# 4. Top 5 cities with the highest customer base
# city_customers = my_dataframe.groupby('City')['Customer ID'].nunique()
# top5_cities_customers = city_customers.head(5)

# # Plotting the horizontal bar graph
# colors = plt.cm.Paired(range(len(top5_cities_customers)))
# top5_cities_customers.plot(kind='barh', color=colors, edgecolor='black')
# # Adding labels and title
# plt.xlabel('Number of Customers')
# plt.ylabel('City')
# plt.title('Cities with the Most Customers')

# plt.show()
#####################################################################################################################
'''
NOTE: Coding doddles
'''
# 5. Most ordered courses, starters, desserts, drinks and sides  
# Function to create a table
# def create_table(data, title):
#     fig, ax = plt.subplots(figsize=(8, 3))
#     ax.axis('off')
#     ax.set_title(title, fontweight='bold', size=14)
#     table_data = []
#     for idx, (item, sales) in enumerate(data.iteritems()):
#         table_data.append([item, sales])
#     ax.table(cellText=table_data, colLabels=['Item', 'Sales'], cellLoc = 'center', loc='center')
#     plt.show()

# # Top 5 best-selling items for each category
# top_courses = my_dataframe.groupby('Course Name')['Sales'].sum().nlargest(5)
# top_starters = my_dataframe.groupby('Starter Name')['Sales'].sum().nlargest(5)
# top_desserts = my_dataframe.groupby('Dessert Name')['Sales'].sum().nlargest(5)
# top_drinks = my_dataframe.groupby('Drink Name')['Sales'].sum().nlargest(5)
# top_sides = my_dataframe.groupby('Sides Name')['Sales'].sum().nlargest(5)

# # Bottom 5 least-selling items for each category
# bottom_courses = my_dataframe.groupby('Course Name')['Sales'].sum().nsmallest(5)
# bottom_starters = my_dataframe.groupby('Starter Name')['Sales'].sum().nsmallest(5)
# bottom_desserts = my_dataframe.groupby('Dessert Name')['Sales'].sum().nsmallest(5)
# bottom_drinks = my_dataframe.groupby('Drink Name')['Sales'].sum().nsmallest(5)
# bottom_sides = my_dataframe.groupby('Sides Name')['Sales'].sum().nsmallest(5)

# # Create tables for top and bottom items in each category
# create_table(top_courses, 'Top 5 Best-Selling Courses')
# create_table(top_starters, 'Top 5 Best-Selling Starters')
# create_table(top_desserts, 'Top 5 Best-Selling Desserts')
# create_table(top_drinks, 'Top 5 Best-Selling Drinks')
# create_table(top_sides, 'Top 5 Best-Selling Sides')

# create_table(bottom_courses, 'Bottom 5 Least-Selling Courses')
# create_table(bottom_starters, 'Bottom 5 Least-Selling Starters')
# create_table(bottom_desserts, 'Bottom 5 Least-Selling Desserts')
# create_table(bottom_drinks, 'Bottom 5 Least-Selling Drinks')
# create_table(bottom_sides, 'Bottom 5 Least-Selling Sides')