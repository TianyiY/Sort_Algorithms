def insertion_sort(list):
    length=len(list)
    for i in range(1, length):
        # compare the former and latter element, if the latter is smaller than the former
        if list[i]<list[i-1]:
            # retrieve the number, and store its index
            temp=list[i]
            index=i
            # compare backwards
            for j in range(i-1, -1, -1):
                if list[j]>temp:
                    list[j+1]=list[j]
                    index=j
                else:
                    break
            list[index]=temp
    return list

print insertion_sort([49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 5, 4, 62, 99, 98, 54, 56, 17, 18, 23, 34, 15, 35, 25, 53, 51])


