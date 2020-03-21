try:
    # Attempt to import the pygame module for playing music on Raspberry Pi.
    # If an exception is caught, then we're not running on a Raspberry Pi.
    import pygame
    rasp_env = True
except(ImportError, RuntimeError):
    # Set flag indicating that we are not running on a Raspberry Pi.
    rasp_env = False

class MusicPlayer:
    def __init__(self, musicDir):
        self.musicDir = musicDir

        if rasp_env:
            print("Initializing MusicPlayer - musicDir: ", self.musicDir)
            pygame.mixer.init();

        return

    def playSong(self, filename):
        print("Song starting: " + filename)

        if rasp_env:
            pygame.mixer.music.load(self.musicDir + "/" + filename)
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play()

    def stop(self):
        if rasp_env:
            pygame.mixer.music.stop()
        return