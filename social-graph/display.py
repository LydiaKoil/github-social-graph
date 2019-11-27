import plotly.graph_objects as go
import retrieval

data = retrieval.commits_per_day()
days = data[0]
values = data[1]

fig = go.Figure([go.Bar(x=days, y=values)])
fig.update_layout(autosize=False, width=400, height=300)
fig.show()