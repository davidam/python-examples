#!/usr/bin/python

#
# Simple HTTP Adder
# Adds in two stages
#
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# September 2009
#

import socket

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

myPort = 1234
mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost',myPort))

# Queue a maximum of 10 TCP connection requests
mySocket.listen(5)

# Declare and initialize state
#
# Are we in first round? (receiving first addend)
firstRound = True
# First addend
addend1 = 0

# Accept connections, read incoming data, and answer back an HTLM page
#  (in a loop)

# Exception for capturing interruptions to the program
try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'HTTP request received:'
        httpRequest = recvSocket.recv(1024)
        # Split HTTP request by space, get second (1) element
        # (which is the resource), get everything from it except
        # for the first character (/).
        resourceName = httpRequest.split(' ',2)[1][1:]
        # Next is not really needed, since non-ints are dealt with later,
        # but makes it clear that requests for favicon will probably
        # be received.
        if resourceName == "favicon.ico":
            httpCode = "400 Resource not available"
            htmlBody = "No favicons for now"
        else:
            try:
                if firstRound:
                    addend1 = int(resourceName)
                    htmlBody = "Received " + resourceName + " as first addend. " \
                        + "Waiting for second addend to add..."
                else:
                    addend2 = int(resourceName)
                    htmlBody = "Add done: " + str(addend1) + " + " \
                        + str(addend2) + " = " + str(addend1 + addend2)
                httpCode = "200 OK"
                # To finish, change to the other round
                firstRound = not (firstRound)
            except ValueError:
                httpCode = "404 Not Found"
                htmlBody = "Only integers are accepted as addends"
        recvSocket.send("HTTP/1.1 " + httpCode + "\r\n\r\n" +
                        "<html><body>" + htmlBody + "</body></html>" +
                        "\r\n")
	recvSocket.close()
except KeyboardInterrupt:
    mySocket.close()
