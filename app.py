import joblib as joblib
from flask import Flask, request, jsonify
#import joblib
import sys

sys.modules['sklearn.externals.joblib'] = joblib
import  flask_restful
from flask_restful import Resource, Api

import joblib
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

api = Api(app)

model = joblib.load(open('CoronaViru', 'rb'))


@app.route('/')
def home():
    return 'prediction api '


@app.route("/predictions", methods=["post"])
def predictions():
    values = request.json['values']
    predictions = model.predict([ values , ])

    if predictions[0] == 0:
        return 'The patient negative'
    else:
        return 'The patient positive '
    # return 'z' #jsonify(list(predictions))


if __name__ == '__main__':
    app.run(debug=True)
