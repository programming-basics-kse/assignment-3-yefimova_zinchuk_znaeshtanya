import argparse
from main import installer
installer()
parser = argparse.ArgumentParser()
parser.add_argument('--total','-t', nargs = +1, type=int, help= 'file to count total')
args = parser.parse_args()
result = None
if args.total:
    pass