import pandas as pd
from flask import Flask, render_template, request, url_for, redirect
from flask import url_for, send_from_directory
import json
import plotly
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

app = Flask(__name__)

# This is the csv file which contains fake data for demonstration purposes
df = pd.read_csv('data.csv')

@app.route("/")
def modals():
    
    table = df.sort_values(by='WW', ascending=False)
    table = table.drop_duplicates(subset=['brand'])
    
    graphs = dict()
    for item in df['brand'].unique():
        subset = df[df['brand'] == item]
        title = item.capitalize()
        plot = get_scatter(subset, title)
        graphs[item] = plot
    
    return render_template("modals.html", table=table, graphs=graphs, df=df)

@app.route("/content", methods = ['POST'])
def content():
    
    clicked=request.form['data'].replace(" ","").replace('\n','')
    Message = {"Message": "Python says Hello"}
    #dd = df.set_index('WW')
    sub = df[df['brand'] == clicked]
    section = "I clicked " + clicked
    print(sub)
    print(clicked)
    print(section)
    
    title = clicked.capitalize()
    fig = get_scatter(sub, title)
    print(type(fig))
    
    return fig

def get_scatter(df, title):
    scatter = px.scatter(df, x=df['WW'],
                             y=df['cost'],
                            color=df['brand'],
                            color_discrete_map={
                                                "nike": "blue",
                                                "adidas": "red",
                                                 "puma": "green"},
                            category_orders={"brand": ["nike", "adidas", "puma"]})
    scatter.update_layout(xaxis_type='category', xaxis={'categoryorder': 'category ascending'})
    scatter.update_traces(mode='lines+markers')
    scatter.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')),
                          selector=dict(mode='lines+markers'))

    trace = go.Figure(data=scatter)
    trace.update_layout(title_text='Scatterplot of {} Cost Over Time'.format(title), title_x=0.5)
    trace.update_layout(width=1100, height=500)
    trace.update_xaxes(tickangle=30)
    trace.update_layout(font=dict(
        family="commuters-sans, sans-serif"
    ))

    return json.dumps(trace, cls=plotly.utils.PlotlyJSONEncoder)

@app.route("/<path:file_path>")
def send_file(file_path):
    
    return send_from_directory(app.static_folder, file_path, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)