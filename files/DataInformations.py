import pandas as pd
from importData import Customers, Products, Regions, Returns, Stores, Transactions

# get General informations About our Data

print("General info : ",Stores.info())
print("firts Customers : ",Customers.head())
print("last Regions : ",Regions.tail())
print("Summarizes Statistical Properties : ",Products.describe())
print("Rows Number : ",Returns.shape[0])
print("Columns Number : ",Returns.shape[1])
print("Columns Name : ", Transactions.columns.to_list())