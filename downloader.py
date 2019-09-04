import youtube_dl

# important: this program has to be tested in console, else it's buggy. the IDE console reacts strange to links.


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

    # we could create a queue in case the program has something to tell, e.g. "succeeded",
    # but the interface is too fast

    # def download_part(begin, end): # looks like an feature.. as plugin.
    # possible pattern. but limited plugins per type, else we get conflicts.(?)

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
            print("download succeded!") # else it crashes in ydl.*

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
