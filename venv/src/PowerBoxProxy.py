import requests
import json

class PowerBoxProxy:

    def __init__(self, address, port, numChannels):
        self.address = address
        self.port = port
        self.numChannels = numChannels

    def sendCmd(self, channel, action):
        url = "http://" + self.address + ":" + str(self.port) + "/PowerBox/setChannelState"
        channelCommand = {
            'channel': channel,
            'state': action
        }
#        print("Sending command to ", url, " ", json.dumps(channelCommand))
        try:
            resp = requests.post(url, json=channelCommand)
            if resp.status_code != 200:
                print("Exception sending command to ", url, " ", json.dumps(channelCommand), format(resp.status_code))
#                raise Exception('Exception calling POST', url, json.dumps(channelCommand), format(resp.status_code))
        except Exception as e:
            print(e)
        return

    def channelOn(self, channel):
        self.sendCmd(channel, "ON")
        
#        url = "http://" + self.address + ":" + str(self.port) + "/PowerBox/setChannelState"
#        channelCommand = {
#            'channel':channel,
#            'state':'ON'
#        }
#        print("Sending command to ", url, " ", json.dumps(channelCommand))
#        resp = requests.post(url, json=channelCommand)
#        if resp.status_code != 200:
#            print("Exception sending command to ", url, " ", json.dumps(channelCommand), format(resp.status_code))
#            raise Exception('Exception calling POST', url, json.dumps(channelCommand), format(resp.status_code))
#        return
    
    def channelOff(self, channel):
        self.sendCmd(channel, "ON")

#        url = "http://" + self.address + ":" + str(self.port) + "/PowerBox/setChannelState"
#        channelCommand = {
#            'channel': channel,
#            'state': 'OFF'
#        }
        #        print("Sending command to ", url, " ", json.dumps(channelCommand))
#        resp = requests.post(url, json=channelCommand)
#        if resp.status_code != 200:
#            print("Exception sending command to ", url, " ", json.dumps(channelCommand), format(resp.status_code))
#            raise Exception('Exception calling POST', url, json.dumps(channelCommand), format(resp.status_code))
#        return
    
