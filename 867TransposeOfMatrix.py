class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A:
            return None
        m,n = len(A), len(A[0])
        res = [ [] for x in range(n)]
        print(type(res[0]))
        for i in range(m):
            for j in range(n):
                cur = A[i][j]
                res[j].append(cur)
        return res
                    
                    