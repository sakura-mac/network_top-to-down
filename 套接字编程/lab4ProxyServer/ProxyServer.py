# -*- coding: UTF-8 -*-
# 使用localhost来作为代理服务器的ip，port：8888
# 多线程的操作被封装了，因此只要修改listen参数即可指定客户端个数（网络看的，不知道真假）
# 客户端使用浏览器修改lan局域网配置，并且访问页面https://gaia.cs.umass.edu/kurose_ross/wireshark.htm
# 没有实现GET更新
from socket import *
import sys

#if len(sys.argv) <=1:#这玩意老报错，以后再看吧，先注释掉
#    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address of Proxy Server')
#    sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# fill start
tcpPort = 8888
tcpSerSock.bind(('', tcpPort))
tcpSerSock.listen(10)
# fill end
while 1:
    # start receiving data from the client
    print('ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection form : ', addr)
    message = tcpCliSock.recv(2048).decode()# fill start&end
    print("message from the client : ",message)
    # extract the filename from the given message
    print(message.split()[1])#[0]=='GET',[1]=<url>，这次没有ip写域名得到绝对路径
    filename = message.split()[1].partition("//")[2].partition("/").replace("/", "-")#这里的filename为了简单，包含了path，并且文件名不允许“/”
    print(filename)
    fileExist = "false"
    print(filetouse)
    try:
        # check whether the file exist in the cache
        f = open(filename, "r")
        outputdata = f.readlines()
        fileExist = "true"
        print("文件在cache中")
        # proxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n")
        tcpCliSock.send("Content-Type:text/html\r\n")
        # fill start
        tcpCliSock.send(outputdata.encode())
        # fill end
        pirnt('Read from cache')
    # error handling for file not found in cache
    except IOError:
        # ready to connect to the port80 server
        if fileExist == "false":
            # create a socket on the proxyserver
            print("ready to connect to the 80server")
            c = socket(AF_INET, SOCK_STREAM)#fill start&end
            hostn = message.split()[1].partition("//").partition("/")[0]#域名跟主机名一样唯一映射ip
            print(hostn)
            try:
                # connect to the socket to port80
                # fill start
                c.connect((hostn, 80))
                # fiil end
                # create a temporary file on this socket and ask port 80 for the file requested by the client
                # fileobj = c.makefile('r', 0),这里我只弄了文字，就不需要封装对象了
                # fileobj.write("GET " + "http://" + filename + "HTTP/1.0\n\n")
                # Read the response into buffer
                # fill start
                c.send(message.encode())
                buffer = c.recv(4096)
                tcpCliSock.send(buffer)
                # fill end
                # create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                # fill start
                tmpFile = open(filename, "w")
                tmpFile.writelines(buffer.decode())
                tmpFile.close()
                # fill end
            except:
                print("Illegal request")
                c.close()
        else:
            # HTTP response message for file not found
            # fill start
            tcpCliSock.send("proxy读了但是没完全读".encode())
            # fill end
        # close the client and the server sockets
    tcpCliSock.close()
    print("tcpClientSocket close")
# fill start
tcpSerSock.close()
print("proxyServer close")
# fill end