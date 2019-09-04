# mp4-downloader

import pytube
#i = input("Geben Sie nun Ihren Link ein")
url = 'https://www.youtube.com/watch?v=G-9hWUEjvIU'
youtube = pytube.YouTube(url)
video = youtube.stream.first()
video.download()