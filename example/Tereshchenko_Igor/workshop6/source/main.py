import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import json

from flask import Flask, render_template, request
from example.Tereshchenko_Igor.workshop4.source.forms.user import UserForm

from example.Tereshchenko_Igor.workshop4.source.dao.userhelper import *
app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET'])
def index():
    count = 500
    xScale = np.linspace(0, 100, count)
    yScale = np.random.randn(count)

    # Create a trace
    trace = go.Scatter(
        x=xScale,
        y=yScale
    )

    data = [trace]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html',
                           graphJSON=graphJSON)


@app.route('/graphs', methods=['GET'])
def graphs():
    count = 500
    x = np.linspace(-np.pi, np.pi, 50)
    y = np.sin(x)


    line = go.Scatter(
        x=x,
        y=y,
        name="sin(x)"
    )

    bar = go.Bar(
        x=["House","Car"],
        y=[100,300]
    )
    data = [line,bar]
    ids=[1,2]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('graphs.html',
                           graphJSON=graphJSON, ids=ids)

if __name__ == '__main__':
    app.run(debug=True)