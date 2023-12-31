
'''
UDPServer by: ishan
Listens for packets on a particular address and port.
Alpha: 19dec23
'''

import socket
import settings.udp as settings

#######################Defining the ip port and buffer size#################################################
I_P = settings.UDP["SERVER_UDP_IPv4"]
P_ORT = settings.UDP["SERVER_PORT"]
BUFFER_SIZE = 1024


####################################3printing the output#####################################################################
print(f'This is the UDP server, it will open a port at {I_P}:{P_ORT} and being listening')
print(f'Make sure the actual server IP address matches {I_P} in the settings file')
print('This script has no error handling, by design')


#################Using wile loop############################################################################
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind( (I_P, P_ORT) )
    print('Listening on', I_P)
    while True:
        data, addr = s.recvfrom(BUFFER_SIZE)
        data = data.decode()
        print(addr, data)
