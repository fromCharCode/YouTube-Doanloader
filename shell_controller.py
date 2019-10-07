import subprocess


def output_format_information(link):

    x = "youtube-dl -F " + link + " --no-playlist"
    resolutions = (subprocess.Popen(x, shell=True, stdout=subprocess.PIPE).stdout.read())
    #print(resolutions.decode('UTF-8'))
    lines = resolutions.decode('UTF-8').replace(" ", ".").splitlines()

    formatted_lines = []
    for line in lines:
        line.strip()
        if "[" in line or "format" in line:
            lines.remove(line)
            continue

        formatted_lines.append(line)

    # todo: fix this!
    elems = []
    for line in formatted_lines:
        line = line.replace(".*", ", ")
        line = line.replace(".", "")

        print(line)


    return formatted_lines

def duration_information(link):
    pass


def quick_mp3_download(link):
    # the way below can download youtube mp3 without ffmpeg
    x = "youtube-dl --extract-audio --audio-format mp3 " + link
    print(x)
    # label will download from here "downloading..."
    subprocess.Popen(x, shell=True, stdout=subprocess.PIPE).wait()
    print("Download finished")
    # label needs to change here!

def quick_mp4_download(link):
    x = "youtube-dl -f best " + link
    print(x)
    # label will download here..
    subprocess.Popen(x, shell=False, stdout=subprocess.PIPE).wait()
    print("Download finished")
    # l c

# youtube-dl -f best 'http://www.youtube.com/watch?v=P9pzm5b6FFY'

# https://www.youtube.com/watch?v=VpwCnylNdLk
# https://www.youtube.com/watch?v=ekL2qVdOR98
