import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = pd.read_csv("population_csv.csv",skiprows=[0], names=['CountryName','CountryCode','Year','Value'])
print(data)


fig = plt.figure()
fig.subplots_adjust(hspace=0.6, wspace=0.6)


data1=data[data.CountryName=="India"]
ax1 = fig.add_subplot(231)
ax1.title.set_text("population of India")
ax1.plot(data1.Year,data1.Value)


data2=data[data.CountryName=="Zimbabwe"]
ax2 = fig.add_subplot(232)
ax2.title.set_text("population of Zimbabwe")
ax2.plot(data2.Year,data2.Value)

data3=data[data.CountryName=="Arab World"]
ax3 = fig.add_subplot(233)
ax3.title.set_text("population of Arab World")
ax3.plot(data3.Year,data3.Value)

data4=data[data.CountryCode=='CSS']
ax4 = fig.add_subplot(234)
ax4.title.set_text("population of CSS")
ax4.plot(data4.Year,data4.Value)

data5=data[data.CountryCode=='CEB']
ax5 = fig.add_subplot(235)
ax5.title.set_text("population of CEB")
ax5.plot(data5.Year,data5.Value)

data6=data[data.CountryCode=='EAR']
ax6 = fig.add_subplot(236)
ax6.title.set_text("population of EAR")
ax6.plot(data6.Year,data6.Value)

plt.show()