from pytube import YouTube
from sys import argv
import os

out = os.getcwd() + "/Downloaded/"
link = argv[1]
yt = YouTube(link)

yd = yt.streams.filter(only_audio=True).first()

yd.download(out)
