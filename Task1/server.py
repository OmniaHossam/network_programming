from socket import *

try:
    s = socket(AF_INET, SOCK_STREAM)
    print('Server socket is successfully created')

    host = '127.0.0.1'
    port = 24921
    s.bind((host, port))
    print(f'Socket is bound to port {port}')

    s.listen(5)
    print('Socket is listening')

    c, addr = s.accept()
    print(f'Connected to {addr}')

    while True:
        receive = b''
        while True:
            part = c.recv(2048)
            if not part:
                print('Client closed the connection.')
                break
            receive += part
            if b'\n' in part:
                break
        print(f'Server received: {receive.decode()}')

        # Send response to client
        inp = input('Server Response: ')
        # +b'\n'  indicator for end o message
        c.send(inp.encode() + b'\n')

    c.close()
except Exception as e:
    print(e)
