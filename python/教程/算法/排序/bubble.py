def bubble_sort(list):
    length = len(list)
    
    for index in range(length):
        for j in range(1, length - index):
            if list[j - 1] > list[j]:
                list[j - 1] , list[j] = list[j], list[j - 1]
    
    return list
