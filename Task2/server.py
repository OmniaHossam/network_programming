import socket
import threading

# Connection Data
host = '127.0.0.1'
port = 7000

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message,mess_client=None):
    for client in clients:
        if(client != mess_client):
            client.send(message)
        
# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message,client)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break
        
# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        c, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        c.send('NICK'.encode('ascii'))
        nickname = c.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(c)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        c.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(c,))
        thread.start()
        
receive()
