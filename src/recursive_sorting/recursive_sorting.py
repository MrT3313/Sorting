# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    # Data Check
    print(elements)
    print(merged_arr)
    # TODO: -A-
    ## Goal: replace all '0' entries in merge_arr LIST with the appropriately sorted number
    ## Input: 2 individually sorted arrays
    ### Steps
    ### A.1 - create loop for all elements 
    for z in range(elements - 1):

        # A.1.1 # IF CONDITIONAL
        # A.1.1a # A less then B // OR // A == B
        if arrA[0] <= arrB[0]:
            print(z)
            print('A -- less than -- B')
            merged_arr[z] = arrA.pop(0)

            print(merged_arr)
            print(arrA)

            print(merged_arr)
        
        #  A.1.1b # A GREATER THAN B
        elif arrA[0] > arrB[0]:  
            print(z)
            print('A -- GREATER TAN -- B')
            merged_arr[z] = arrB.pop(0)

            print(merged_arr)
            print(arrB)

            print(merged_arr)
        
        #  A.1.1c # ERROR
        else:
            print('ERROR -- Should not have gotten here...')

        # A.1.2 
        # Checking for Empty List
        # This is here with the thought of arrays of different lengths...I would need to find a way to replace a single 0 from the original merged_arr with the rest of the remaining list
        if not arrA: 
            print(merged_arr)
            print(arrB[:z])

            merged_arr[z + 1] = arrB[:z][0]

            print(merged_arr)
        elif not arrB:
            print(merged_arr)
            print(arrA[:z])

            merged_arr[z + 1] = arrA[:z][0]
            
            print(merged_arr)
    # A.2 # Return 
    return merged_arr


print(merge([1,4,7,8],[2,3,6,9] ))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
