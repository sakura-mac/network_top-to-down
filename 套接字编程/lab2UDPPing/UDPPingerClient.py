# -*- coding: UTF-8 -*-
# 1.使用UDP发送ping Ping <sequence_number> <time>
# 2.打印服务器的pong(也就是你的ping大写化)，计算RTT（s）
# 3.无响应打印“Requested time out”
import time
from socket import *
ip = '192.168.1.108'
severPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
# 约束等待响应不超过1s
clientSocket.settimeout(1)
for i in range(1, 11):
    old_time = time.time()
    sendtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(old_time))
    clientSocket.sendto(("Ping %d %s" %(i, sendtime)).encode(), (ip, severPort))
    try:
        Pong, add = clientSocket.recvfrom(2048)
        print("报文：%s" % Pong.decode())
        rtt = time.time() - old_time
        print("RTT: %f" % rtt)
    except Exception:
        print("Requested time out of package %d" % i)

clientSocket.close()


