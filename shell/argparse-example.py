import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help')
parser.add_argument('--version', action='version', version='%(prog)s 2.0')
parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
args = parser.parse_args()

