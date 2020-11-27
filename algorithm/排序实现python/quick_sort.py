# # arr = [49,38,65,97,76,13,27,48,55,4]
# arr = [0, 5, 3, 2, 2]

def quickSort(arr):
    l = len(arr)
    if l<=1:
        return arr
    else:
        pivot = arr.pop()
        greater, lesser = [], []
        for i in arr:
            if i >pivot:
                greater.append(i)
            else:
                lesser.append(i)
        print("start")
        print(greater)
        print(pivot)
        print(lesser)
        return quickSort(lesser) + [pivot] + quickSort(greater)
arr = [49,38,65,97,76,13,27,48,55,4]
sortArr = quickSort(arr)

#arr排序后会被破坏
print(arr)
print(sortArr)  # [1，3, 5, 6, 8, 19]
