from dotenv import load_dotenv
from flask import request, jsonify, render_template, redirect
from .functions import jsonConversion, transform+get, list_subreddits
from flask_cors import CORS
import joblib
from .models import

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    CORS(app)

try:
    title = request.args['title']
    body = request.args['body']
    user = request.args['user']
except KeyError as e:
    return ('Some values are missing')

@app.route('/')
def template():
    return '''<h1>This is just a test</h1>
<p>Working remotely on build week project.</p>'''


@app.route('/subreddit', methods=['POST'])
def get_subreddits():
    reg = request.get_json(force=True)
    con = request.jsonConversion(reg)
    tran = transform_get(con, titel, body, user)
    subreddit_list = list_subreddits(tran)


    return jsonify(subreddit_list)


@app.route('/subreddit_test', methods=['POST'])
def get_subreddits():
    title, body, user = sorted([request.values['title'],
                                request.values['body'],
                                request.values['user']])
    reg = {'title': title, 'body': body, 'user': user}
    con = jsonConversion(reg)
    tran = transform_get(reg, title, body, user)
    subreddit_list = list_subreddits(tran)

    return jsonify(subreddit_list)


@app.route('/username', methods=['POST'])
def from_username(name=None):
    name = name or request.values['user_name']
    model = Username_Model(name=name)
    prediction = mdoel.predict()
    output = list_subreddits(prediction)

    return jsonfy(output)

app.run()
