#  num_lst = list(map(int, input().split()))
#  num_lst = [8, 11, -6, 3, 0, 1, 1]
num_lst = [2, 1]


def merge_list(a, b):
        c = []
        n = len(a)
        m = len(b)

        i = 0
        j = 0
        while i < n and j < m:
            if a[i] <= b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        c += a[i:] + b[j:]
        return c


def sorting(lst):
    half = len(lst) // 2
    lst1 = lst[:half]
    lst2 = lst[half:]
    if len(lst1) > 1:
        lst1 = sorting(lst1)
    if len(lst2) > 1:
        lst2 = sorting(lst2)
    return merge_list(lst1, lst2)


print(sorting(num_lst))
