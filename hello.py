import os
from Flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello Joshua!'