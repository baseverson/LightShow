#!/usr/bin/python3

import MasterConfig
import PowerBoxProxy
import MusicPlayer
import ShowRunner
import time

class MasterController:
    def __init__(self):
        # Create objects
        self.cfg = MasterConfig.MasterConfig()

        # Create the MusicPlayer to handle the music.  This will be passed to the ShowRunner.
        self.player = MusicPlayer.MusicPlayer(self.cfg.getMusicDir())

        # Using the list of configured Power Boxes, instantiate the power box list
        self.powerBoxList = {}
        self.powerBoxConfig = self.cfg.getPowerBoxList()
        for box in self.powerBoxConfig:
            self.powerBoxList[box['id']] = PowerBoxProxy.PowerBoxProxy(box['address'], box['port'], box['channels'])

        # Connect each PowerBoxProxy to its associated Power Box
        print("The following Power Boxes have been configured:")
        for box in self.powerBoxList:
            print("    Box #" + str(box) + ", address: " + self.powerBoxList[box].address + ", port: " + str(self.powerBoxList[box].port) + ", channels: " + str(self.powerBoxList[box].numChannels))
#            self.powerBoxList[box].connect()

        # Create the Show runner that will reach each script and run the show.
        self.showRunner = ShowRunner.ShowRunner(self.powerBoxList, self.player, self.cfg.getMusicDir())

        # The playlist stores the high level of song/scripts and other generic light control commands.
        self.playlist = []

        return

    def allLightsOn(self):
        for box in self.powerBoxList:
            self.powerBoxList[box].channelOn("*")
        return

    def allLightsOff(self):
        for box in self.powerBoxList:
            self.powerBoxList[box].channelOff('*')
        return

    def readPlaylist(self):
        print("Reading playlist: " + self.cfg.getMusicDir() + '/playlist.cfg')
        file = open(self.cfg.getMusicDir() + '/playlist.cfg', "r")
        lines = []
        for line in file:
#            print("Line: " + line)
            if (line != "\n") and (not line.startswith('#')):
                self.playlist.append(line.strip('\n'))

        print("Playlist:")
        for command in self.playlist:
            print("  " + command)

        return

    def Main(self):

        while True:
            self.readPlaylist()

            for iter in self.playlist:
                tokens = iter.split(" ")
                if tokens[0] == "ALL_ON":
                    print("Turning all lights on for " + str(float(tokens[1])) + " seconds.")
                    self.allLightsOn()
                    time.sleep(float(tokens[1]))
                elif tokens[0] == "ALL_OFF":
                    print("Turning all lights off for " + str(float(tokens[1])) + " seconds.")
                    self.allLightsOff()
                    time.sleep(float(tokens[1]))
                else:
                    print ("Running script: " + tokens[0])
                    self.showRunner.readScript(tokens[0])
                    self.showRunner.runScript()


if __name__== '__main__':
    mcp = MasterController()
    mcp.Main()
