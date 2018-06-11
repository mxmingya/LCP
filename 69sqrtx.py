class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start, end, preMid = 0, x, -1
        if not x or x <= 0 or x == 1:
            return x
        while start < end:
            mid = start + (end-start)/2
            # print(mid)
            if math.fabs(mid*mid - x) <= 0.5 or preMid == mid:
                return int(math.floor(mid))
            if mid*mid < x:
                start = mid
            else:
                end = mid
            preMid = mid
        return end
        