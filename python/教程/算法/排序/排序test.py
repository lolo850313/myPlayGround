a = [42, 20, 17, 13, 28, 14, 23, 15]

# for i in range(1,len(a)):
#     for j in range(0, i):
#         if a[i] < a[j]:
#             a[i], a[j] = a[j], a[i]

# for i in range(len(a)):
#     for j in range(1, len(a) - i):
#         print(a)
#         if a[j-1] > a[j]:
#             a[j-1] , a[j] = a[j] , a[j-1]

def quickSort(a):
    if len(a) < 2:
        return a
    pivot = a[0]
    left, right = [], []

    for i in range(1, len(a)):
        if a[i] < pivot:
            left.append(a[i])
        else:
            right.append(a[i])
    return quickSort(left) + [pivot] + quickSort(right)

q = quickSort(a)

print(q)