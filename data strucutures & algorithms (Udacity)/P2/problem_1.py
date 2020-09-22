#Finding the Square Root of an Integer

##  recursion using binary searh
def sqrt(number):
    if not number:
        print('this is not a number')
        return 
    if number<0:
        print('this number does not have square root')
        return
    return sqrt_rec(1, number, number)

def sqrt_rec(low, high, number):
    mid=(low+high)//2
    if mid*mid<=number and (mid+1)*(mid+1)>number:
        return mid
    elif mid*mid<number:
        return sqrt_rec(mid+1, high, number)
    else:
        return sqrt_rec(low, mid-1, number)
    
#test case 1
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

##test case 2:
sqrt(-1)
sqrt(None)


##test case 3
sqrt(1232371827849218)  ##35105153