import os
import logging
from Flask import Flask

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
	logging.debug("saying hello")
	return 'Hello Joshua!'