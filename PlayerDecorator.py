from os import getcwd
from os.path import join
from time import sleep
from mplayer import *

"""
amixer  sset PCM,0 90%
"""


class PlayerDecorator:
    def __init__(self, song_path):
        self._is_paused = True
        self._player = Player()
        self._player.volume = 100
        self._player.loadfile(song_path)
        self._player.pause()

    def load(self, song_path):
        self._player.loadfile(song_path)
        self._is_paused = False

    def load_cwd(self, song_name):
        print("start playing: " + join(getcwd(), song_name))
        self.load(join(getcwd(), song_name))

    def pause(self):
        if not self._is_paused:
            self._player.pause()
            self._is_paused = True

    def resume(self):
        if self._is_paused:
            self._player.pause()
            self._is_paused = False

    def set_volume(self, volume):
        print("volume: ", volume)
        if 0 <= volume <= 100:
            self._player.volume = volume

    def is_alive(self):
        return self._player.is_alive()

    def quit(self):
        self._player.quit()


def play_one(_players, which):
    for i in range(len(_players)):
        _players[i].pause() if i != which else _players[i].resume()


if __name__ == "__main__":
    songs_names = ["call_me.mp3", "atomic.mp3", "long.mp3", ]
    add_song = "bondi.mp3"
    counter = 0
    playersDecs = []

    for name in songs_names:
        playersDecs.append(PlayerDecorator(join(getcwd(), name)))

    while True:
        for i in range(len(playersDecs)):
            print("play #", i)
            play_one(playersDecs, i)
            sleep(5.0)
        for player in playersDecs:
            player.resume()
        print("play all together")
        sleep(5.0)
        counter += 1
        if counter == 2:
            playersDecs[0].load(join(getcwd(), add_song))
            playersDecs[0].set_volume(1)
