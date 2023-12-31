'''
TCPClient by: ishan
Send TCP packets to a particular address and port.
Alpha: 19dec23
'''

import socket
import time
from datetime import datetime
import settings.tcp as settings

###########################Definning ip and port#########################################
i_p = settings.TCP["SERVER_TCP_IPv4"]
p_ort = settings.TCP["SERVER_PORT"]

#####################Printing the output of client and port#########################################################
print(f'This is the TCP client, it will try to connect to a server at {i_p}:{p_ort} in the settings file.')
print('This script has no error handling, by design')


#Usage of while loop 
BUFFER_SIZE = 1024
while True:
    print(f'Trying to open a socket to {i_p}:{p_ort}')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        message_text = f"ATU {datetime.now()}"
        message = message_text.encode('utf-8')
        s.connect((i_p, p_ort))
        s.send(message)
        print(f'Sent {message_text} to {i_p}:{p_ort}')
        data = s.recv(BUFFER_SIZE)
        print('Server echoed:', data)
        time.sleep(1)
