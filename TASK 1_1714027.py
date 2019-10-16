import pandas as pd
from matplotlib import pyplot as plt
data=pd.read_csv("population_csv.csv",skiprows=[0],names=('CountryName','CountryCode','Year','Value'))
print(data)
data1=data[data.CountryName=="India"]
print(data1)
plt.plot(data1.Year,data1.Value,label="India")
data2=data[data.CountryName=="Zimbabwe"]
plt.plot(data2.Year,data2.Value,label="Zim")
data3=data[data.CountryName=="Arab World"]
plt.plot(data3.Year,data3.Value,label='Arab World')
data4=data[data.CountryCode=='CSS']
plt.plot(data4.Year,data4.Value,label='CSS')
data5=data[data.CountryCode=='CEB']
plt.plot(data5.Year,data5.Value,label='CEB')
plt.legend(loc='upper left')
plt.show()