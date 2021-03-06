from flask import Flask
import pandas as pd
import galpy
import pygal

app = Flask(__name__)

@app.route('/hello')
def hello():
    return '<html><body>%s</body></html>' % galpy.pygal_stat()

@app.route('/1')
def graph1():
    line_chart = pygal.Line()
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    return '<html><body><div style="width:800px">%s</div></body></html>' % line_chart.render()

@app.route('/')
def graph():
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
