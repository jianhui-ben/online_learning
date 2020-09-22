def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list)==0:
        print('empty list')
        return
    if not number:
        print('target variable is not a number')
        return
    rotation= find_rotate(input_list, 0, len(input_list)-1)  ##binary search to find the rotation index
    if number>input_list[-1]:
        return rotated_array_search_rec(input_list, 0, rotation-1, number)
    else: return rotated_array_search_rec(input_list, rotation, len(input_list)-1, number)

def find_rotate(input_list, start, end):
    mid= (start+ end)//2
    if input_list[mid]>input_list[end] and input_list[mid+1]<=input_list[end]:
        return mid+1
    elif input_list[mid]>input_list[end]:
        return find_rotate(input_list, mid+1, end)
    else:
        return find_rotate(input_list, start, mid)

def rotated_array_search_rec(input_list, start, end, number):
    mid= (start+ end)//2
    if start==end and input_list[mid]!=number:
        return -1
    elif input_list[mid]==number:
        return mid
    elif input_list[mid]<number:
        return rotated_array_search_rec(input_list, mid+1, end, number)
    elif input_list[mid]>number:
        return rotated_array_search_rec(input_list, start, mid-1, number)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")



#test case 1
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

##edge cases
rotated_array_search([], 0)  ##None
rotated_array_search([1,2,3], None)  ##None

