
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Downloads/sales_data.csv')  
print(df.head())

category_sales = df.groupby('Category')['Sales'].sum()
print(category_sales)

date_sales = df.groupby('Date')['Sales'].sum()
print(date_sales)

category_sales.plot(kind='bar', title='Sales by Category')
plt.ylabel('Sales')
plt.xlabel('Category')
plt.tight_layout()
plt.show()

date_sales.plot(kind='line', title='Sales Over Time')
plt.ylabel('Sales')
plt.xlabel('Date')
plt.tight_layout()
plt.show()
