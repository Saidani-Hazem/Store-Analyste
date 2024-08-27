import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
from DataCleaning import (Customers, Products, Regions, Returns, Stores,
                          Transactions)



# Distribution of Customers Country
country_counts = Customers['customer_country'].value_counts()
plt.figure(figsize=(12, 6))
sb.barplot(x=country_counts.index, y=country_counts.values, palette='viridis', edgecolor='black')
plt.title('Distribution of Customer Countries', fontsize=16, fontweight='bold')
plt.xlabel('Country', fontsize=14)
plt.ylabel('Number of Customers', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()



# Distribution of Customers Yearly_Income
income_count = Customers['yearly_income'].value_counts()
plt.figure(figsize=(12, 6))
sb.barplot(x=income_count.index, y=income_count.values, palette='coolwarm' , edgecolor='black')
plt.title('Distribution of Yearly Income', fontsize=14, fontweight='bold')
plt.xlabel('Yearly Income', fontsize=10)
plt.ylabel('Number of Customers', fontsize=10)
plt.xticks(rotation=20, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()



# Distribution of Gender
gender_counts = Customers['gender'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['#68228b', '#ff34b3'], startangle=140, textprops={'fontsize': 14})
plt.title('Distribution of Gender', fontsize=16, fontweight='bold')
plt.show()


# other one with countPlot
sb.countplot(x='member_card' , data=Customers)
plt.title('Member Card Distribution')
plt.xlabel('Card Type')
plt.ylabel('Total Customers')
plt.show()