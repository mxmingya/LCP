class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) <= 1:
            return s
        max, left, right = [0], [0], [0]
        def expand( start, end):
            while start>=0 and end<len(s) and s[start] == s[end]:
                if end-start+1>max[0]:
                    max[0] = end-start+1
                    left[0], right[0] = start, end
                    
                start -= 1
                end += 1
        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)
        return s[left[0]:right[0]+1]