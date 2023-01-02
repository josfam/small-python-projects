"""Program that generates numbers from the Collatz Sequence,
from the user-provided number,n, up to 1"""


def main():
    while True:
        start_num = int(input("Enter a starting number (greater than 0) or QUIT:\n> "))
        if start_num <= 0:
            continue
        else:
            sequence = get_collatz(start_num)
            print(sequence)
            break


def get_collatz(n):
    """Returns a collatz sequence from n to 1"""
    
    collatz_seq = []

    # keep the first number as well
    collatz_seq.append(str(n))

    while True:
        if n == 1:
            break
        elif n % 2 == 0:
            # for the even case
            n = n // 2
            collatz_seq.append(str(n))
        else:
            # for the odd case
            n = n * 3 + 1
            collatz_seq.append(str(n))

    return ', '.join(collatz_seq)


if __name__ == "__main__":
    main()
