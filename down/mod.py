from pytube import YouTube, Playlist
from pathlib import Path

save_path = Path.home() / 'Music'

class Download:
    def __init__(self, link, save_path=save_path) -> None:
        self.link = link
        self.save_path = save_path

    def download_video(self) -> None:
        video = YouTube(self.link)
        filename = video.title + ".mp3"
        print(f'Downloading: \033[33m{video.title}\033[m')
        audio = video.streams.get_audio_only()
        audio.download(self.save_path, filename)
        print(f'\033[32m{filename} finalizado!\033[m')
    
    def download_playlist(self) -> None:
        pl = Playlist(self.link)
        for video in pl.videos:
            filename = video.title + ".mp3"
            try:
                print(f'Downloading: \033[33m{video.title}\033[m')
                audio = video.streams.get_audio_only()
                audio.download(self.save_path, filename)
                print(f'\033[32m{filename}\033[m finalizado!')
            except Exception as Error:
                print(f'Erro no download: {Error}')
