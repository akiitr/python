import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
from statistics import mean
import statistics as st

#----------------DICTionay-------------------------
ak_web1 = {'day':[1,2,3,4,5,6], 'visitor':[90,80,70,60,50,40], 'Bounce':[10,20,30,40,50,60]}
ak_web2 = {'day':[1,2,3,4,5,6], 'visitor':[90,80,70,60,50,40], 'Bounce2':[10,20,30,40,50,600], 'money':[1,2,3,4,5,6]}
#-----------Data Frame-------------------------

df1 = pd.DataFrame(ak_web1)
df2 = pd.DataFrame(ak_web2)
merge = pd.merge(df1, df2, on='day')

df3 = pd.DataFrame({'ak':[1,2,3], 'pk':[4,5,6]}, index=[1,2,3])
df4 = pd.DataFrame({'jk':[7,8,9],'no':[10,11,12]},index=[2,3,4])
#index are row no and dict key are columns merged with outer datafrmae

joined = df4.join(df3)
#changing index and key column
#changing index to mk in df4
df4.set_index("no",inplace= True)
df5 = df4.rename(columns= {'jk':'age'})

concat = pd.concat([df4,df5])
#read a CSV

csv = pd.read_csv('test.csv', index_col=0)
csv.to_html('test.html')
csv = csv.reindex(columns=['age'])
csv = csv.diff(axis=0)

#csv.plot(kind = 'bar')
#plt.show()
#---------------Print and Plot statements-----------------
print(csv)
print(mean([1,1,1,1,2,3,3,5,4,4]))
print(st.mean([1,1,1,1,2,3,3,5,4,4]))
print(st.mode([1,1,1,1,2,3,3,5,4,4]))
print(st.variance([1,1,1,1,2,3,3,5,4,4]))
#df5.plot()
#plt.show()
#print(df1.head(2))
#print(df2.tail(2))
#print(merge)
#print(joined)