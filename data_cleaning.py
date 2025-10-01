import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

input_file = 'sales_data.csv'
output_folder = 'output_charts'
os.makedirs(output_folder, exist_ok=True)

df = pd.read_csv(input_file)
df = df.drop_duplicates()
df.fillna(0, inplace=True)

plt.figure(figsize=(8,5))
sns.lineplot(data=df, x='Month', y='Revenue')
plt.title('Monthly Revenue')
plt.savefig(os.path.join(output_folder,'monthly_revenue.png'))
plt.close()
