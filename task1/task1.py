import sys
from itertools import cycle

n = int(sys.argv[1])
m = int(sys.argv[2])
def_list = [x for x in range(1, n + 1)]
cycle_list = cycle(def_list)
res_list = list([1])
i = 1

for elem in cycle_list:
    if i >= m:
        if elem == 1:
            break
        res_list.append(elem)
        i = 2
    else:
        i += 1

for elem in res_list:
    print(elem, end='')