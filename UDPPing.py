import random
from socket import *
import time

#prompt user for server address
serverName = input("input the IP address or hostname of the server you wish to ping \n")

# Create and setup a UDP socket
clientPort = 1024
serverPort = 22000
message = "I am ping"
clientSocket = socket(AF_INET, SOCK_DGRAM)
for i in range(1, 10):

    clientSocket.sendto(message.encode(), (serverName, serverPort))
    start = time.time()

    while True:
        clientSocket.settimeout(1)
        gotMessage, serverAddress = clientSocket.recvfrom(serverPort)
        end = time.time()
        dif = end - start
        if dif >= 1:
            print("\n packet " & i & "was lost in transmission \n")
            dif = "infinity"
            break
        elif gotMessage == "":
            break

    print("packet " & i & "had a RTT of " & dif & "\n")
clientSocket.close()
