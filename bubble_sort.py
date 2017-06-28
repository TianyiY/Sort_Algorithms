def bubble_sort(list):
    length=len(list)
    for i in range(length):
        flag=True
        for j in range(1, length-i):
            if list[j-1]>list[j]:
                flag = False
                list[j-1], list[j]=list[j], list[j-1]

        if flag==True:    # if the former is smaller than the latter, do nothing.
            return list
    return list


print bubble_sort([49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 5, 4, 62, 99, 98, 54, 56, 17, 18, 23, 34, 15, 35, 25, 53, 51])
