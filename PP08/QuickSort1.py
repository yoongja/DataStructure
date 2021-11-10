def partition(values, first, last):
    pivot = values[first]
    low = first + 1
    high = last

    while True:
        while low <= high and values[high] >= pivot:
            high = high - 1
        while low <= high and values[low] <= pivot:
            low = low + 1

        if low <= high:
            values[low], values[high] = values[high], values[low]
        else:
            break

    values[first], values[high] = values[high], values[first]

    return high


def quick_sort(values, first, last):
    if first < last:
        pivot = partition(values, first ,last)
        quick_sort(values, first, pivot-1)
        quick_sort(values, pivot+1, last)
    return values
