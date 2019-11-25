import plotly.graph_objects as go

import base64
import json
import requests
from pprint import pprint
from datetime import datetime
from pprint import pprint
import pandas as pd
import numpy as np
import plotly.express as px

def commits_per_day():
    response = requests.get('https://api.github.com/repos/jonahwilliams/webdev/stats/commit_activity')
    data = json.loads(response.text)
    
    days=['Sunday','Monday','Tuesday','Wednesday', 'Thursday', 'Friday','Saturday','Sunday']
    values=[0,0,0,0,0,0,0]
    i=0
    for item in data: 
        for day in item['days']:
            values[i]+=day
            i+=1
        i=0
    
    data = []
    data.append(days)
    data.append(values)
    return data

    # iris = px.data.iris() # iris is a pandas DataFrame
    # fig = px.scatter(iris, x="sepal_width", y="sepal_length")
    # fig.show()


def commits_ratio():
    response = requests.get('https://api.github.com/repos/rvailnaveed/pii-tool/stats/participation')
    print(response.text)
    data = json.loads(response.text)
    owner = data['owner']
    others = data['all']
    i=0
    for _ in others:
        others[i]= others[i]-owner[i]
        i+=1
    owner_f=[]
    others_f=[]

    for i in range(7,19):
        others_f.append(others[i])
        owner_f.append(owner[i])


    print(others_f)
    print(owner_f)

    return [owner_f, others_f]

