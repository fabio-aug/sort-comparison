from datetime import datetime

moves = 0
compare = 0


def merge(array, left, mid, right):
    global moves
    global compare

    left_size = mid - left + 1
    right_size = right - mid

    left_array = [0] * left_size
    right_array = [0] * right_size

    for i in range(0, left_size):
        moves += 1
        left_array[i] = array[left + i]

    for j in range(0, right_size):
        moves += 1
        right_array[j] = array[mid + 1 + j]

    i = 0
    j = 0
    k = left

    compare += 1
    while i < left_size and j < right_size:
        compare += 2
        if left_array[i] <= right_array[j]:
            moves += 1
            array[k] = left_array[i]
            i += 1
        else:
            moves += 1
            array[k] = right_array[j]
            j += 1
        k += 1

    compare += 1
    while i < left_size:
        compare += 1
        moves += 1
        array[k] = left_array[i]
        i += 1
        k += 1

    compare += 1
    while j < right_size:
        compare += 1
        moves += 1
        array[k] = right_array[j]
        j += 1
        k += 1


def sort(array, left, right):
    global compare
    compare += 1
    if left < right:
        mid = left + (right - left) // 2

        sort(array, left, mid)
        sort(array, mid + 1, right)
        merge(array, left, mid, right)


def merge_sort(array):
    global moves
    global compare

    moves = 0
    compare = 0
    time = datetime.now()

    sort(array, 0, len(array) - 1)

    time = datetime.now() - time
    return [moves, compare, time]
