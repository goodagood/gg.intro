
import argparse

parser = argparse.ArgumentParser(description='prepare Static web site by Convert dir of markdown files.')

parser.add_argument('-s', '--source-dir', help="source directories")
parser.add_argument('-t', '--target-dir', help="target directories")
parser.add_argument('--conf', help="configure directories")
parser.add_argument('-d', '--delete-dir',
        help="delete target directorie before-hand if exists")
parser.add_argument('-c', '--cwd',
        help="set working dir, current working dir")
parser.add_argument('-e', '--extension', help="change file extension to ")

#parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')

#parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')


def get_args():
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parser.parse_args()

    #print(args)

    print(get_args())
    #print(args.accumulate(args.integers))
