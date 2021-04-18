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
        print(partition, pivot, arr)
        quicksort(arr, left, partition - 1, is_asc)
        quicksort(arr, partition + 1, right, is_asc)


def main():
    arr = [2, 6, 3, 1, 0, 8, 12, 4, 8, 5, 9, 49, 10, 2, 3, 5, 6, -1]
    quicksort(arr, 0, len(arr) - 1, False)
    print('sorted array = {}'.format(arr))


main()
