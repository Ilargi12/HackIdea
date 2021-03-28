from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/results')
def hello_world():
    return {'name':['hi macarena', 'hi chichua'], 'description': ['lozl', 'kimbs']}


if __name__ == '__main__':
    app.run()
