import dash_core_components as dcc
import plotly.figure_factory as ff
import plotly.graph_objects as go
import dash_html_components as html
import dash_daq as daq
import dash_table
import pandas as pd
import numpy as np
solar_data = {'Index':  ['timestamp', 'Second value'],
        'Second Column Name': ['First value', 'Second value'],
        }


solar_df = pd.DataFrame (solar_data)
labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]



x = np.arange(10)

wellbeing = go.Figure(data=go.Scatter(x=x, y=x**2))
wellbeing.update_layout(
    autosize=True,
    # width=500,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
    ))

zanzibar = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in solar_df.columns],
    data=solar_df.to_dict('records'),
    row_deletable=True,
)

def wrapiefigure(labels, values, holes):
    return go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])

pie = wrapiefigure(labels, values, .4)
pie.update_layout(
    autosize=True,
    # width=500,
    margin=dict(
        l=10,
        r=10,
        b=10,
        t=10,
    ),
    paper_bgcolor="#ddd",
    showlegend=False,


)
# pie.update_layout(legend=dict(x=0, y=0))
pie.update_yaxes(automargin=True)

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]

gantt_diagram = ff.create_gantt(df)
gantt_diagram.update_layout(autosize=True,     margin=dict(
        l=70,
        r=70,
        b=70,
        t=70,
    ),)
gantt_diagram["layout"].pop("height", None)
gantt_diagram["layout"].pop("width", None)

sleep = go.Figure()
sleep.add_trace(go.Bar(
    y=[''],
    x=[8],
    name='SF Zoo',
    orientation='h',
    marker=dict(
        color='rgba(246, 78, 139, 1)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
    )
))
sleep.add_trace(go.Bar(
    y=[''],
    x=[8],
    name='LA Zoo',
    orientation='h',
    marker=dict(
        color='rgba(58, 71, 80, 1)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    ),
))
sleep.add_trace(go.Bar(
    y=[''],
    x=[8],
    name='SF Zoo',
    orientation='h',
    marker=dict(
        color='rgba(246, 78, 139, 1)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
    )
))



sleep.update_layout(barmode='stack', autosize=True,     margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
    ), showlegend=False, title = "test",
                    paper_bgcolor="#ddd",

                    )


fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta", value = 220,
    domain = {'x': [0.1, 1], 'y': [0, 1]},
    title = {'text' :"<b>Profit</b>"},
    delta = {'reference': 200},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 300]},
        'threshold': {
            'line': {'color': "red", 'width': 2},
            'thickness': 0.75,
            'value': 280},
        'steps': [
            {'range': [0, 150], 'color': "lightgray"},
            {'range': [150, 250], 'color': "gray"}]}))

task_name = dcc.Input(id='task_content', type='text', value="name")
task_start = dcc.Input(id='task_start', type='text', value="start")
task_stop = dcc.Input(id='task_stop', type='text', value="stop")
task_group = dcc.Input(id='task_stop', type='text', value="group")
submit_tasks = html.Button('Submit', id='submit-val', n_clicks=0),

todo_name = dcc.Input(id='task_content', type='text', value="name")
submit_todo = html.Button('Submit', id='submit-val', n_clicks=0),

journal_content = dcc.Textarea(
    id="journal_content",
    placeholder="What's on your mind?",
    # value='This is a TextArea component',
    style={'width': '100%', 'height': '300px'}
)

horizontal_stats = go.Figure(go.Bar(
            x=[20, 14, 23],
            y=['work', 'sleep', 'recr'],
            orientation='h',

))
horizontal_stats.update_layout(
    margin=dict(
        l=0,
        r=10,
        b=10,
        t=10,
    ),
    paper_bgcolor="#ddd",

)

slider1= daq.Slider(
  id='my-daq-slider',
  value=40,
  min=0,
  max=100,
  step = 10,
  color=dict(default="grey"),
 size = 100
  # targets={"25": {"label": "TARGET"}}
)

slider2= daq.Gauge(
  id='my-daq-gauge',
  min=0,
  max=10,
  value=6,
  size=100
)

interpolation_strats = dcc.Dropdown(
    id='demo-dropdown',
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='NYC'
)
# fig.update_layout(height = 250)
# fig.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})


