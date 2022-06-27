import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))


def convert(lst1):
    for el in lst1:
        for i in range(len(el)):
            el[i] = int(el[i])
    return lst1


lst = list(map(lambda s: list(s.split()), lst_in))

lst2D = convert(lst)

# регение в строку lst2D = [list(map(int, i.split())) for i in lst_in]
