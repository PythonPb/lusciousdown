from os import system as cmd

try:
    import luscious_dl
except ModuleNotFoundError:
    cmd('python -m pip install -U luscious-downloader')


def album(url:str):
    cmd(f'lsd -a {url}')
