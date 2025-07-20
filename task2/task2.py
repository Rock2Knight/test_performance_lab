import sys
from pathlib import Path
from decimal import Decimal, getcontext

getcontext().prec = 38

file1 = Path(sys.argv[1]).resolve()
file2 = Path(sys.argv[2]).resolve()

center = None
radius = None

with open(file1, 'r') as f1:
    center = [Decimal(x) for x in f1.readline().strip().split(' ')]
    radius = Decimal(f1.readline().strip())

with open(file2, 'r') as f2:
    for line in f2:
        point = [Decimal(x) for x in line.strip().split(' ')]
        left_part = (point[0] - center[0])**2 + (point[1] - center[1])**2
        if left_part < radius**2:
            print('1')
        elif left_part == radius**2:
            print('0')
        else:
            print('2')
