class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left , right+1):
            cur = i
            while cur > 1: 
                curDig = cur % 10
                if curDig != 0 and i % curDig == 0:
                    cur /= 10
                else:
                    break
            if cur <= 1:
                res.append(i)
        return res
            