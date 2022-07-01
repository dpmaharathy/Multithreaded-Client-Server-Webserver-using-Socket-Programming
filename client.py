import socket
from datetime import datetime
import pickle

HEADER=64
FORMAT='utf-8'
PORT=9879
DISCONNECT_MESSAGE="EXIT"
SERVER="127.0.0.1"
ADDR=(SERVER,PORT)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send_location(msg):
    message=msg.encode(FORMAT)
    msg_len=len(message)
    send_length=str(msg_len).encode(FORMAT)
    send_length+=b' ' * (HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    api_data=(pickle.loads(client.recv(2048)))
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    city=api_data['name']
    weather_desc = api_data['weather'][0]['description']
    temp_city = ((api_data['main']['temp']) - 273.15)
    
    print("Selected City is: ",city)
    print ("Current temperature is: {:.2f} deg C".format(temp_city))
    print ("Current weather desc  :",weather_desc)
    print ("Current Humidity      :",hmdt, '%')
    print ("Current wind speed    :",wind_spd ,'kmph')

send_location("Jodhpur")
#send_location("Hello PROJECT")
#send_location(DISCONNECT_MESSAGE)
