from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

database = {
    'Premit': [
        {'de': 'SEQUENCIA', 'para': '', 'id': '1', 'grupo': 'premit'},
        {'de': 'COD_CIA', 'para': '', 'id': '1', 'grupo': 'premit'},
        {'de': 'NUM_PROC', 'para': '', 'id': '1', 'grupo': 'premit'},
    ],
    'Premrec': [
        {'de': 'SEQUENCIA', 'para': '', 'id': '1', 'grupo': 'premrec'},
        {'de': 'COD_CIA', 'para': '', 'id': '1', 'grupo': 'premrec'},
        {'de': 'NUM_PROC', 'para': '', 'id': '1', 'grupo': 'premrec'},
    ]
}

@app.route('/<string:idx>')
def index(idx):
    return jsonify(database[idx])

if(__name__ == '__main__'):
    app.run('localhost', 5000, True)