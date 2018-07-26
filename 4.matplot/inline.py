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


%matplotlib inline
import pandas as pd
df = pd.read_csv('member.csv')
df.T[df.T.index.str.contains('売上')][5].plot()


%matplotlib inline
import pandas as pd
df = pd.read_csv('member.csv')
df.T[df.T.index.str.contains('売上')].fillna(0).loc[:,[x for x in range(70)]].plot(figsize=(18,12))


%matplotlib inline
import pandas as pd
df = pd.read_csv('member.csv')
df.index = df['社員名']
a = df.T[df.T.index.str.contains('売上')].fillna(0).iloc[:,[x for x in range(70)]].T
a.loc[a['売上(2018/05)'] > 800]


%matplotlib inline
import pandas as pd
df = pd.read_csv('member.csv')
df.index = df['社員名']
a = df.T[df.T.index.str.contains('売上')].fillna(0).T
a.loc[a['売上(2018/05)'] > 1100].T.plot(figsize=(18,12))


%matplotlib inline
import pandas as pd
df = pd.read_csv('member.csv')
#df.index = df['社員名']
a = df.T[df.T.index.str.contains('売上') | df.T.index.str.contains('社員名')].fillna(0).T
a.groupby('社員名').sum().sort_values('売上(2018/05)', ascending=False)

%matplotlib inline
import pandas as pd
df = pd.read_csv('member.csv')
#df.index = df['社員名']
a = df.T[df.T.index.str.contains('売上') | df.T.index.str.contains('社員名')].fillna(0).T
a.groupby('社員名').sum().sort_values('売上(2018/06)', ascending=False)[0:20]
