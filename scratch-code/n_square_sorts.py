def selection_sort(arr):
    """Refresher implementation of selection sort - in-place & stable.

    :param arr: List of integers to sort
    :return: Sorted list
    """
    for i in range(len(arr)):
        min = i
        # selecting index of smallest number
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j
        # swaping current index with smallest number
        arr[i], arr[min] = arr[min], arr[i]
    return arr

def insertion_sort(arr):
    """Refresher implementation of inserstion sort - in-place & stable.

    :param arr: List to be sorted.
    :return: Sorted list.
    """
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i
        # find the position for insertion
        for j in range(i, len(arr)):
            # the position is found if the prev element is smaller than current
            if arr[j - 1] < tmp:
                break
            # shift to the right
            arr[j] = arr[j - 1]
        arr[j] = tmp
    return arr

def bubble_sort(arr):
    """Refresher implementation of buble-sort - in-place & stable.
    
    :param arr: List to be sorted.
    :return: Sorted list.
    """
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            # check if elements are in relative out-of-order
            if arr[j] > arr[j + 1]:
                # swapping adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [23, 12, 3, 9, 7, 1, 13, 10]
    print("original", arr)
    print("selection-sort", selection_sort(arr))
    print("insertion-sort", insertion_sort(arr))
    print("bubble-sort", bubble_sort(arr))
