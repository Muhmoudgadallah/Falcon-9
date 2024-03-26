import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from bs4 import BeautifulSoup
import requests
import seaborn as sns
import plotly.express as px 
from dash import Dash,dcc,html,Output,Input,callback
####
df = pd.read_csv("falcon9.csv")

##graphs__________________________________________________




###
app = Dash(__name__)
app.layout = html.Div(children=[
    html.H1("Falcon 9 report ",style={"textAlign":"center","color":"grey"}),
    html.H3("Count of Launches per Year, Day , Season"),
    html.Div(children=[
        
        dcc.Dropdown(options = df.year.unique(),
                     value="2008",
                     id = "choose_year")]),
        dcc.Graph(id="seasons"),
        dcc.Graph(id="month"),
        dcc.Graph(id="day"),
        dcc.Graph(id="total") ])



@callback(
    [
     Output("seasons","figure"),
     Output("month","figure"),
     Output("day","figure")
     #,Output("total","figure")
     ],

     Input("choose_year","value")
)

### Callback 
def update(value) : 
    dff = df.query("year == @value")
    month = dff.groupby("month")["month"].count().sort_values(ascending=False)
    season = dff.groupby("season")["month"].count().sort_values(ascending=False)
    days = dff.groupby("day")["month"].count().sort_values(ascending=False)
    total = dff["month"].count()

    f1 = px.pie(values=season.values, names=season.index, title='Launches per Season')
    f2 = px.bar(days,x=days.index,y=days.values)
    f3 = px.bar(month,x=month.index,y= month.values)

    return f1,f2,f3






if __name__ == "__main__" : 
    app.run_server()