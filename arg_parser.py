import argparse
import sys

def get_args(args):
    parser = argparse.ArgumentParser(description='TicTacToe game!', formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
        '-l',
        '--log',
        action = "store_true",
        help='create log file if log else log to <stderr>'
    )
    return parser.parse_args(args)
