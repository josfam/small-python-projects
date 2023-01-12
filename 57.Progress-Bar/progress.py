"""Program that simulates a download progress bar on the commandline"""

import argparse
import random
import rich
import time

PAUSE_DURATION = 0.2
ONE_BAR = chr(9608)  # represents █
ONE_DASH = '\u2013'  # represents –
BAR_WIDTH = 40
DEFAULT_DOWNLOAD_SIZE = 1024

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--size', type=int, help="the size of 'data' to be 'downloaded'")
parser.add_argument('-l', '--ladder', action='store_true', help="display the download bar as stacked cumulative chunks")
args = parser.parse_args()

download_size = args.size if args.size else DEFAULT_DOWNLOAD_SIZE
display_mode = '\n' if args.ladder else ''


def main():
    print('Progress bar simulation')
    bytes_downloaded = 0

    while bytes_downloaded < download_size:
        # 'download' a random number of 'bytes', then show the progress bar
        bytes_downloaded += random.randint(0, 100)

        # clamp down the 'bytes' 'downloaded' to stay between 0 and the total bytes
        if bytes_downloaded > download_size:
            bytes_downloaded = download_size

        progress_bar = get_progress_bar(bytes_downloaded, download_size)
        rich.print(f'{progress_bar}{display_mode}', end='', flush=True)

        time.sleep(PAUSE_DURATION)

        # stop if all 'bytes' have been 'downloaded'
        if bytes_downloaded == download_size:
            break

        # replace current progress bar with a new one on the same line
        print('\b' * len(progress_bar), end='', flush=True)


def get_progress_bar(bytes_got, total_bytes):
    """Returns a representation of the full progress bar, with all details attached"""
    num_of_blocks = int((bytes_got / total_bytes) * BAR_WIDTH)
    percent_got = get_percent_downloaded(bytes_got, total_bytes)
    remaining_line = f'{ONE_DASH}' * (BAR_WIDTH - num_of_blocks)
    blocks_got = get_blocks_downloaded(num_of_blocks)
    fractional_progress = get_progress_as_fraction(bytes_got, total_bytes)
    start_cap, end_cap = get_bar_caps()
    return f'{start_cap}{blocks_got}{remaining_line}{end_cap} {percent_got} {fractional_progress}'


def get_blocks_downloaded(num_of_blocks):
    """Returns blocks representing how much 'data' has been 'downloaded'"""
    block_color = f'[green]'
    return f'{block_color}{ONE_BAR}{block_color}' * num_of_blocks


def get_percent_downloaded(bytes_got, total_bytes):
    """Returns the percentage of bytes downloaded"""
    percent_color = f'[green]'
    percent = round((bytes_got / total_bytes) * 100, 1)
    return f'{percent_color}{percent}{percent_color}%'


def get_progress_as_fraction(bytes_got, total_bytes):
    """Returns, as a fraction, the download progress"""
    frac_color = f'[grey74]'
    return f'{frac_color}({bytes_got}/{total_bytes}){frac_color}'


def get_bar_caps():
    """Returns the end caps that are at the beginning and end of the download bar"""
    cap_color = '[grey100]'
    left_cap = f'{cap_color}[{cap_color}'
    right_cap = f'{cap_color}]{cap_color}'
    return (left_cap, right_cap)


if __name__ == '__main__':
    main()
