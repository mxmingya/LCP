class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        l = len(s)
        res = [0]
        
        def extendPalindrome(s, start, end):
            while (start >= 0 and end < len(s) and s[start] == s[end]):
                start -= 1
                end += 1
                res[0] += 1
        
        for i in range(l):
            extendPalindrome(s, i, i)
            extendPalindrome(s, i, i+1)
        return res[0]