from flask import Flask
from flask import request
from PoliticalClassifier import PoliticalClassifier
app = Flask(__name__)
cl = PoliticalClassifier()        
@app.route('/',methods=['POST'])
def get_predictions():
    print(request.get_json()['text'])
    return [cl.predict(x) for x in request.get_json()['text']]