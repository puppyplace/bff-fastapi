from src.models.user import User
from src.models.verifier import Verifier

from dotenv import dotenv_values

import requests

class AuthService():

    def __init__(self):
        # configuracoes
        configs = dotenv_values(".env")

        self.apiId = configs.get('apiKey')
        self.url = configs.get('apiUrl')
        
    
    # cadastro de usuario
    def sign_in(self, user: User):
        details = { 'email': user.email, 'password': user.password, 'returnSecureToken': True }
        r = requests.post(self.url + "signUp?key={}".format(self.apiId),data=details)
        
        return self.resolve(r)

    # login no firebase
    def sign_up(self, user: User):

        """
        login no firebase
        """

        details = { 'email': user.email, 'password': user.password, 'returnSecureToken': True }
        r = requests.post(self.url + "signInWithPassword?key={}".format(self.apiId),data=details)

        return self.resolve(r)

    def verifier(self, token: Verifier):

        """
        verifica o email
        """

        headers = {
            'Content-Type': 'application/json',
        }

        details = '{ "requestType": "VERIFY_EMAIL", "idToken": "' + token.idToken + '" }'
        r = requests.post(self.url + "sendOobCode?key={}".format(self.apiId), headers=headers, data=details)

        return self.resolve(r)
    

    # trata o resultado de cada chamada da api
    def resolve(self, r):
        if 'error' in r.json().keys():
            return {'status':'error','message':r.json()['error']['message']}

        return r.json()