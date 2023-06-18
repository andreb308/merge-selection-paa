import numpy as np

def mergeSort(myList):
    if len(myList) <= 1:
        return myList

    mid = len(myList) // 2
    left = mergeSort(myList[:mid])
    right = mergeSort(myList[mid:])

    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return np.array(merged)

