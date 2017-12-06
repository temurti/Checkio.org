def largest_histogram(arr):
    area = 0
    i = 0
    index = []

    while i <= len(arr):
        if not index or (i < len(arr) and arr[i] > arr[index[-1]]):
            index.append(i)
            i += 1
        else:
            last = index.pop()
            if not index:
                area = max(area, arr[last] * i)
            else:
                area = max(area, arr[last] * (i - index[-1] - 1))
    return area
#
if __name__ == "__main__":
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
