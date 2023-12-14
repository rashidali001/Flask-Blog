'''

When you import this package, the __init__.py executes and defines the following
symbols the package exposes to the outside world.

'''
from flask import Flask

app = Flask(__name__)


# ALL IMPORT TO BE PLACE IN THE BOTTOM SO AS TO AVOID CIRCULAR IMPORTS

from app import routes