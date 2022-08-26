import pandas as pd
import matplotlib.pyplot as plt

#Getting Data Frame
df = pd.read_csv('HistoricalPrices.csv')
# print(df)

#Getting x and y 
date = df.loc[:, "Date"].tolist()
closing = (df.iloc[:, 4]).toList()


plt.plot(date, closing)
plt.title("Closing Price vs Date")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()