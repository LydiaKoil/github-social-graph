import plotly.graph_objects as go

import base64
import json
import requests
from pprint import pprint
from datetime import datetime
from pprint import pprint

def data_access():
    response = requests.get('https://api.github.com/users/Lydtk')
    details = json.loads(response.text)
    pprint(details)

if __name__ == "__main__":
    data_access()