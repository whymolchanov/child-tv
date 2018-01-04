from os import listdir
import subprocess
from random import shuffle
from copy import copy
import curses
from thread import start_new_thread

VIDEO_FOLDER = '/home/pi/child-tv/video/'
all_videos = []
video_queue = []

def get_videos():
    directories = listdir(VIDEO_FOLDER)
    videos = []

    for directory in directories:
        for video_file in listdir(VIDEO_FOLDER + directory):
            videos.append(directory + '/' + video_file)

    return videos

all_videos = get_videos()

def play_next_video(collection):
    file_name = collection.pop(0)
    subprocess.call(['omxplayer', '-b', VIDEO_FOLDER + file_name])

def start_playing():
    video_queue = copy(all_videos)
    shuffle(video_queue)

    while len(video_queue) > 0 : play_next_video(video_queue)

while True : start_playing()
