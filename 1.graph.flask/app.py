from flask import Flask
import galpy

app = Flask(__name__)

@app.route('/')
def hello():
    return '<html><body>%s</body></html>' % galpy.pygal_stat()
