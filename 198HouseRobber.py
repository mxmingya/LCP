class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        rob = 0
        notRob = 0
        
        for n in nums:
            temp = notRob
            notRob = max(temp, rob)
            rob = n + temp
                
        return max(rob, notRob)