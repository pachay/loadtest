# coding=utf-8
import websocket
import json
import time
import os


ws_url = os.getenv('WS_URL')
n_clients = int(os.getenv('N_CLIENTS'))

class Client(object):
    def __init__(self, ws_url):
        self.ws = websocket.WebSocket()
        self.ws.connect(ws_url)

    def send(self):
        self.ws.send(json.dumps({'body': u'Привет, это чат!'}))

clients = []
for n in range(0, n_clients):
    clients.append(Client(ws_url))

while True:
    for client in clients:
        client.send()
        print 'Message sent'
        time.sleep(0.1)

