import configparser
import sys

defaultConfigFile = "../config/Master.cfg"

class MasterConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()

        if len(sys.argv) >=2:
            configFile = sys.argv[1]
        else:
            configFile = defaultConfigFile
        print("Config file: " + configFile)

        self.config.read(configFile)

#        print("Sections: ", self.config.sections())
#
#        for section in self.config.sections():
#            print(section)
#            for key in self.config[section]:
#                print("    ",key,"=",self.config[section][key])

    def getPowerBoxList(self):
        powerBoxList = []
        for section in self.config.sections():
            if str(section).startswith("PowerBox"):
#                print(section,self.config[section]['id'],self.config[section]['address'])
                powerBoxList.append({'id' : int(self.config[section]['id']), 'address' : self.config[section]['address'], 'port' : int(self.config[section]['port']), 'channels' : int(self.config[section]['channels'])})
        return powerBoxList

    def getMusicDir(self):
        return self.config.get('General', 'musicDir')

    def getStartTimeHour(self):
        return self.config.get('StartTime', 'hour')

    def getStartTimeMinute(self):
        return self.config.get('StartTime', 'minute')

    def getEndTimeHour(self):
        return self.config.get('StopTime', 'hour')

    def getEndTimeMinute(self):
        return self.config.get('StopTime', 'minute')

