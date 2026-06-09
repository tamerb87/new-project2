import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Value": [10, 20, 15, 8]
})

fig = px.bar(df, x="Category", y="Value", title="Sample Bar Chart")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Sample Dashboard"),
    dcc.Graph(figure=fig),
    html.P("This is a sample dashboard using Dash and Plotly.")
])

if __name__ == "__main__":
    app.run_server(debug=True)

    print("Neta good luck")