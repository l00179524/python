
'''
UDPClient by: ishan
Send UDP packets to a particular address and port.
Alpha: 9dec23
'''

import socket
import time
from datetime import datetime
import settings.udp as settings


##############################Defining the ip and port############################################
I_p = settings.UDP["SERVER_UDP_IPv4"]
P_ORT = settings.UDP["SERVER_PORT"]

##############Printing the result##############################################
print(f'This is the UDP client, it will try to connect to a server at {I_P}:{P_ORT} in the settings file.')
print('This script has no error handling, by design')

#################################Usage of while loop#################################
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        message_text = f"ATU {datetime.now()}"
        message = message_text.encode('utf-8')
        s.sendto(message, (I_P, P_ORT))
        print(f'Sent {message_text}')
        time.sleep(1)



