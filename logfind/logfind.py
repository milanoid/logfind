import argparse

parser = argparse.ArgumentParser(description='Finds string(s) in log files. Takes any number of arguments.')
parser.add_argument('strings', metavar='N', type=str, nargs='+',
                   help='a string(s) to look for')
parser.add_argument('-o', dest='logical OR', action='store_const',
                   const=sum, default=max,
                   help='switch logical operator to OR (AND is default)')

args = parser.parse_args()
print args.accumulate(args.integers)
