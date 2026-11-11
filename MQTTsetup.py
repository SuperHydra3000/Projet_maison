import time
import network
from thingsboard_sdk.tb_device_mqtt import TBDeviceMqttClient


# This callback will be called when an RPC request is received from ThingsBoard.
def on_server_side_rpc_request(request_id, request_body):
  print("[RPC] id:", request_id, "body:", request_body)
  client.send_rpc_reply(request_id, "ok")
  
def initMQTT(ip, token):
    # Initialising client to communicate with ThingsBoard
    client = TBDeviceMqttClient(ip, port=1883, access_token=token)
    # Register the server-side RPC callback before the main loop
    client.set_server_side_rpc_request_handler(on_server_side_rpc_request)
    # Connect to ThingsBoard
    client.connect()
    
    if client.connect():
        print(client connecté)
