import sys
from pathlib import Path

def align_list(spisok, avg, i) -> int:
    left = spisok[:avg]
    right = spisok[avg:]
    if len(left) < len(right):
        i += len(left)
    else:
        i += len(right)
    return i


filename = Path(sys.argv[1]).resolve()
spisok = list([])
with open(filename, 'r', encoding='utf-8') as f:
    spisok = [int(x.strip()) for x in f]

spisok = sorted(spisok)
i = 0

while len(set(spisok)) > 1:
    avg = len(spisok) // 2

    if len(spisok) % 2 == 0:
        if len(set(spisok[:avg])) == 1 and len(set(spisok[avg:])) == 1:
            if abs(spisok[avg] - spisok[avg-1]) == 1:
                i = align_list(spisok, avg, i)
                break
    else:
        if len(set(spisok[:avg])) == 1 and len(set(spisok[avg:])) == 1:
            if abs(spisok[avg] - spisok[avg-1]) == 1:
                i = align_list(spisok, avg, i)
                break
        elif len(set(spisok[:avg+1])) == 1 and len(set(spisok[avg+1:])) == 1:
            if abs(spisok[avg+1] - spisok[avg]) == 1:
                i = align_list(spisok, avg+1, i)
                break

    spisok[0] += 1
    spisok[-1] -= 1
    spisok.sort()
    i += 2

print(i)