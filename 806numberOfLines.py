class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        if not S or not widths:
            return [0,0]
        line, cur, least = 1, 0, 100
        for i in range(len(S)):
            curWidth = widths[ord(S[i])-ord('a')]
            if curWidth + cur > 100:
                line += 1
                
                least = cur if least > cur else least
                cur = 0
            cur += curWidth
        least = least if least < cur else cur
        return [line, least]