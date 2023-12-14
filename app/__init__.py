'''

When you import this package, the __init__.py executes and defines the following
symbols the package exposes to the outside world.

'''
from flask import Flask

app = Flask(__name__)