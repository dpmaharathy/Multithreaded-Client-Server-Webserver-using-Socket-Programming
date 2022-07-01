import socket
import threading
import requests
import pickle

HEADER=64
FORMAT='utf-8'
PORT=9879
DISCONNECT_MESSAGE="EXIT"
SERVER="127.0.0.1"
#SERVER=socket.gethostbyname(socket.gethostname())

ADDR=(SERVER,PORT)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)#binding the socket

def handle_client(conn,addr):
    print("NEW connection ",addr," connected")

    connected=True
    while connected:
        msg_len=conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len=int(msg_len)
            msg=conn.recv(msg_len).decode(FORMAT)
            if(msg==DISCONNECT_MESSAGE):
                connected=False
            print(f"[{addr}] {msg}")

            user_api = "ee938cc3477bf4e627bb49eba464e06f"

            location = input("Enter the city name: ")

            complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()
            send_msg=pickle.dumps(api_data)
            conn.send(send_msg)
    
    conn.close()
        
        

def start():
    server.listen()
    print(f"Server is listening on {SERVER}")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"ACTIVE connections: {threading.activeCount()-1} :")
print("Server is starting...")
start()