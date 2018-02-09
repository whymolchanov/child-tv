import os
from random import shuffle
from copy import copy
import curses

VIDEO_FOLDER = '/mnt/child-tv/video/'
all_videos = []
video_queue = []
omxd_file = open('/var/run/omxctl', 'w')

def get_videos():
    directories = os.listdir(VIDEO_FOLDER)
    videos = []

    for directory in directories:
        for video_file in os.listdir(VIDEO_FOLDER + directory):
            videos.append(directory + '/' + video_file)

    return videos

all_videos = get_videos()

def play_next_video(collection):
    file_name = collection.pop(0)
    os.system('omxplayer -b ' + VIDEO_FOLDER + file_name)

def start_playing():
    video_queue = copy(all_videos)
    shuffle(video_queue)

    while len(video_queue) > 0 : play_next_video(video_queue)

while True : start_playing()
