# 快速排序函数


def partition(a, p, r):
    key = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= key:
            i = i + 1
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    temp = a[i + 1]
    a[i + 1] = a[r]
    a[r] = temp
    return i + 1


def quicksort(a, p, r):
    if p >= r:
        return
    q = partition(a, p, r)
    quicksort(a, p, q - 1)
    quicksort(a, q + 1, r)
# end of