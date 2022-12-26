def findZigZagSequence(arr):
    arr.sort()
    n = len(arr)
    mid = int((n + 1) / 2)
    arr[mid], arr[n - 1] = arr[n - 1], arr[mid]

    st = mid + 1
    ed = n - 1
    while (st < ed):
        arr[st], arr[ed] = arr[ed], arr[st]
        st = st + 1
        ed = ed + 1


    return arr


if __name__=="__main__":
    findZigZagSequence(arr=[2,3,5,1,4])