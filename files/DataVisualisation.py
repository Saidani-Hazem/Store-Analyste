import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
from DataCleaning import Customers, Products, Regions, Returns, Stores,Transactions




# Total transactions by store_id
store_transactions = Transactions.groupby('store_id').size()
store_transactions.plot(kind='bar', color='blue', title='Total Transactions by Store')
plt.xlabel('Store ID')
plt.ylabel('Number of Transactions')
plt.show()



# Total transactions by store Name
names = Transactions.merge(Stores, on='store_id')
transactions = names.groupby('store_name').size()
store_transactions.plot(kind='bar', color='red', title='Total Transactions by Store Name')
plt.xlabel('Store Name')
plt.ylabel('Number of Transactions')
plt.show()


#store by country
store = Stores['store_country'].value_counts()
plt.pie(store, labels=store.index, autopct='%1.1f%%', colors=['red', 'blue' , 'green'])
plt.title('Distribution of store country', fontsize=16, fontweight='bold')
plt.show()


sb.histplot(data=Customers, x="birthdate", bins=20)
plt.show()