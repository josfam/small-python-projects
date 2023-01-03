import random
import time

PAUSE_DURATION = 0.2
ONE_BAR = chr(9608)  # 9608 represents '█'
BAR_WIDTH = 40
DOWNLOAD_SIZE = 4096


def main():
    bytes_downloaded = 0

    while bytes_downloaded < DOWNLOAD_SIZE:
        # "download" a random number of "bytes", then show the progress bar
        bytes_downloaded += random.randint(0, 100)

        # clamp down the "bytes" "downloaded" to stay between 0 and the total bytes
        if bytes_downloaded > DOWNLOAD_SIZE:
            bytes_downloaded = DOWNLOAD_SIZE

        progress_bar = get_progress_bar(bytes_downloaded, DOWNLOAD_SIZE)
        print(progress_bar, end='', flush=True)

        # pause for a while
        time.sleep(PAUSE_DURATION)

        # replace current progress bar with a new one on the same line
        print('\b' * len(progress_bar), end='', flush=True)


def get_progress_bar(bytes_got, total_bytes):
    """Returns a representation of the full progress bar, with all details attached"""
    num_of_bars = int((bytes_got / total_bytes) * BAR_WIDTH)
    empty_space = str(' ' * (BAR_WIDTH - num_of_bars))
    download_percent = get_percent_downloaded(bytes_got, total_bytes)
    return f'[{ONE_BAR * num_of_bars}{empty_space}] {download_percent} ({bytes_got}/{total_bytes})'


def get_percent_downloaded(bytes_got, total_bytes):
    """Returns the percentage of bytes downloaded"""
    percent = round((bytes_got / total_bytes) * 100, 1)
    return str(percent) + '%'


if __name__ == '__main__':
    main()
