import pygame

class MusicPlayer:
    def __init__(self, musicDir):
        self.musicDir = musicDir
        print("Initializing MusicPlayer - musicDir: ", self.musicDir)

        pygame.mixer.init();
        return

    def playSong(self, filename):
        print("Song starting: " + filename)
        pygame.mixer.music.load(self.musicDir + "/" + filename)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()

#        while pygame.mixer.music.get_busy() == True:
#            pass

    def stop(self):
        pygame.mixer.music.stop()
        return