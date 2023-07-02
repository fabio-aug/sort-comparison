def selection_sort(array):
    moves = 0
    compare = 0
    time = 0

    for step in range(len(array)):
        moves += 1
        min_idx = step

        for i in range(step + 1, len(array)):
            compare += 1
            if array[i] < array[min_idx]:
                min_idx = i

        moves += 2
        (array[step], array[min_idx]) = (array[min_idx], array[step])

    return [moves, compare, time]
