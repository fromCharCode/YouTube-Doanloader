# todo: yet this class seems to be needed
# it probably should be removed later

import youtube_dl

class Downloader:

    link = ""

    def __init__(self):
        print(self.__str__(), " created") # debug later

    codec = "mp3"  # default

    # do not touch! until you really know what it does and can do
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': codec,
            'preferredquality': '192'
        }],
    }

    def download(self, link):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': self.codec,
                'preferredquality': '192'
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            print("downloader.py: download succeeded!")

    def download_path(self, path, codec):
        self.codec = codec
        with open(path, "r") as file:
            for line in file:
                print(line)
                self.download(self, line)

# MP3

    def download_mp3(self, link):
        self.codec = "mp3"
        self.download(self, link)

    def download_mp3_path(self, path):
        print("before opening file")
        with open(path, "r") as file:
            for line in file:
                print(line)
                self.download_mp3(self, line)

# MP4
    # stop it right here. we need to find an design pattern!
