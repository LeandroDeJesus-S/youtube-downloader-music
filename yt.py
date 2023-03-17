#!/usr/bin/env python
import argparse
from pathlib import Path
from utils import messages, tryerrors
from down.mod import Download
from utils import functions
from time import sleep
from colorama import init

init()

default_music_path = Path.home() / 'Music'
default_video_path = Path.home() / 'Videos'
functions.verify_default_path(default_music_path, default_video_path)

args = argparse.ArgumentParser()
args.add_argument('link', type=str, nargs='+')
args.add_argument('-p', action='store_true', help=messages.P_MESSAGE)
args.add_argument('-v', action='store_true', help=messages.V_MESSAGE)
args.add_argument('-t', nargs=1, default='mp3', help=messages.T_MESSAGE)
args.add_argument('-o', default=default_music_path, nargs=1, 
                  type=str, help=messages.O_MESSAGE, metavar='[output]')

parsed = args.parse_args()


save_path = parsed.o[0] if isinstance(parsed.o, list) else parsed.o
if parsed.t:
    filetype = parsed.t[0] if isinstance(parsed.t, list) else parsed.t

save_path = functions.get_default_path(
    filetype, default_music_path, default_video_path
)

for link in parsed.link:
    downloader = Download(link, save_path)
    if parsed.p:
        tryerrors.make_download_treatments(downloader.download_playlist, filetype)
        
    elif parsed.v:
        tryerrors.make_download_treatments(downloader.download_video, filetype)
