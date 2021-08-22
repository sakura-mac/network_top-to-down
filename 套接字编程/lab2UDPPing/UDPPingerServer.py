#We willl need the folling module to generate randomized lost packets
import random
from socket import *

#Create a UDP socket
#Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
#Assign IP addrass and port to socket
serverSocket.bind(('', 12000))

#ready to UDP&response
while True:
    print("server ready...")
    #Generate random number in the range of 0-10
    rand = random.randint(0,10)
    #Receive the client packet along with the address it is coming from
    message, add = serverSocket.recvfrom(1024)
    #Capitalize the message from the client
    message = message.upper()
    #If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
    #Otherwise, the server responds
    serverSocket.sendto(message, add)

