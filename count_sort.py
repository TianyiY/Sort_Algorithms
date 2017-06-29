def count_sort(list):
    import numpy
    minimum=numpy.inf
    maximum=0
    # retrieve the min and max value
    for i in list:
        if i < minimum:
            minimum=i
        if i > maximum:
            maximum=i

    count_list=[0]*(maximum-minimum+1)
    for i in list:
        count_list[i-minimum]+=1

    index=0
    for i in range(maximum-minimum+1):
        for j in range(count_list[i]):
            list[index]=i+minimum
            index+=1
    return list


print count_sort([49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 5, 4, 62, 99, 98, 54, 56, 17, 18, 23, 34, 15, 35, 25, 53, 51, 111, 123, 234, 321, 245, 543, 126, 160, 156, 451, 156])
