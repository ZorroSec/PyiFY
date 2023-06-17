from requests import get, post
import os
import time
from app import *

class Generator:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def cpf(self):
        pass