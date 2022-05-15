def find_min(arr, start, end):
    min_index = start  # !imp, arr index of the minimum element
    min_val = arr[start]  # value at the minimum index, starting value

    for i in range(start, end):
        if arr[i] < min_val:
            min_val = arr[i]
            min_index = i
    return min_val, min_index


def sort_arr(arr):
    for i in range(len(arr)):
        min_val, min_index = find_min(arr, i, len(arr))
        temp = arr[i]  # swap values
        arr[i] = min_val
        arr[min_index] = temp
    return arr


ar1 = [15,7,2]
print('original arr: ', str(ar1))
print('new srr: ', str(sort_arr(ar1)))
