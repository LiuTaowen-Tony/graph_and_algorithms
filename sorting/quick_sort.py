def qsort(lst : list, cmp : callable):
    length = len(lst)
    middle = split(lst, 0, length, cmp)

def split(lst, left, right, cmp):
    if left == right:
        return
    pivot = lst[left]
    i = left + 1
    j = right
    while i <= j:
        if cmp(lst[i], pivot) < 0:
            i = i + 1
        else:
            swap(lst, i, j)
            j = j - 1
    swap(lst, left, j)
    split(lst, left, j - 1, cmp)
    split(lst, j + 1, right, cmp)

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def qsort2(lst, cmp):
    length = len(lst)
    if length == 0:
        return
    else:
        pivot, left, right = lst[0], [], []
        for i in lst[1:] : left.append[i] if cmp(i, pivot) <= 0 else right.append[i]
        return qsort2(left) + [pivot] +qsort2(right)