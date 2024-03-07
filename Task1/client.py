from socket import *

try:
    s = socket(AF_INET, SOCK_STREAM)
    print('Client socket is successfully created')

    host = '127.0.0.1'
    port = 24921
    s.connect((host, port))
    print(f'Connected to server at {host}:{port}')

    while True:
        inp = input('Client send: ')
         # +b'\n'  indicator for end o message
        s.send(inp.encode() + b'\n' )
        # Receive response from server
        receive = b''
        while True:
            part = s.recv(2048)
            if not part:
                break
            receive += part
            if b'\n' in part:
                break
        print(f'Client received: {receive.decode()}')

    s.close()
except Exception as e:
    print(f'Socket error: {e}')
