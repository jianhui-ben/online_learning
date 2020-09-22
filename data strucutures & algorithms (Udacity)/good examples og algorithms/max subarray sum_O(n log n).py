#given an array arr having n integers. You have 
#to find the maximum sum of contiguous subarray among all the possible subarrays

def maxSubArray(arr):
    '''
    param: An array `arr`
    return: The maximum sum of the contiguous subarray. 
    No need to return the subarray itself.
    '''
    return maxSubArrayRecursive(arr, 0, len(arr)-1)

def maxSubArrayRecursive(arr, start, stop):
    if start== stop:
        return arr[start]
    mid= (start+ stop)//2
    L=maxSubArrayRecursive(arr, start, mid)
    R= maxSubArrayRecursive(arr, mid+1, stop)
    C= maxCrossingSum(arr, start, mid, stop)
    return max(C, max(L, R))
    
def maxCrossingSum(arr, start, mid,  stop):
    '''LEFT PHASE - Traverse the Left part starting from mid element'''
    leftSum = arr[mid]                                     # Denotes the sum of left part from mid element to the current element
    leftMaxSum = arr[mid]                                  # Keep track of maximum sum
    
    # Traverse in reverse direction from (mid-1) to start 
    for i in range(mid-1, start-1, -1):                    # The second argument of range is not inclusive. Third argument is the step size.
        leftSum = leftSum + arr[i]
        if (leftSum > leftMaxSum):                         # Update leftMaxSum
            leftMaxSum = leftSum
    
    '''RIGHT PHASE - Traverse the Right part, starting from (mid+1)'''
    rightSum = arr[mid+1]                                  # Denotes the sum of right part from (mid+1) element to the current element
    rightMaxSum = arr[mid+1]                               # Keep track of maximum sum
    
    # Traverse in forward direction from (mid+2) to stop
    for j in range(mid+2, stop+1):                         # The second argument of range is not inclusive
        rightSum = rightSum + arr[j]
        if (rightSum > rightMaxSum):                       # Update rightMaxSum
            rightMaxSum = rightSum

    '''Both rightMaxSum and lefttMaxSum each would contain value of atleast one element from the arr'''
    return (rightMaxSum + leftMaxSum)


# Test your code
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 6

arr = [-4, 14, -6, 7] 
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 15

arr = [-2, -5, 6, -2, -3, 1, 5, -6]
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 7