import pandas as pd
from importData import Customers, Products, Regions, Returns, Stores,Transactions


# Calculate the empty cells

if __name__ == "__main__":
  print(Customers.isnull().sum())
  print(Products.isnull().sum())
  print(Regions.isnull().sum())
  print(Returns.isnull().sum())
  print(Stores.isnull().sum())
  print(Transactions.isnull().sum())



#remove rows with empty cells
Transactions = Transactions.dropna()



# Filling Missing Data With "Unknow"
Customers = Customers.fillna("Unknow")
Stores = Stores.fillna("Unknow")
Returns = Returns.fillna("Unknow")
Regions =Regions.fillna("Unknow")
Products = Products.fillna("Unknow")



#remove dublicate rows

Customers = Customers.drop_duplicates()
Transactions = Transactions.drop_duplicates()
Products = Products.drop_duplicates()



# remove dublicate Rows Based on one Column
Stores = Stores.drop_duplicates(subset=['store_name'])



# fix Some Data Type
Products['product_retail_price'] = Products['product_retail_price'].astype(float)
Products['product_cost'] = Products['product_cost'].astype(float)
Returns['return_date'] = pd.to_datetime(Returns['return_date'])
Customers['birthdate'] = pd.to_datetime(Customers['birthdate'])

# Fix Some Data Format

Stores['store_name'] = Stores['store_name'].str.upper()
Products['product_name'] = Products['product_name'].str.upper()
Customers['first_name'] = Customers['first_name'].str.upper()
Customers['last_name'] = Customers['last_name'].str.upper()
Regions['sales_district'] = Regions['sales_district'].str.upper()


