import pandas as pd
from datetime import datetime
date_parse= lambda x: datetime.strptime(x, '%Y-%m-%d')

#Table Precipitation Matosinhos With Sliding Media

import pandas as pd
data_precipitation = pd.read_csv('https://api.ipma.pt/open-data/observation/climate/precipitation-total/porto/mrrto-1308-matosinhos.csv', index_col=0, parse_dates=['date'], date_parser=date_parse)
data_precipitation['avg'] = data_precipitation.iloc[:,4].rolling(window=3).mean()
data_precipitation

#ApplyMap (!Nao aparece a tabela em ficheiro PDF!)¶

def most_precipt(v, props=''):
    return props if v > 10 else None
data_precipitation.style.applymap(most_precipt,subset='mean',props='color:white;background-color:green')   


#Plot Graph
import matplotlib.pyplot as plt

df1 = data_precipitation['mean']
df2 = data_precipitation['avg']
plt.figure(figsize=(16,4))
plt.plot(df1,'r*',linewidth=2, label='mean',linestyle='dashed' )
plt.plot(df2,'b',label='avg', linewidth=2)
plt.legend()
plt.grid()
plt.title('Matosinhos precipitation graph')
plt.ylabel('Precipitation %')
plt.xlabel('Date')
import matplotlib.pyplot as plt
​
df1 = data_precipitation['mean']
df2 = data_precipitation['avg']
plt.figure(figsize=(16,4))
plt.plot(df1,'r*',linewidth=2, label='mean',linestyle='dashed' )
plt.plot(df2,'b',label='avg', linewidth=2)
plt.legend()
plt.grid()
plt.title('Matosinhos precipitation graph')
plt.ylabel('Precipitation %')
plt.xlabel('Date')
​
#DateMax
df1.argmax()
var_max_precip = df1.index[df1.argmax()]
df1.argmin()
var_min_precip = df1.index[df1.argmin()]
print(f'The day it rained the most was: {datetime.strftime(var_max_precip,"%Y-%m-%d")}')
print(f'The day it rained the less was: {datetime.strftime(var_min_precip,"%Y-%m-%d")}')~

#Table Maximum Temperature Matosinhos
import pandas as pd
data_max = pd.read_csv('https://api.ipma.pt/open-data/observation/climate/temperature-max/porto/mtxmx-1308-matosinhos.csv', index_col=0, parse_dates=['date'], date_parser=date_parse)
data_max

#ApplyMap (!Nao aparece a tabela em ficheiro PDF!)
def high_temp(v, props=''):
    return props if v > 20 else None
data_max.style.applymap(high_temp,subset='mean',props='color:white;background-color:blue')   

#Plot Graph
import matplotlib.pyplot as plt
df_max = data_max['mean']
plt.figure(figsize=(16,4))
plt.plot(df_max, 'g', linewidth=3, label='mean')
plt.grid()
plt.legend(loc=2)
plt.title('Graph of Average Maximum Temperature in Matosinhos')
plt.ylabel('Temperature ºC')
plt.xlabel('Date')

#DateMax
max_day=round(max(df_max),2)
df_max.argmax()
var_max = df_max.index[df_max.argmax()]
print(f'The maximum temperature detected was: {max_day}\u2103, in day {datetime.strftime(var_max,"%Y-%m-%d")}')

#Table Minimum Temperature Matosinhos
import pandas as pd
data_min = pd.read_csv('https://api.ipma.pt/open-data/observation/climate/temperature-min/porto/mtnmn-1308-matosinhos.csv', index_col=0, parse_dates=['date'], date_parser=date_parse)
data_min

#ApplyMap (!Nao aparece a tabela em ficheiro PDF!)

def low_temp(v, props=''):
    return props if v < 10 else None
data_min.style.applymap(low_temp,subset='mean',props='color:white;background-color:red')

#Plot Graph
import matplotlib.pyplot as plt
df_min = data_min['mean']
plt.figure(figsize=(16,4))
plt.plot(df_min,'b',linewidth=3, label='mean')
plt.grid()
plt.legend(loc=2)
plt.title('Graph of Average Minimum Temperature in Matosinhos')
plt.ylabel('Temperature ºC')
plt.xlabel('Date')

#DateMin

min_day=round(min(df_min),2)
df_min.argmin()
var_min=df_min.index[df_min.argmin()]
print(f'The minimum temperature detected was: {min_day}\u2103, in day {datetime.strftime(var_min,"%Y-%m-%d")}')
