from os import system
from pathlib import Path


def verify_default_path(*paths):
    """Verifica se o caminho existe, caso contrario ele sera criado."""
    for path in paths:
        if not Path(path).exists():
            system(f'mkdir {path}')
            
def get_default_path(filetype, mp3path, mp4path):
    if filetype == 'mp4':
        return mp4path
    return mp3path
