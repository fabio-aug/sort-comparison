from methods.insertion_sort import insertion_sort
from methods.merge_sort import merge_sort
from methods.selection_sort import selection_sort


def create_array(size):
    array_scope = [0] * size

    for j in range(size):
        array_scope[j] = size - j

    return array_scope


def show_result(method_name, result):
    [movements, comparisons, time] = result

    print(f"\n{method_name}")
    print(f"- Movements: {movements}")
    print(f"- Comparisons: {comparisons}")
    print(f"- Time: {time}")


def calculate_insertion(size):
    array = create_array(size)
    result = insertion_sort(array)
    show_result("Insertion Sort", result)


def calculate_merge(size):
    array = create_array(size)
    result = merge_sort(array)
    show_result("Merge Sort", result)


def calculate_selection(size):
    array = create_array(size)
    result = selection_sort(array)
    show_result("Selection Sort", result)


if __name__ == '__main__':
    array_tests_sizes = [100, 1000, 100000]

    for i in range(len(array_tests_sizes)):
        length = array_tests_sizes[i]

        print(f"\nSize: {length} ------------------------------")
        calculate_insertion(length)
        calculate_merge(length)
        calculate_selection(length)
