    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if not nums or l  == 0:
            return 0
        
        max = 0
        res = nums[0]
        for n in nums:
            max = n + max if n + max > 0 else 0
            if res < 0 and max == 0:
                res = n if res < n else res
                continue
            res = max if max > res else res
        
        return res