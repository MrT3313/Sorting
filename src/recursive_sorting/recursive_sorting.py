### helper function
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    A_counter = 0
    B_counter = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range( 0, elements ):
        if A_counter >= len(arrA):    
            merged_arr[i] = arrB[B_counter]
            B_counter += 1
        elif B_counter >= len(arrB):  
            merged_arr[i] = arrA[A_counter]
            A_counter += 1
        elif arrA[A_counter] < arrB[B_counter]:  
            merged_arr[i] = arrA[A_counter]
            A_counter += 1
        else:  
            merged_arr[i] = arrB[B_counter]
            B_counter += 1
    return merged_arr

def merge_sort( arr ):
    if len( arr ) > 1:
        left = merge_sort( arr[ 0 : len( arr ) // 2 ] )
        right = merge_sort( arr[ len( arr ) // 2 : ] )
        arr = merge( left, right )   # merge() defined later
    return arr

print(merge_sort([1,4,7,4,2,6,4,7,87,2,54,3]))








# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
    # TO-DO

    # return arr

# def merge_sort_in_place(arr, l, r): 
    # TO-DO

    # return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

    # return arr
