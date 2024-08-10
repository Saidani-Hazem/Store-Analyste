import pandas as pd

#import csv data into variables (DATA FRAME)

Stores = pd.read_csv("Data/MavenMarket_Stores.csv")
Customers = pd.read_csv("Data/MavenMarket_Customers.csv")
Products = pd.read_csv("Data/MavenMarket_Products.csv")
Regions = pd.read_csv("Data/MavenMarket_Regions.csv")
Returns = pd.read_csv("Data/MavenMarket_Returns_1997-1998.csv")

Tran1997 = pd.read_csv("Data/MavenMarket_Transactions_1997.csv")
Tran1998 = pd.read_csv("Data/MavenMarket_Transactions_1998.csv")


# testing some DATA FRAME

if __name__ == "__main__":
  print(Stores)
  print(Returns)


# Concatenate Tran1997 and Tran1998 into One DATA FRAME (with ignoring index to generate a index from 1 to rows number)

Transactions = pd.concat([Tran1997 , Tran1998], ignore_index=True)

if __name__ == "__main__":
  print(Transactions)