import pandas as pd
import matplotlib.pyplot as plt

years = [2025,2026,2027,2028,2029]
revenue = [100000, 120000, 140000, 160000, 180000]
expenses = [60000, 72000, 84000, 96000, 108000]
net_income = [r-e for r,e in zip(revenue, expenses)]

df = pd.DataFrame({'Year': years,'Revenue': revenue,'Expenses': expenses,'Net Income': net_income})
df.to_csv('forecast_output.csv', index=False)

plt.figure(figsize=(8,5))
plt.plot(years, revenue, label='Revenue')
plt.plot(years, expenses, label='Expenses')
plt.plot(years, net_income, label='Net Income')
plt.title('3–5 Year Financial Forecast')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.savefig('forecast_chart.png')
plt.close()
