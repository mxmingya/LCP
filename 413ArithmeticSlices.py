class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)
        if not A or l <= 2:
            return 0
        if l == 3 and A[2]-A[1]==A[1]-A[0]:
            return 1
        res = []
        i = 0
        while i<l-2:
            cur = 2
            a, b, c = i+2, i+1, i
            
            while  a<l and A[a]-A[b]==A[b]-A[c]:
                # print("%d %d %d" % (a,b,c))
                a, b, c =  a+1, a, b
                cur += 1
            if cur > 2:
                i += cur
                res.append(cur)
            else: i+=1
            
        def msum(n):
            re = 0
            for i in range(n-2, 0, -1):
                re += i
            return re
        
        ret = 0
        if not res:
            return 0
        # print(res)
        for n in res:
            ret += msum(n)
            
        return ret
        
        
            
                    
        