from handlers import *
"""
generally mc_1 is for action and mc_2 is for background
"""
TOPICS = {
    "/er/mc1/pause": mc1_pause,
    "/er/mc1/resume": mc1_resume,
    "/er/mc1/vol/set": mc1_vol_set,
    "/er/mc2/pause": mc2_pause,
    "/er/mc2/resume": mc2_resume,
    "/er/mc2/vol/set": mc2_vol_set,
    "/er/music/play": music_play,
    "/er/music/stop": music_stop,
    "/er/musicback/play": mc2_resume,
    "/er/musicback/stop": mc2_pause,
}