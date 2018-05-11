class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = len(nums)
        if not nums and l < 0:
            return 0
        if l == 1:
            return nums[0]
        pmax, nmax, maxi = [0], [0], nums[0]
        
        for i in range(0, l):
            n = nums[i]
            lastP = pmax[i]
            lastN = nmax[i]
            if n < 0:
                pmax.append(0 if lastN == 0 else lastN * n)
                nmax.append(n if lastP == 0 else lastP * n)
                
            elif n > 0:
                pmax.append(n if lastP == 0 else lastP * n)
                nmax.append(n * lastN)
                
            else:#n == 0
                pmax.append(0)
                nmax.append(0)
                
            maxi = max(maxi, pmax[-1])
        
        return maxi
                
        