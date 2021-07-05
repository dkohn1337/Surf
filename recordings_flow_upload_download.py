## The below packages must be installed via pip

import requests 
import json 
import time
import pprint
import calendar
import pendulum



# Change IMEI
imei = '357660101091346'


# Login credentials
auth_data = {"email":"user@email.com","password":"12345"}
login_api = requests.post('https://api-prod.surfsight.net/v2/authenticate',json=auth_data)
login_data = json.loads(login_api.content.decode('utf-8'))
token = login_data['data']['token']


# Request media token and media address
media_api = requests.post('https://api-prod.surfsight.net/v2/devices/'+imei+'/connect-media',headers={"content-type": "application/json", "Authorization":"Bearer " + token})
media_json = json.loads(media_api.content.decode('utf-8'))
media_token = media_json['data']['mediaToken']
media_address = media_json['data']['address']
print('Media Address: '+media_address,' // Media Token: '+media_token)


# Choose recordings range availibility
recording_availibility_api = requests.get('https://api-prod.surfsight.net/v2/devices/'+imei+'/recording-ranges?start=2021-02-14T21:00:00.000Z&end=2021-02-24T20:59:59.999Z',headers={"content-type": "application/json", "Authorization":"Bearer " + token})
recordings_files = json.loads(recording_availibility_api.content.decode('utf-8'))
recordings_files_response = recordings_files
pprint.pprint(recordings_files_response) # Pretty Print JSON


# Choose time
seconds = int (input ("Enter length of video: "))       
t = (input("Enter date and time (Year-Month-DayTHour:Minute:Seconds: " ))
stream_id = int (input ("Enter stream number 1 or 2: "))
quality = (input ("Enter quality (hq or lq): "))


# Time conversion from ISO8601 to Epoch
dt = pendulum.parse(t)
time = dt.int_timestamp



# Stream Link
## https://<media-address>/rec/{imei}/{cameraId}/{mediaToken}/{startTime}/{videoDuration}/{qualityLevel}/rec.mp4

webrtc_stream_session_1 = "https://" + media_address + "/rec/" + str(imei) + "/" + str(stream_id) + "/" + media_token + "/" + str(time) + "/" + str(seconds) + "/" + quality + '/rec.mp4'


webrtc_stream_session_2 = "https://" + media_address + "/rec/" + str(imei) + "/" + '2' + "/" + media_token + "/" + str(time) + "/" + str(seconds) + "/" + quality + '/rec.mp4'



# Upload / Download Link
headers2 = {"range": "bytes=0-", "accept": "*/*"}
print('Uploading video 1, this may take a moment... ' * 3)
print('////////////////////////////////////////////////////')
recording_availibility_api = requests.get(webrtc_stream_session_1,headers=headers2)
print('STATUS CODE : ',recording_availibility_api.status_code)
print('////////////////////////////////////////////////////')
print('Uploading video 2, this may take a moment... ' * 3)
print('////////////////////////////////////////////////////')
recording_availibility_api_2 = requests.get(webrtc_stream_session_2,headers=headers2)
print('STATUS CODE : ',recording_availibility_api_2.status_code)
print('////////////////////////////////////////////////////')
file_name_1 = "https://" + media_address + "/download/" + str(imei) + "/" + media_token + "/" + str(imei) + "_" + str(stream_id) + "_" + str(time) + "_" + str(seconds) + "_" + quality + ".mp4"
file_name_2 = "https://" + media_address + "/download/" + str(imei) + "/" + media_token + "/" + str(imei) + "_" + '2' + "_" + str(time) + "_" + str(seconds) + "_" + quality + ".mp4"
 
print("Download Link: ", file_name_1)
print('////////////////////////////////////////////////////')
print("Download Link: ", file_name_2)


## https://<media-core-server-address>/download/{imei}/{mediaToken}/{imei}_{cameraId}_{startTime}_{videoDuration}_{qualityLevel}.mp4







































