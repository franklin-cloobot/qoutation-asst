# from .test import *
# from .Monolithic.main import start_conversation
# from .Monolithic.server import start_whatsapp_conversation_server

# try:
#     start_whatsapp_conversation_server()
#     # start_conversation()
# except Exception as e:
    # print(e)
# import sys
# # print(sys.version)
# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def hello():
#     return "Hello, I love Digital Ocean! "
# if __name__ == "__main__":
#     app.run()

from .test import *
# from .Monolithic.main import *
from .Monolithic.server import *
# from .Monolithic.server import start_whatsapp_conversation_server

try:
    app()
    # start_conversation()
except Exception as e:
    print(e)

