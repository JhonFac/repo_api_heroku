import requests
import json
from pathlib import Path

BASEDIR = Path('./db_app').absolute()

class SendDataSharpSpring():
        
    def __init__(self):
        
        id= self.get_secret('ID_ACCOUNT')
        secretKey=self.get_secret('SECRETKEY')

        # if id== '1':
        #     return {'ERROR': 'file secret_key not found'}

        self.url=f'http://api.sharpspring.com/pubapi/v1/?accountID={id}&secretKey={secretKey}'
    
    def get_secret(sefl, secret_name):
        """ Function to use the secret.json """

        with open(BASEDIR / 'secret_key.json') as f:
            secrets = json.loads(f.read())

        try:
            return secrets[secret_name]
        except:
            return {'ERROR': 'La variable {secret_name} no existe'}

    def SendData(self, data):
        data=json.loads(data) 

        arg={ 
            "method": "createLeads",
            "params": {
                "firstName": data['name'],
                "lastName": data['lastname'],
                "emailAddress": data['email'],
                "companyName": data['company'],
                "phoneNumber": data['phone'],
                "t__rminos_y_condiciones_de_servicio_6205bf308321f": data['t&c'],
                "form_message_62067fe7debaf": data['message'],
                "schedule_call_620688e37724a": data['date'],
                "formulario_website_620680a8375c8": data['identifier']
            },
            "id": ""
        } 

        print(arg)
        res=requests.post(self.url, data=json.dumps(arg))

        if (res.status_code==200):
            res_json=json.loads(res.text)
            print(res_json)
            return {
                'message': ' Successful registration',
                'response': f'{res_json}'
            }
        else:
            return {
                'message': 'the shipment was not successful',
                'response': f'{res}'
            }