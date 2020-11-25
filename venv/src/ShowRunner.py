import time
import configparser
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Action:
    time: float
    box: int
    channel: int
    action: str

class ShowRunner:
    def __init__(self, powerBoxList, player, musicDir):
        self.powerBoxList = powerBoxList
        self.player = player
        self.musicDir = musicDir
        self.curentSong = ""
        self.actionList = []

    def readScript(self, scriptName):
        print("Reading script: " + self.musicDir + '/' + scriptName + '.script')
        file = open(self.musicDir + '/' + scriptName + '.script', "r")
        self.actionList = []
        lines = []
        for line in file:
#            print("Line: " + line)
            if (line != "\n") and (not line.startswith('#')):
                lines.append(line.strip('\n'))

#        for line in lines:
#            print("Good line: " + line)

        # The first line should be the file name of the song to play
        self.currentSong = lines[0]

        for iter in range(1, len(lines)):
#            print(lines[iter])
            tokens = lines[iter].split(' ')
            newAction = Action(tokens[0], tokens[1], tokens[2], tokens[3])
#            print("Adding new action...")
#            print("    Time: " + newAction.time)
#            print("    Box: " + newAction.box)
#            print("    Channel: " + newAction.channel)
#            print("    Action: " + newAction.action)
            self.actionList.append(newAction)
        return

    def runScript(self, endTime):
        if self.currentSong == "":
            print("No script currently loaded.")
            return

        # Start the song
        if self.currentSong != "none":
            self.player.playSong(self.currentSong)

        # Set current time to zero. This will serve as the timer for running all of the actions.
        startTime = time.time()

        # Loop through the actions and run them per the scripted time.
        for action in self.actionList:
            # Check to make sure we are not past the end time for the show
            now = datetime.now().time()
            if (now > endTime):
                break

            actionTime = float(action.time) + startTime
            currentTime = time.time()
            if (actionTime > currentTime):
                time.sleep(actionTime - currentTime)

            self.executeAction(action.box, action.channel, action.action)

        self.player.stop()

        return

    def executeAction(self, boxID, channelID, action):

        if str(boxID) == '*':
            for box in self.powerBoxList:
                self.powerBoxList[box].sendCmd('*', action)
        else:
            try:
                self.powerBoxList[int(boxID)].sendCmd(channelID, action)
            except Exception as e:
                print(e)
        return

