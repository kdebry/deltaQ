from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import pandas as pd
import requests
import json


from ui import app


data = r'./devops_assignment_linear_dependency.csv'
df = pd.read_csv(data)
json_data = df.to_json()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    # return render_template('result.html')
    if request.method == 'POST':
        res = request.get_json()
        
        with open('data.json', 'w') as json_file:
            json.dump(res, json_file)
        return res
    else:
        # read file
        with open('data.json', 'r') as json_file:
            data=json.load(json_file)
        #res = json.load(data)
        rdf = pd.read_json(data)
        return render_template('result.html', tables=[rdf.to_html(classes='data',header="true")])


@app.route('/api', methods=['POST'])
def analyze():
    api_url = 'http://localhost:5001/api'
    header = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url=api_url, json=json_data, headers=header)
    print(r.status_code)
    return redirect(url_for('result'))


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename(file.filename))
        return 'file uploaded successfully'


if __name__ == "__main__":
    app.run(debug=True)
