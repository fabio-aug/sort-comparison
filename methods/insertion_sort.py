def insertion_sort(array):
    moves = 0
    compare = 0
    time = 0

    for i in range(1, len(array)):
        moves += 1
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            compare += 1
            moves += 1
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key
        moves += 1

    return [moves, compare, time]
