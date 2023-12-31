
'''
TCPServer by: ishan
Listens for packets on a particular address and port.
Alpha: 19dec23
'''

import socket
import settings.tcp as settings

#####################Defining variable like port ip address and buffer size ################################
I_P = settings.TCP["SERVER_I_Pv4"]
P_ORT = settings.TCP["SERVER_PORT"]
BUFFER_SIZE = 1024

###################Printing the output##########################################
print(f'This is the TCP server, it will open a port at {I_P}:{P_ORT} and being listening')
print(f'Make sure the actual server IP address matches {I_P} in the settings file')
print('This script has no error handling, by design')

##########################Using try and exception####################################################
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((I_P, P_ORT))
        print(f'Bound to {I_P}:{P_ORT}')
        while True:
            s.listen(1)
            conn, addr = s.accept()
            print(f'Connection address: {addr}')
            data = conn.recv(BUFFER_SIZE).decode()
            print(data)
            conn.send(data.encode())
except socket.error as e:
    print(f'Error: {e}')




