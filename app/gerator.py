from requests import get, post
import os
import time
from colorama import Fore, Style
from app import *

class Generator:
    url = 'https://www.4devs.com.br/'
    password = 'zorro'
    def __init__(self, url, password):
        self.url = url
        self.password = password
    
    def cpf(self):
        req = post(self.url, {'acao':'gearar_cpf', 'ponntuacao':'s'})
        req = req.text
        print(req)

