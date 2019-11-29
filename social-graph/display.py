import plotly.graph_objects as go
import retrieval

#Display Bar Chart
data = retrieval.commits_per_day()
days = data[0]
values = data[1]

fig = go.Figure([go.Bar(x=days, y=values)])
fig.update_layout(autosize=False, width=400, height=300, title_text='Number of Commits To Repo Per Day')

fig.show()



#Display Line Graph

groupData=retrieval.commits_ratio()
owner=groupData[0]
others=groupData[1]

fig2 = go.Figure(go.Scatter(
    x = list(range(1,len(owner))),
    y = owner,
    name="Owner",
    hovertemplate =
    '<i>Price</i>: $%{y:.2f}'+
    '<br><b>X</b>: %{x}<br>'+
    '<b>%{text}</b>',
    text = ['Custom text {}'.format(i + 1) for i in range(5)],
    showlegend = True))

fig2.add_trace(go.Scatter(
    x = list(range(1,len(others))),
    y = others,
    name="Other Contributors",
    hovertemplate = 'Price: %{y:$.2f}<extra></extra>',
    showlegend = True))

fig2.update_layout(
    hoverlabel_align = 'right',
    title = "Commits Over the Duration the Project")

fig2.update_layout(autosize=False,
    width=600,
    height=400,
    margin=go.layout.Margin(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ))

<<<<<<< HEAD



fig2.show()



=======
fig2.show()

>>>>>>> 8cd8e30b0c8c258b29ac5321e18b454fc6440258
