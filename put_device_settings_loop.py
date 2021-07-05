## Below packages must be installed via pip

import requests
import json
import time



# Generate Login Token
auth_data = {"email":"user@email.com","password":"12345"}
login_api = requests.post('https://api-prod.surfsight.net/v2/authenticate',json=auth_data)
login_data = json.loads(login_api.content.decode('utf-8'))
token = login_data['data']['token']
print(token)

# Device Settings PUT request (use any of the API's property that you may need and can be found in the API docs)
my_list = ['357660101356789', '357660101354321', '3576601013012345']
lenght = len(my_list)
print('Total devices in the list:',lenght)
for idx,imei in enumerate(my_list):
  try:
    time.sleep(0.5)
    token_header = {"Authorization": "Bearer " + token}
    body = {"hotSpot":{"internetAccess": False}}
    put_device_settings = requests.put('https://api-prod.surfsight.net/v2/devices/'+imei+'/device-config',headers=token_header,json=body)
    put_device_settings_response = json.loads(put_device_settings.content.decode('utf-8'))
    print(imei,put_device_settings_response,idx, 'out of', lenght)
  except KeyError:
    print(imei + ' offline')
    continue
