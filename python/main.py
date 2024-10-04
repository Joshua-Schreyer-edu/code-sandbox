"""
https://open.kattis.com/problems/dragafra
"""

import sys

def get_input(this_input):
    if this_input+1 < len(sys.argv):
        return sys.argv[this_input+1]
    else:
        return input()

def main():
    number1 = int(get_input(0))
    number2 = int(get_input(1))
    print(number1 - number2)


if __name__ == "__main__":
    main()