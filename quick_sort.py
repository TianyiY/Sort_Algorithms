def quick_sort(list):
    left=[]
    pivots=[]
    right=[]
    length=len(list)

    if length<=1:
        return list     # exit recursion
    else:
        pivot=list[0]
        for i in list:
            if i<pivot:
                left.append(i)
            elif i>pivot:
                right.append(i)
            else:
                pivots.append(i)

        # recursion
        left=quick_sort(left)
        right=quick_sort(right)
        return left+pivots+right


def quick_sort_easy(list):
    if len(list)<=1:
        return list
    else:
        pivot=list[0]
        return quick_sort_easy([i for i in list[1:] if i<pivot]) + [pivot] + quick_sort_easy([j for j in list[1:] if j>=pivot])


print quick_sort([49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 5, 4, 62, 99, 98, 54, 56, 17, 18, 23, 34, 15, 35, 25, 53, 51, 111, 123, 234, 321, 245, 543, 126, 160, 156, 451, 156])

print quick_sort_easy([49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 5, 4, 62, 99, 98, 54, 56, 17, 18, 23, 34, 15, 35, 25, 53, 51, 111])