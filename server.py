import flask
import urllib.request
import json
import requests
import ast
from flask import request, jsonify
from flask_cors import CORS
import pickle

#single product
# from .constants import *
# from .quote_assistant import assistant, CONTACT_TEXT, HELP_TEXT

#Multiple products, one at a time
# from .assist_multi_1_at_a_time.quote_assistant import assistant
# from .assist_multi_1_at_a_time.constants import *

#Dump, Review, Change
from .Monolithic.assist_multi_drc.utils import *
from .Monolithic.assist_multi_drc.quote_assistant import assistant, CONTACT_TEXT, HELP_TEXT
from .Monolithic.assist_multi_drc.constants import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#flask process to host and allow cors
cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/getwhatsappmessage', methods=['POST'])
def getwhatsappmessage():
    print('Getwhatsapp')
    print(request.data)
    eventsDict = json.loads(request.data)
    print('Getwhatsapp---json\n\n')
    print(eventsDict)

    if eventsDict :
        # user = get_user(eventsDict['payload']['sender']['phone'][2:])
        # if(user == 'new'):
        #     resp = "Sorry your number is not in my registry plaese contact your manager.Thankyou\nsee u soon :)"
        # else:
        #     resp = 'Hi '+ user + ' Please connect with us \n'+CONTACT_TEXT+'\n\n'+HELP_TEXT
        resp = 'Please connect with us \n'+CONTACT_TEXT+'\n\n'+HELP_TEXT
        if 'type' in eventsDict and eventsDict['type'] == 'message':
            if 'payload' in eventsDict and 'payload' in eventsDict['payload'] and 'text' in eventsDict['payload']['payload']:
            
                input_data = eventsDict['payload']['payload']['text']
                phone = eventsDict['payload']['sender']['phone'][2:]

                print('Input from whatsappuser::',phone,'::',input_data)

                flag, resp = assistant(input_data, phone, MODE_WHATSAPP)
                print("\nprint in server : ",type(resp),resp)
                print('output from assistant::',flag,'::',resp)
        
        elif 'type' in eventsDict and eventsDict['type'] == 'user-event':
            if 'payload' in eventsDict and 'type' in eventsDict['payload'] and eventsDict['payload']['type'] == 'opted-in':

                input_data = 'hi'
                phone = eventsDict['payload']['phone']

                print('Input from whatsappuser::',phone,'::',input_data)

                flag, resp = assistant(input_data, phone, MODE_WHATSAPP)

                print('output from assistant::',flag,'::',resp)
        # elif 'type' in eventsDict and eventsDict['type'] == 'user-event'
    

    return resp, 201

@app.route("/test")
def hello2():
    return "1234"

@app.route("/")
def hello():
    return "Hello, Im bot!"

if __name__ == "__main__":
    app.run(use_reloader=False)
# def start_whatsapp_conversation_server():
#     app.run(port=WHATSAPP_SERVER_PORT,host="0.0.0.0",use_reloader=False)

