#!/usr/bin/env python
import argparse
from pathlib import Path
from utils import messages, tryerrors
from os import system
from down.mod import Download

save_path = Path.home() / 'Music'
if not Path(save_path).exists():
    system(f'mkdir {save_path}')

args = argparse.ArgumentParser()
args.add_argument('link', type=str)
args.add_argument('-p', action='store_true', help=messages.P_MESSAGE)
args.add_argument('-v', action='store_true', help=messages.V_MESSAGE)
args.add_argument('-o', default=save_path, nargs=1, 
                  type=str, help=messages.O_MESSAGE, metavar='[output]')

parsed = args.parse_args()
if isinstance(parsed.o, list):
    save_path = parsed.o[0]

downloader = Download(parsed.link, save_path=save_path)
if parsed.p:
    tryerrors.make_download_treatments(downloader.download_playlist)
    
elif parsed.v:
    tryerrors.make_download_treatments(downloader.download_video)
