def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if not nums:
        return None
    res, dictionary = [], {}
    for i in nums:
        if i not in dictionary :
            dictionary[i] = 0
        dictionary[i] += 1
    
    bucket = [[]]*len(nums)
    # print("len of buck: %d" % len(bucket))
    # print(bucket)
    for key in dictionary:
        freq = dictionary[key]
        bucket[freq].append(key)
        print(bucket)
    # print(bucket)
    for i in range(len(bucket)-1, len(bucket)-k-1, -1):
        for n in bucket[i]:
            # print(n)
            res.append(n)
    print(res)
    return sorted(res)

topKFrequent([1,1,1,2,2,3], 2)