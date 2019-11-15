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
    response = requests.get('https://api.github.com/repos/rvailnaveed/College-Work/stats/commit_activity')
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
