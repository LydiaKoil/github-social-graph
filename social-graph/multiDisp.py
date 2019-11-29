from plotly.subplots import make_subplots
import plotly.graph_objects as go
import retrieval

fig = make_subplots(
    rows=2, cols=2,
    specs=[[{"type": "bar"},{"type": "scatter"}], [{"type": "pie"},{}]],
    subplot_titles=("<b>The Average Number of Commits on Each Day of the Week</b>","<b>Contribution During Programming Project (2nd Year)</b>","<b>Languages Used in College Work</b>")
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


langData = retrieval.languages_used()
count = langData[0]
langs = langData[1]

fig.add_trace(go.Pie(values=count, labels=langs),
              row=2, col=1)

fig.update_layout(height=1000,
                  title={
        'text': "<i>Visualisation of The Software Engineering Process Using GitHub</i> ",
        'y':0.999,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
                  font=dict( family="Courier New, monospace",color="#232b2b")
    )

fig.add_layout_image(
    dict(
        source="https://banner2.cleanpng.com/20180320/iew/kisspng-computer-icons-github-desktop-wallpaper-clip-art-icon-github-download-5ab1a968570b46.7771010815215926803565.jpg",
        xref="paper", yref="paper",
        x=1, y=1.05,
        sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom"
    )
)



fig.show()