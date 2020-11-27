# arr = [6,5,3,1,8,7,2,4]
arr = [49,38,65,97,76,13,27,48,55,4]
n = len(arr)
gap = int(n / 2)
while(gap > 0):
    for i in range(gap,n):
        tmp = arr[i]
        j = i
        #在j前面的间隔为gap的数，如果比j大就往后走，直到j前面的间隔为gap的数都比j大。
        #由于第一次gap取列表长度的一半，所以第一次只会交换2个数。也就不会出现没有充分交换的情况。
        #即j遇到比他小的数，不再往前走，但在它更前面还有更大的数没有被交换到后面
        while( j >= gap and arr[j - gap] > tmp):
            arr[j] = arr[j - gap]
            j -= gap
        arr[j] = tmp
        
    gap = int(gap / 2)
print(arr)


