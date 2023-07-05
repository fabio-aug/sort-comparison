import random

from methods.insertion_sort import insertion_sort
from methods.merge_sort import merge_sort
from methods.selection_sort import selection_sort


def create_array(size, type_order):
    array_scope = [0] * size

    # Types: ["OrdC", "OrdD", "OrdA"]
    if type_order == "OrdC":
        for c in range(size):
            array_scope[c] = c
    elif type_order == "OrdD":
        for d in range(size):
            array_scope[d] = size - d
    elif type_order == "OrdA":
        for a in range(size):
            array_scope[a] = random.randint(1, size)

    return array_scope


def show_result(method_name, result):
    [movements, comparisons, time] = result

    print(f"\n{method_name}")
    print(f"- Movements: {movements}")
    print(f"- Comparisons: {comparisons}")
    print(f"- Time: {time}")


def calculate_insertion(array_values):
    result = insertion_sort(array_values)
    show_result("Insertion Sort", result)


def calculate_merge(array_values):
    result = merge_sort(array_values)
    show_result("Merge Sort", result)


def calculate_selection(array_values):
    result = selection_sort(array_values)
    show_result("Selection Sort", result)


if __name__ == '__main__':
    array_tests_order = ["OrdC", "OrdD", "OrdA"]
    array_tests_sizes = [100, 1000, 100000]

    for i in range(len(array_tests_order)):
        order = array_tests_order[i]

        print(f"\nOrder: {order} ------------------------------")

        for j in range(len(array_tests_sizes)):
            length = array_tests_sizes[j]
            array = create_array(length, order)

            print(f"\nSize: {length} ------------------------------")

            calculate_insertion(array.copy())
            calculate_merge(array.copy())
            calculate_selection(array.copy())
