import argparse

parser = argparse.ArgumentParser(description='Testing parameters')
parser.add_argument('-p1',dest='param1', help='parameter 1')
parser.add_argument('-p2',dest='param2', help='parameter 2')
params = parser.parse_args()
print(params.param1)
print(params.param2)