import os
from random import shuffle
from copy import copy
import curses

VIDEO_FOLDER = '/mnt/child-tv/video/'
all_videos = []
video_queue = []
omxd_file = open('/var/run/omxctl', 'w')

# find max length of arrays inside array
# param {array[]} directories
def find_dir_max_length(directories):
    max_length = 0

    for directory in directories:
        if len(directory) > max_length:
            max_length = len(directory)

    return max_length

# collect videos from multiple folders to one
# array that we can use furter to play video
def collect_videos():
    directories = os.listdir(VIDEO_FOLDER)
    dir_max_length = find_dir_max_length(directories)
    videos = []

    for i in range(dir_max_length):
        for directory in directories:
            # i % len(directory) used to add previous videos of the directory if
            # it's length lesser than dir_max_length
            videos.append(directory + '/' + os.listdir(VIDEO_FOLDER + directory)[i % len(directory)])

    return videos

all_videos = collect_videos()

def play_next_video(collection):
    file_name = collection.pop(0)
    os.system('omxplayer -b ' + VIDEO_FOLDER + file_name)

def start_playing():
    video_queue = copy(all_videos)

    while len(video_queue) > 0 : play_next_video(video_queue)

while True : start_playing()
