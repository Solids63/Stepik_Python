import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_1 = (tuple(map(str, i.split('='))) for i in lst_in)

b = tuple(lst_1)

lst = list(filter(lambda x: int(x[1]) > 500, b))

n = list(map(lambda y: y[0], lst))

print(*n)
