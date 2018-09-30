def merge_sort(arr):
    """Refresher implementation of merge-sort - stable.

    :param arr: List to sort
    :return: Sorted list
    """
    # base case: theres 1 or 0 elements in the array - array is sorted!
    if len(arr) <= 1: return arr
    # compute middle index
    m = int(len(arr)/2)
    # apply merge-sort to the left side 0...m-1
    left = merge_sort(arr[0:m])
    # apply merge-sort to the right side m..len-1
    right = merge_sort(arr[m:len(arr)])
    # merge sorted sides
    return merge(left, right)

def merge(left, righ):
    """Merging two sorted lists.
    
    :param left: Sorted list.
    :param right: Sorted list.
    :return: A merged sorted list
    """
    t = len(left) + len(righ) # total items to merge
    f = [] # place holder for final merged list
    l_i, r_i = 0, 0 # initializing left and right index

    # execute until list is full
    while len(f) != t:
        # if all items of left list have been exhausted
        # extend final list with leftovers from right list
        if l_i > len(left) - 1:
            f.extend(righ[r_i:len(righ)])
            break
        # if all items of right list have been exhausted
        # extend final list with leftovers from left list
        if r_i > len(righ) - 1:
            f.extend(left[l_i:len(left)])
            break
        # if current-left is smaller than current-right - add to final list
        if left[l_i] < righ[r_i]:
            f.append(left[l_i]) # adding current left
            l_i += 1 # incrementig left-index
        else:
            f.append(righ[r_i]) # adding current right
            r_i += 1 # incrementing right-index
    return f

if __name__ == '__main__':
    arr = [23, 12, 3, 9, 7, 1, 13, 10]
    print("merge_sort", merge_sort(arr))
