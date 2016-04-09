

def _merge_arr(arr, l, m, u):

    lower = arr[l:m]
    upper = arr[m:u]

    lower.append(1e309)
    upper.append(1e309)
    cur_l = 0
    cur_u = 0

    for val in range(l, u):
        if lower[cur_l] <= upper[cur_u]:
            arr[val] = lower[cur_l]
            cur_l = cur_l + 1
        else:
            arr[val] = upper[cur_u]
            cur_u = cur_u + 1


def merge_sort(arr, lower, upper):

    middle = (lower + upper) / 2

    if upper - lower > 1:
        merge_sort(arr, lower, middle)
        merge_sort(arr, middle, upper)

    _merge_arr(arr, lower, middle, upper)

    return arr

def insertion_sort(numbs):
    sorted_numbs = numbs
    for cur_index in range(1, len(numbs)):
        cur_val = sorted_numbs[cur_index]

        lookup_index = cur_index - 1

        while lookup_index >= 0 and sorted_numbs[lookup_index] >= cur_val:
            sorted_numbs[lookup_index + 1] = sorted_numbs[lookup_index]
            lookup_index -= 1
        sorted_numbs[lookup_index + 1] = cur_val

    return sorted_numbs
