# -*- coding: utf-8 -*-
%matplotlib inline
import matplotlib.pyplot as plt
plt.figure()
plt.xlabel(u'豆腐 - tofu')
plt.title(u'豆腐 - TOFU')
plt.show()


import pandas as pd
df = pd.read_csv('upyear.csv')
g = df.groupby('cus').sum()
d = df.sort_values('for', ascending=False)
d.plot.bar(y=['for','ac'],stacked=False, figsize=(14,4))


%matplotlib inline
import pandas as pd
df = pd.read_csv('upyear.csv')
g = df.groupby('cus').sum()
d = df.loc[df['cus']==chr(84)+chr(73)+'S'].sort_values('ac', ascending=False)
d.index = d['name']
d.plot.bar(y=['for','ac'],stacked=False, figsize=(14,4))
