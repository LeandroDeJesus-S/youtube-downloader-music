from pytube import exceptions

def make_download_treatments(func, *args):
    try:
        func(*args)
    except (exceptions.RegexMatchError, KeyError):
        print(f'\033[31mErro no download, verifique se a url está correta...\033[m')
    except exceptions.VideoPrivate:
        print(f'\033[31mErro no download, o video ou playlist é privado.\033[m')
    except exceptions.MaxRetriesExceeded:
        print(f'\033[31mErro no download, máximo de tentativas excedidas.\033[m')
    except Exception as error:
        print(f'\033[31mErro:\033[m', error)
