import subprocess
import logging
#  from run import set_label_success, set_label_downloading, set_label_failed, set_label_updating

logger = logging.getLogger(__name__)  # now we use logger.debug, etc.
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(style="{", fmt="{asctime} [{levelname}] {message}", datefmt="%d.%m.%Y %H:%M:%S")

file_handler = logging.FileHandler('shell_controller.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# deprecated
def output_format_information(link):

    x = "youtube-dl -F " + link + " --no-playlist"
    resolutions = (subprocess.Popen(x, shell=False, stdout=subprocess.PIPE).stdout.read())
    lines = resolutions.decode('UTF-8').replace(" ", ".").splitlines()

    formatted_lines = []
    for line in lines:
        line.strip()
        if "[" in line or "format" in line:
            lines.remove(line)
            continue

        formatted_lines.append(line)

    # todo: fix this!
    # todo: first thing about another method with "medium, best, etc" in console
    elems = []
    for line in formatted_lines:
        line = line.replace(".*", ", ")
        line = line.replace(".", "")

        print(line)


    return formatted_lines


def update_ydl():
    #  set_label_updating()
    logger.debug("Enter update_ydl()")
    subprocess.Popen("pip install --upgrade youtube-dl", shell=False, stdout=subprocess.PIPE).wait()


def duration_information(link):
    pass


def quick_mp3_download(link):
    console_text = "youtube-dl --extract-audio --audio-format mp3 " + link
    download(console_text)


def quick_mp4_download(link):
    console_text = "youtube-dl -f best " + link
    download(console_text)


def download(input):
    logger.debug(input)
    #set_label_downloading()
    try:
        subprocess.Popen(input, shell=False, stdout=subprocess.PIPE).wait()
        logger.info("Download succeeded")
    except:
        logger.exception("Download failed")

    #set_label_success()

class Controller():
    pass



# valid examples
# youtube-dl -f best 'http://www.youtube.com/watch?v=P9pzm5b6FFY'

# https://www.youtube.com/watch?v=VpwCnylNdLk
# https://www.youtube.com/watch?v=ekL2qVdOR98
