from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
app = Dash(__name__)




# app.layout = html.Div([
#     html.H1("Simple Dash Apllication"),
#     html.H2(children="test1",
#             style={
#                 "textAlign": "center",
#                 "color": "red",
#             }
#             ),
#     html.H3(children="test2",
#             style={
#                 "textAlign": "center",
#                 "color": "green",
#             }
#             ),
#     html.H4(children="test3",
#             style={
#                 "textAlign": "center",
#                 "color": "blue",
#             }
#             ),
#     html.H5(children="test5",
#             style={
#                 "textAlign": "center",
#                 "color": "orange",
#             }
#             ),
#     html.H6(children="test5",
#             style={
#                 "textAlign": "center",
#                 "color": "yellow",
#             }
#             ),


#     # PLOTTING A GRAPH
#     dcc.Graph(
#         id="Simple Graph",
#         figure = {
#             'data' : [
#                 {'x': [2,4,6,8], 'y': [23,56,89,10], 'type': 'bar', 'name': 'first chart'},
#                 {'x': [2,4,6,8], 'y': [80,20,50,100], 'type': 'bar', 'name': 'Second chart'}
#                 ],
#             'layout' : {
#                 "plot_bgcolor": 'grey',
#                 "paper_bgcolor": "aqua",
#                 "font" : {
#                     "color": "white"
#                 },
#                 'title': "Simple Bar Chart"
#             }
#         },
#     )
# ])

app.layout = html.Div([
    html.H1(children="Second div",
            style={
                'textAlign': 'center',
                'color': "red"
            }),
    
    dcc.Graph(
        id="Scatter Plot",
        figure = {
            'data': [
                go.Scatter(
                    x=[43,12,9,56,89,32,40,13,99,85,73,65],
                    y=[33,78,23,12,11,89,55,65,7,93,29,77],
                    mode='markers'
            )],
            'layout': go.Layout(
                title = "Scatter plot of random numbers",
                xaxis = {"title": "random x values"},
                yaxis = {'title': "random y values"}
            )
        }
    )

])

# orders = pd.read_csv("dataset/orders.csv")
# print(orders.columns)
# dcc.Graph(
#     id= "barchart",
#     figure={
#         'data':[
#             go.Bar(
#                 x = orders.order_id,
#                 y = orders.order_hour_of_day
#             )
#         ],
#         'layout' : go.Layout(
#             title= "Orders per hour chart",
#             x = {'title':"order_id"},
#             y = {'title': "orders_per_hour"}
#         )
#     }
# )
if __name__ == "__main__":
    app.run(debug=True)