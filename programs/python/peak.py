def find_peak(array):
    mid = int(len(array)/2)
    # print("ELEMENT", array[mid])
    print("CUUR array", array)
    print("MID", mid)
    # print( "array[mid] <= array[mid-1]",array[mid], array[mid-1])
    # print( "array[mid] <= array[mid+1]",array[mid], array[mid+1])

    if len(array) == 2:
        if array[0] > array[1]:
            return array[0]
        else:
            if array[0] != array[1]:
                return  array[1]
            else:
                return None
    if array[mid] < array[mid-1]:
        return find_peak(array[:mid+1])
    elif array[mid]< array[mid+1]:
        return find_peak(array[mid:])
    else:
        print("LAST", array[mid])
        # return array[mid]
        return find_peak(array[mid:])

# array = [2,5,10,20,30]
# array = [1,2,3]
# array = [3,2,1]
# array = [1,2, 1]
# array = [1,0, 1]
# array = [1,5, 1]
array = [1,1, 1]
print("Peak is" ,find_peak(array))
