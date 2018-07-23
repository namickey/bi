# coding=utf8
from flask import Flask
import pandas as pd
import pygal

app = Flask(__name__)

@app.route('/f')
def graph_for():
    return '<html><body><div style="width:800px">%s</div></body></html>' % getFor().render()

def getFor():
    #顧客別
    df = pd.read_csv('upyear.csv',encoding='utf-8')
    g = df.groupby('cus')
    t = g.sum().sort_values('for', ascending=False)['for']
    chart = pygal.Bar(x_label_rotation=40)
    chart.title = u'2018年度：年間売上計画（顧客別）'
    chart.x_labels = t.index
    chart.add(u'売上', t.values)
    return chart

@app.route('/a')
def graph_ac():
    return '<html><body><div style="width:800px">%s</div></body></html>' % getAc().render()

def getAc():
    #顧客別
    df = pd.read_csv('upyear.csv',encoding='utf-8')
    g = df.groupby('cus')
    t = g.sum().sort_values('ac', ascending=False)['ac']
    chart = pygal.Bar(x_label_rotation=40)
    chart.title = u'2018年度：年間売上実績（顧客別）'
    chart.x_labels = t.index
    chart.add(u'売上', t.values)
    return chart

@app.route('/')
def graph():
    return '<html><body><div style="width:800px">%s</div></body></html>' % gethist().render()

def gethist():
    #売上見込みのヒストグラム
    df = pd.read_csv('upyear.csv')
    a = df['for'].astype(int)/1000
    chart = pygal.Bar()
    chart.title = u'2018年度：年間案件数（売上別）'
    chart.x_labels = range(0,65000,5000)
    chart.add(u'案件数', [((r<=a) & (a<r+5)).sum() for r in range(0,65,5)])
    return chart

def gethist_t():
    #売上見込みのヒストグラム
    df = pd.read_csv('upyear.csv')
    a = df.loc[df['cus'] == 'T' + 'I' + 'S']['for'].astype(int)/1000
    chart = pygal.Bar()
    chart.title = u'2018年度：年間案件数（売上別）'
    chart.x_labels = range(0,65000,5000)
    chart.add(u'案件数', [((r<=a) & (a<r+5)).sum() for r in range(0,65,5)])
    return chart

@app.route('/all')
def graph_all():
    ret = '<html><body>'
    ret += '<div style="width:800px">%s</div>' % gethist().render()
    ret += '<div style="width:800px">%s</div>' % gethist_t().render()
    ret += '<div style="width:800px">%s</div>' % getAc().render()
    ret += '<div style="width:800px">%s</div>' % getFor().render()
    ret += '</body></html>'
    return ret
