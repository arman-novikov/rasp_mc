from PlayerDecorator import PlayerDecorator
from os import getcwd
from os.path import join

back_music = "atomic.mp3"

back_player = PlayerDecorator(join(getcwd(), back_music))
action_player = PlayerDecorator(join(getcwd(), ""))


def mc1_pause(void):
	print("mc1_pause")
	action_player.pause()


def mc1_resume(void):
	print("mc1_resume")
	action_player.resume()


def mc1_vol_set(volume):
	print("mc1_vol_set: ", volume)
	print("out of work")


def mc1_lang_set(lang_index):
	print("mc1_lang_set: ", lang_index)


def mc2_pause(void):
	print("mc2_pause")
	back_player.pause()


def mc2_resume(void):
	print("mc2_resume")
	back_player.resume()


def mc2_vol_set(volume):
	print("mc2_vol_set: ", volume)
	print("out of work")


def music_play(track):
	print("music_play: ", track)
	action_player.load_cwd(track)


def music_stop(void):
	print("music_stop")
	action_player.pause()


def back_music_play(void):
	back_player.resume()
	print("back_music_play")


def hint1_play(hint_index):
	print("hint1_play: ", hint_index)