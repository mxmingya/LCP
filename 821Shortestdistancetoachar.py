import math
from collections import deque
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        sPosi = []
        hash = {}
        for i in range(len(S)):
            c = S[i]
            if c == C:
                sPosi.append(i)
        # print(sPosi)
        def helper(posi, sArr):
            res = 1000000
            for i in sArr:
                res = min(res, math.fabs(i-posi) )
            return int(res)
        
        for i in range(len(S)):
            c = S[i]
            if c not in hash.keys():
                hash[c] = deque([])
            hash[c].append(helper(i, sPosi))
            # print("compare result:%d current position:%d" % (curDis, i))
            
        ret = []

        for char in list(S):
            # print("current mini is %d" % hash[char])
            ret.append(hash[char].popleft())
        return ret
            
                    