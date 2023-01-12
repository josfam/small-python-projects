"""Program that generates numbers from the Collatz Sequence,
from the user-provided number,n, up to 1"""

import time
from collections import deque
import rich

UP_ARROW = '\u2B08'
DOWN_ARROW = '\u2B0A'
LEFT_BRACKET = '\u27E6'
RIGHT_BRACKET = '\u27E7'
LONG_WAIT = 0.8
SHORT_WAIT = 0.3


def main():
    while True:
        start_num = int(input("Enter a starting number (greater than 0) or QUIT:\n> "))
        if start_num <= 0:
            continue
        break

    pairs = deque()

    for i, num in enumerate(get_collatz_numbers(start_num)):
        # show the starting number as well
        if i == 0:
            print(f'{LEFT_BRACKET}{num}{RIGHT_BRACKET} ', end='', flush=True)

        pairs.append(num)

        # only get arrows if there is a pair of numbers to look at
        if not len(pairs) == 2:
            continue
        else:
            prev_num = pairs[0]
            current_num = pairs[1]
            arrows = get_arrows(prev_num, current_num)
            time.sleep(LONG_WAIT)
            rich.print(f'{arrows} ', end='', flush=True)
            time.sleep(SHORT_WAIT)
            print(f'{LEFT_BRACKET}{current_num}{RIGHT_BRACKET} ', end='', flush=True)
            pairs.popleft()


def get_collatz_numbers(n):
    """Returns collatz numbers, one at a time, from n to 1"""
    # keep the first number as well
    yield n

    while True:
        if n == 1:
            break
        elif n % 2 == 0:
            # for the even case
            n = n // 2
            yield n
        else:
            # for the odd case
            n = n * 3 + 1
            yield n


def get_arrows(prev_num, current_num) -> str:
    """Returns how many arrows (representing the absolute difference) there are between two numbers.
    Upward facing arrows represent an increase between the two numbers.
    Downward facing arrows represent a decrease between the two numbers."""

    arrow_count = abs(current_num - prev_num)
    if current_num < prev_num:
        return '[bold hot_pink]{}[/bold hot_pink]'.format(DOWN_ARROW * arrow_count)
    else:
        return '[bold green]{}[/bold green]'.format(UP_ARROW * arrow_count)


if __name__ == "__main__":
    main()
