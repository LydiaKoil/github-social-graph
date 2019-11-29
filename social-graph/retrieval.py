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

from requests.auth import HTTPBasicAuth

credentials = json.loads(open('credentials.json').read())
authentication = HTTPBasicAuth(credentials['username'], credentials['password'])

def commits_per_day():
    response = requests.get('https://api.github.com/repos/rvailnaveed/College-Work/stats/commit_activity', auth=authentication)
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
    response = requests.get('https://api.github.com/repos/rvailnaveed/pii-tool/stats/participation', auth=authentication)
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
    

    
    return [owner_f, others_f]

def languages_used():
    response = requests.get('https://api.github.com/repos/rvailnaveed/College-Work/languages', auth=authentication)
    data = json.loads(response.text)
    count=list(data.values())
    langs=list(data.keys())

    return [count, langs]
    

