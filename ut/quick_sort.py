def partitioning(arr, low, high, is_asc):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if is_asc:
            if arr[j] < pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        else:
            if arr[j] > pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, left, right, is_asc=True):
    if right - left <= 0:
        return
    else:
        pivot = arr[right]
        partition = partitioning(arr, left, right, is_asc)
        # print(partition, pivot, arr)
        quicksort(arr, left, partition - 1, is_asc)
        quicksort(arr, partition + 1, right, is_asc)


def binary_search(arr, left, right, item):
    if right >= left:
        mid = left + (right - left) // 2
        if mid == item:
            return arr[mid]
        elif mid < item:
            return binary_search(arr, mid + 1, right, item)
        else:

            return binary_search(arr, left, mid - 1, item)
    else:
        return -1


def main():
    arr = [2, 6, 3, 1, 0, 8, 12, 4, 8, 5, 9, 49, 10, 2, 3, 5, 6]
    quicksort(arr, 0, len(arr) - 1, True)
    print('sorted array = {}'.format(arr))
    indexed = binary_search(arr, arr[0], arr[len(arr) - 1], 9);
    print('searched array index={}'.format(indexed))


main()
