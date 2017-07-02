def merge_sort(list):
    length=len(list)
    if length<=1:
        return list

    # split
    mid=length//2
    left=merge_sort(list[:mid])
    right=merge_sort(list[mid:])

    # merge
    return merge(left, right)

def merge(left, right):
    left_index=0
    right_index=0
    res=[]
    while left_index<len(left) and right_index<len(right):
        if left[left_index] < right[right_index]:
            res.append(left[left_index])
            left_index+=1
        else:
            res.append(right[right_index])
            right_index+=1
    res+=left[left_index:]
    res+=right[right_index:]
    return res


print merge_sort([49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 5, 4, 62, 99, 98, 54, 56, 17, 18, 23, 34, 15, 35, 25, 53, 51, 111, 123, 234, 321, 245, 543, 126, 160, 156, 451, 156])