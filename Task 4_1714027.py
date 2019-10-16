import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
d = pd.read_csv("population_csv.csv",skiprows=[0], names=['CountryName','CountryCode','Year','Value'])
print(d)
data=d.groupby(["CountryName"])["Value"].mean()
print(data)
plt.scatter(d['CountryName'].drop_duplicates(),data)
plt.show()