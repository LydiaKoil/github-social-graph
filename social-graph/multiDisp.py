from plotly.subplots import make_subplots
import plotly.graph_objects as go
import retrieval

fig = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "bar"}, {"type": "scatter"}]],
    subplot_titles=("<b>The Average Number of Commits on Each Day of the Week</b>","<b>Contribution During Programming Project</b>")
)

data = retrieval.commits_per_day()
days = data[0]
values = data[1]

fig.add_trace(go.Bar(x=days, y=values, name="No. Of Commits"),
              row=1, col=1, )



groupData=retrieval.commits_ratio()
owner=groupData[0]
others=groupData[1]

fig.add_trace(go.Scatter(
    x = list(range(1,len(owner))),
    y = owner,
    name="Owner",
    hovertemplate =
    '<b>Commits</b>: %{y}'+
    '<br><b>Week</b>: %{x}<br>',
    showlegend = True),
              row=1, col=2)


fig.add_trace(go.Scatter(
    x = list(range(1,len(others))),
    y = others,
    name="Other Contributors",
    hovertemplate =
    '<b>Commits</b>: %{y}<extra></extra>'+
    '<br><b>Week</b>: %{x}<br>',
    showlegend = True),
              row=1, col=2)


fig.update_layout(height=700, showlegend=True, title= " GIT HUB ")

fig.show()
