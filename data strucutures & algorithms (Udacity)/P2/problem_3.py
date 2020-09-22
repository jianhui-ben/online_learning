## idea:
## create a maxheap to store the input_list
## and then remove the head continuously to create two integers
    
def heapify(arr, n, index):
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    TODO: Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top
    """
    large= index
    left= 2*index+1
    right= 2*index+2
    
    if left<n and arr[left]> arr[index]:
            large= left
    if right<n and arr[right]> arr[large]:
            large= right
        
    if large!= index:
        arr[index], arr[large]= arr[large], arr[index]
        heapify(arr, n, large)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list)==0:
        print('empty list')
        return
    ##create maxheap tree:
    arr=[i for i in input_list if i]
    heapify(arr, len(arr), 0)
    for i in range(len(arr)-1, -1, -1):
        heapify(arr, len(arr), i)
    a,b=[], []
    i=0
    while len(arr)>0:
        if i%2==0:
            a.append(str(arr.pop(0)))
        else:
            b.append(str(arr.pop(0)))
        heapify(arr, len(arr), 0)
        i+=1
    return [int(''.join(a)), int(''.join(b))]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

##test case 1
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)


##test case 2
rearrange_digits([])  ## empty list

rearrange_digits([4, 6, 2, 5, 9, 8])
##test case 3:
rearrange_digits([4, 6, 2, 5, 9, 8, None])  ## ignore the None entry in the list