import socket
import time
import struct

class PowerBoxProxy:

    def __init__(self, address, port, numChannels):
        self.address = address
        self.port = port
        self.numChannels = numChannels

        self.mySocket = socket.socket()
        self.connected = False

    def connect(self):
        retries = 0
        MAX_RETRIES = 10

        while not self.connected and retries <= MAX_RETRIES:
            try:
                self.mySocket.connect((self.address, self.port))
            except Exception as e:
#                print(e)
                time.sleep(1)
#                print("Retrying connection to " + self.address + ":" + str(self.port))
                retries += 1
            else:
                print("Connection to " + self.address + ":" + str(self.port) + " established.")
                self.connected = True

        if not self.connected:
            print("Connection to " + self.address + ":" + str(self.port) + " failed.")

    def disconnect(self):
        self.mySocket.close()
        self.connected = False

    def sendCmd(self, channel, action):
        msg = str(channel) + "," + action

        if not self.connected:
            # If the socket is not connected, raise an exception.
            #raise Exception("Socket not connected.")
            print("Socket not connected (" + self.address + ":" + str(self.port) + ") - Message (" + msg + ") not sent.")
            return

        if (channel != '*') and (int(channel) > self.numChannels or int(channel) <= 0):
            # If the action requested is for an invalid channel, raise an exception
            raise Exception("Invalid channel ID.")

        self.mySocket.send(msg.encode())
        ack = self.mySocket.recv(1024).decode()
        print(str(time.clock_gettime(time.CLOCK_REALTIME)) + " Sent command (" + msg + ") to " + self.address + ":" + str(self.port))

