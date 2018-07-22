# coding=utf8
from flask import Flask
import pandas as pd
import pygal

app = Flask(__name__)

@app.route('/t')
def graph_tis():
    #顧客別
    df = pd.read_csv('upyear.csv',encoding='utf-8')
    g = df.groupby('cus')
    t = g.sum().sort_values('for', ascending=False)['for']
    chart = pygal.Bar(x_label_rotation=40)
    chart.x_labels = t.index
    chart.add(u'売上', t.values)
    return '<html><body><div style="width:1100px">%s</div></body></html>' % chart.render()

@app.route('/')
def graph():
    #売上見込みのヒストグラム
    df = pd.read_csv('upyear.csv')
    a = df['for'].astype(int)/1000
    chart = pygal.Bar()
    chart.x_labels = range(0,65,5)
    chart.add('up', [((r<=a) & (a<r+5)).sum() for r in range(0,65,5)])
    return '<html><body><div style="width:1100px">%s</div></body></html>' % chart.render()
