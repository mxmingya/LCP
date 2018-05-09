class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res = []
        l = len(S)
        i=0
        while(i<l):
            point = i
            while point < l-1 and S[point] == S[point+1]:
                point += 1
            if point-i >= 2:
                res.append([i, point])
            
            i = point if i < point else i+1
        return res