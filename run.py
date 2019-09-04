from __future__ import unicode_literals
from downloader import Downloader
from cmd_interface import CmdInterface
from file_iterator import FileIterator

# eva
# ask for task
# get input
# path -> iterator read
# else just write what is currently saved
# therefore: getName, getDuration, author, link


ci = CmdInterface
ci.welcome(ci)
c = 1

# switch case for input
while c > 0:
    link = ci.get_link(ci)
    if link == "e":
        c = -1
        break
    elif link == "1":
        link = input("Insert path") # links.txt is currently placeholder
        dl = Downloader
        dl.download_mp3_path(dl, link)
    else:
        dl = Downloader
        dl.download_mp3(dl, link)

