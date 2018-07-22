# coding=utf8
from flask import Flask
import pandas as pd
import pygal

app = Flask(__name__)

@app.route('/n')
def graphn():
    #人数と総売上

@app.route('/')
def graph():
    #売上見込みのヒストグラム
    df = pd.read_csv('upyear.csv')
    a = df['for'].astype(int)/1000
    chart = pygal.Bar()
    chart.x_labels = range(0,65,5)
    chart.add('up', [((r<=a) & (a<r+5)).sum() for r in range(0,65,5)])
    return '<html><body><div style="width:1100px">%s</div></body></html>' % chart.render()

@app.route('/2')
def graph2():
    #試作品
    df = pd.read_csv('upyear.csv')
    a = df['for'].astype(int)/1000
    a.hist()
    #print df
    chart = pygal.Line()
    chart.title = 'year'
    chart.x_labels = ['up']
    print df.iloc[[0],[2]].values[0]
    #a = df['年合計(見通し)'].loc[0:3].astype(int)/1000
    chart.add('1', df.iloc[[0],[2]].values[0].astype(int))
    chart.add('2', df.iloc[[1],[2]].values[0].astype(int))
    chart.add('3', df.iloc[[2],[2]].values[0].astype(int))
    #chart.add('sum', df.sum().tolist())
    return '<html><body><div style="width:1100px">%s</div></body></html>' % chart.render()

@app.route('/1')
def graph1():
    #事業部ごとの４年間のラインチャート
    df = pd.read_csv('up.csv')
    print df
    line_chart = pygal.Line()
    line_chart.title = '1,2,3'
    line_chart.x_labels = df.columns
    line_chart.add('1', df.values[0])
    line_chart.add('2', df.values[1])
    line_chart.add('3', df.values[2])
    #line_chart.add('sum', df.sum().tolist())
    return '<html><body><div style="width:1100px">%s</div></body></html>' % line_chart.render()
