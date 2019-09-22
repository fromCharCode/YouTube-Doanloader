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


def test_audio_download(link):
    x = "youtube-dl -f 137+251 " + link
    subprocess.Popen(x, shell=True, stdout=subprocess.PIPE)


# https://www.youtube.com/watch?v=ekL2qVdOR98
