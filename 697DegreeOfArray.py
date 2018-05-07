def findShortestSubArray(self, nums):
"""
:type nums: List[int]
:rtype: int
"""
    degree = 0
    map = {}

    for i in range(len(nums)):
        n = nums[i]
        if n not in map:
            map[n] = [i]
        else: map[n].append(i)

        degree = degree if len(map[n]) < degree else len(map[n])

    return min(map[k][-1] - map[k][0] + 1 for k in map if len(map[k]) == degree)