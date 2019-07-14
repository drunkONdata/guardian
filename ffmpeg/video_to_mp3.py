"""
Python script to extract MP3 audio from videos using Python.
 
Requirements: brew install lame ffmpeg
 
How to use the script:  $ python video_to_mp3.py VIDEO.mp4
"""

import sys
import os
import time
 
 
def video_to_mp3(file_name):

    try:
        file, extension = os.path.splitext(file_name)
        # Convert video into .wav file
        os.system('ffmpeg -i {file}{ext} {file}.wav'.format(file=file, ext=extension))
        # Convert .wav into .mp3 file
        os.system('lame {file}.wav {file}.mp3'.format(file=file))
        os.remove('{}.wav'.format(file))  # Delete the .wav file
        print('"{}" successfully converted into MP3!'.format(file_name))
    except OSError as err:
        print(err.reason)
        exit(1)
 
 
def main():

    if len(sys.argv) != 2:
        print('Usage: python video_to_mp3.py FILE_NAME')
        exit(1)
 
    file_path = sys.argv[1]
    try:
        if not os.path.exists(file_path):
            print('file "{}" not found!'.format(file_path))
            exit(1)
 
    except OSError as err:
        print(err.reason)
        exit(1)
 
    video_to_mp3(file_path)
    time.sleep(1)
 
 
if __name__ == '__main__':
