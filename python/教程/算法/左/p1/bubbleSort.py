#冒泡排序
def swap(arr,i,j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

def sort(arr): 
    # import logging
    if arr == None or len(arr) == 1:
        return arr

    for end in range(len(arr)-1):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                swap(arr,i,i+1)
    return arr
            

test1 = [1,3,2,6,4,1]
test2 = [34,33,33,36,222,11,111]
test3 = [2]
print(sort(test1))
print(sort(test2))
print(sort(test3))

