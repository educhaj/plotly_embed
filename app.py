import pandas as pd
# colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
colors = ['#1a508b', '#d26900', '#1f8a1f', '#a11a1a', '#7a5a9b',
          '#6b4c41', '#c94f8a', '#636363', '#8c8c37', '#1499af']
# Load the cleaned DataFrame
df = pd.read_csv('cleaned_data.csv')

from dash import Dash, html, dcc, callback, Output, Input
from dash import dcc, html
import plotly.express as px
app = Dash(__name__)
server = app.server


app.layout = html.Div([
    dcc.Dropdown(
        id='column-dropdown',
        options=[{'label': col, 'value': col} for col in df],
        value=df['Grade 4'],  # Default selected column
        multi=False  # Set to True if you want to allow multiple selections
    ),
    dcc.Graph(id='histogram-chart')
])



@callback(
    Output('histogram-chart', 'figure'),
    Input('column-dropdown', 'value')
)
def update_chart(selected_column):
    fig = px.histogram(df, x=selected_column, title='Course Enrollment',
                       histfunc="count", color=selected_column,
                       color_discrete_sequence=colors, text_auto=True)
          
          # Update the y-axis title
    fig.update_layout(yaxis_title='Count')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
