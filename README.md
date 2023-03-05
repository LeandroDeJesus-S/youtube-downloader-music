# youtube-downloader-music
cli para baixar musicas do youtube

### usage

Instale as dependencias
```bash
$ pip install pytube colorama
```

Baixando por uma playlist
```bash
$ ./yt.py -p https://playlist-url
```

Baixando por um video
```bash
$ ./yt.py -v https://video-url
```

Por padrão os downloads serão salvos em uma pasta "Music" no diretorio do seu usuário, mas é possivel alterar usando a flag -o
```bash
$ ./yt.py -p https://playlist-url -o caminho/de/destino
```
