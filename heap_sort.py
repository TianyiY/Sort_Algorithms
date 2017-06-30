def shift_down(list, first, last):
    # consider the first element is the root (should be the largest one)
    root=first
    while True:
        child=2*root+1
        if child>last:
            break
        if child+1<=last and list[child]<list[child+1]:
            child+=1
        if list[root]<list[child]:
            list[root], list[child]=list[child], list[root]
            root=child
        else:
            break

def heap_sort(list):
    length=len(list)
    # create max heap
    for first in range((length-2)//2, -1, -1):
        shift_down(list, first, length-1)
    # heap sort
    for last in range(length-1, 0, -1):
        list[0], list[last]=list[last], list[0]
        shift_down(list, 0, last-1)
    return list


print heap_sort([49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 5, 4, 62, 99, 98, 54, 56, 17, 18, 23, 34, 15, 35, 25, 53, 51, 111, 123, 234, 321, 245, 543, 126, 160, 156, 451, 156])
