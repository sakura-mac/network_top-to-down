#import socket module
from socket import *
import sys

serverSocket = socket (AF_INET, SOCK_STREAM)
#PrePare a server socket
#Fill start
serverPort = 12000
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill end
while True:
    #Establish the connection
    print('Ready to server...')
    #new socket && Tcp success
    connectionSocket, addr = serverSocket.accept()#Fill start&end
    try:
        message = connectionSocket.recv(1024).decode()#Fill start&end
        #print(message)
        filename = message.split()[1]
        #print("filename")
        #print(filename)
        #Send one HTTP header line into socket
        headerline="HTTP/1.1 200 OK\r\n"
        connectionSocket.send(headerline.encode())

        f = open(filename[1:])
        outputdata= f.read()#Fill start&end
        #print("outputdata"+outputdata)
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        #connectionSocket.close()
    except IOError:
    #Send response message for file not found
    #Fill start&end:send""404 Not Found"
        connectionSocket.send("404 Not Found\r\n".encode())
        #print("404 Not Found\r\n")
    #Close client socket
    #Fill start
        connectionSocket.close()
    #Fill end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data