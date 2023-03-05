from pytube import YouTube, Playlist
from pathlib import Path
from typing import Literal
import re


class Download:
    def __init__(self, link, save_path) -> None:
        self.link = link
        self.save_path = save_path

    def download_video(self, filetype:Literal['mp3', 'mp4']='mp3') -> None:
        filetype = filetype.lower()
        if filetype not in ['mp3', 'mp4']:
            return print('O tipo deve ser apenas "mp3" ou "mp4".')
        
        video = YouTube(self.link)
        video_name = self.validate_video_name(video.title)
        filename = video_name + f".{filetype}"
        
        print(f'Downloading: \033[33m{video.title}\033[m')
        if filetype == 'mp3':
            video = video.streams.get_audio_only()
        else:
            video = video.streams.get_by_itag(22)
            
        video.download(self.save_path, filename)
        print(f'\033[32m{filename} finalizado!\033[m')
    
    def download_playlist(self, filetype:Literal['mp3', 'mp4']) -> None:
        filetype = filetype.lower()
        if filetype not in ['mp3', 'mp4']:
            return print('O tipo deve ser apenas "mp3" ou "mp4".')
        
        pl = Playlist(self.link)
        for video in pl.videos:
            video_name = self.validate_video_name(video.title)
            filename = video_name + f".{filetype}"
            stream = video.streams
            try:
                print(f'Downloading: \033[33m{video.title}\033[m')
                
                mp3 = filetype == 'mp3'
                audio = stream.get_audio_only() if mp3 else stream.get_by_itag(22)
                audio.download(self.save_path, filename)
            
                print(f'\033[32m{filename}\033[m finalizado!')
            except Exception as Error:
                print(f'Erro no download: {Error}')
        
    def validate_video_name(self, video_name: str):
        exceptions = '\/:*?"<>|'
        name = ''
        for i in video_name:
            if i not in exceptions:
                name += i

        return name


if __name__ == '__main__':
    d = Download('https://youtu.be/wYJ602-hx6o', Path.home() / 'Videos')
    d.download_video()
    