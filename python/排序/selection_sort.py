def selection_sort(list):
    length = len(list)
    for i in range(length):
        min = i
        for j in range(i+1, length):
            if list[j] < list[min]:
                min = j
                print(list[min] , list[i])
                list[min] , list[i] = list[i], list[min]
    
    return list

selection_sort([3,2,4,1])