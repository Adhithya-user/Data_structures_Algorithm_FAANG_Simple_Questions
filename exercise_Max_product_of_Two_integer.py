def max_product(arr):
    #initialise two variable set value 0
    max1,max2=0,0
    #iterate through the array
    for num in arr:
        #if the current number is greater than max1,update the max1,max2
        if num>max1:
            max2=max1
            max1=num
            #if the current number is greater than max2 but not max1,update max2
        elif num>max2:
            max2=num
    #return the product of two largest integer
    return max1*max2
arr=[1,7,3,4,9,5]
print(max_product(arr))

