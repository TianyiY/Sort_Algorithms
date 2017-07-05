def radix_sort(list):
    radix = 10
    maxLength = False
    placement =1

    while not maxLength:
        maxLength = True
        # initialize buckets
        buckets = [[] for n in range(radix)]

        # split list between lists
        for i in list:
            tmp = i // placement
            buckets[tmp % radix].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        # empty lists into list array
        a = 0
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                list[a] = i
                a += 1

        # move to next digit
        placement *= radix
    return list


print radix_sort([49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 5, 4, 62, 99, 98, 54, 56, 17, 18, 23, 34, 15, 35, 25, 53, 51, 111, 123, 234, 321, 245, 543, 126, 160, 156, 451, 156])
