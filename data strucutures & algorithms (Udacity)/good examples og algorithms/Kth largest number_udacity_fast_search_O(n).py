#Given an unsorted array Arr with n positive integers. Find the  𝑘𝑡ℎ  smallest element in the given array, using Divide & Conquer approach.

#Input: Unsorted array Arr and an integer k where  1≤𝑘≤𝑛 
#Output: The  𝑘𝑡ℎ  smallest element of array Arr

##my code
def fastSelect(Arr, k):
    '''TO DO'''
    # Implement the algorithm explained above to find the k^th lasrgest element in the given array
    if len(Arr)==1:
        return Arr[0]
    if len(Arr)>=5:
        num_groups= len(Arr)//5
    else: num_groups=1
    groups=[[] for i in range(num_groups)]
    for i, v in enumerate(Arr):
        groups[i%num_groups].append(v)
    median=[]
    for group in groups:
        group.sort()
        if len(group)>=5:
            median.append(group[2])
        else:
            median.append(group[0])
    if len(median)==1:
        pivot= median[0]
    else:
        pivot= fastSelect(median, len(Arr)/10)

    pre, piv, post = [], [], []
    for num in Arr:
        if num<pivot:
            pre.append(num)
        elif num>pivot:
            post.append(num)
        else: piv.append(num)
    if k<=len(pre):
        return fastSelect(pre, k)
    elif k>len(pre)+len(piv):
        return fastSelect(post, k-len(pre)-len(piv))
    else:
        return pivot
  
    
    #Udacity solution code:
    def fastSelect(Arr, k):                         # k is an index
    n = len(Arr)                                # length of the original array
    
    if(k>0 and k <= n):                         # k should be a valid index         
        # Helper variables
        setOfMedians = []
        Arr_Less_P = []
        Arr_Equal_P = []
        Arr_More_P = []
        i = 0
        
        # Step 1 - Break Arr into groups of size 5
        # Step 2 - For each group, sort and find median (middle). Add the median to setOfMedians
        while (i < n // 5):                     # n//5 gives the integer quotient of the division 
            median = findMedian(Arr, 5*i, 5)    # find median of each group of size 5
            setOfMedians.append(median)         
            i += 1

        # If n is not a multiple of 5, then a last group with size = n % 5 will be formed
        if (5*i < n): 
            median = findMedian(Arr, 5*i, n % 5)
            setOfMedians.append(median)
        
        # Step 3 - Find the median of setOfMedians
        if (len(setOfMedians) == 1):            # Base case for this task
            pivot = setOfMedians[0]
        elif (len(setOfMedians)>1):
            pivot = fastSelect(setOfMedians, (len(setOfMedians)//2))
        
        # Step 4 - Partition the original Arr into three sub-arrays
        for element in Arr:
            if (element<pivot):
                Arr_Less_P.append(element)
            elif (element>pivot):
                Arr_More_P.append(element)
            else:
                Arr_Equal_P.append(element)
        
        # Step 5 - Recurse based on the sizes of the three sub-arrays
        if (k <= len(Arr_Less_P)):
            return fastSelect(Arr_Less_P, k)
        
        elif (k > (len(Arr_Less_P) + len(Arr_Equal_P))):
            return fastSelect(Arr_More_P, (k - len(Arr_Less_P) - len(Arr_Equal_P)))
            
        else:
            return pivot     

# Helper function
def findMedian(Arr, start, size): 
    myList = [] 
    for i in range(start, start + size): 
        myList.append(Arr[i]) 
          
    # Sort the array  
    myList.sort() 
  
    # Return the middle element 
    return myList[size // 2] 

##test cases:
Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
k = 5
print(fastSelect(Arr, k))        # Outputs 12

Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
k = 5
print(fastSelect(Arr, k))        # Outputs 11

Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
print(fastSelect(Arr, k))        # Outputs 99