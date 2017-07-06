def selection_sort(list):
    length=len(list)
    for i in range(length):
        minimum=i
        for j in range(i+1, length):
            if list[j]<list[minimum]:
                minimum=j
                list[minimum], list[i]=list[i], list[minimum]
    return list

print selection_sort([49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 5, 4, 62, 99, 98, 54, 56, 17, 18, 23, 34, 15, 35, 25, 53, 51])