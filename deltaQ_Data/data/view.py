from flask import request
import pandas as pd 
import json
import requests

from data import app


@app.route('/api', methods=['POST'])
def get_result():
    if request.method == 'POST':
        # Get the data.
        data = request.get_json()
        
        # Analayze data.
        res = analyze(data)

        # Send back the result.
        url="http://localhost:5000/result"
        header = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, json=res, headers=header)
        print(r.status_code)
    return data


def analyze(data):
    df = pd.read_json(data)

    # Compute the correlation between variables.
    corr_matrix = df.corr()
    #print(corr_matrix.head())
    
    # Find linearly dependent variables.
    list_linval = []
    for col_name, data in corr_matrix.items():
        j = int(col_name[3:])
        for i, val in enumerate(data):
            if i > j:
                if 0.7 < val <= 1.0:
                    list_linval.append((col_name,"col"+str(i)))
                if -0.7 > val >= -1.0:
                    list_linval.append((col_name,"col"+str(i)))
    print(list_linval)
     
    # Convert to json object.
    json_data = json.dumps(list_linval)
    print(json_data)
    # json_data = corr_matrix.to_json()
    
    return json_data
