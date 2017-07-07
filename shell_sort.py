def shell_sort(list):
    length=len(list)
    # initial step length
    step_len=int(round(length/2))
    while step_len>0:
        for i in range(step_len, length):
            # insertion sort at each step length
            temp=list[i]
            j=i
            while j>=step_len and list[j-step_len]>temp:
                list[j]=list[j-step_len]
                j-=step_len
            list[j]=temp
        #update step length
        step_len=int(round(step_len/2))
    return list

print shell_sort([49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 5, 4, 62, 99, 98, 54, 56, 17, 18, 23, 34, 15, 35, 25, 53, 51])

