arr = [6,5,3,1,8,7,2,4]
for i in range(1,len(arr)):
    tmp = arr[i]
    j = i
    while( j > 0 and arr[j-1] > tmp):
        #在j前面，比j大的往后走，直到j前面的数都比j小
        arr[j] = arr[j-1]
        j = j - 1
        print(arr)
    arr[j] = tmp
    

