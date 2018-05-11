class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        l = len(s)
        right, dic = [0], set(wordDict)
        for i in range(1, l+1):
            for start in right:
                if i <= start: continue
                if s[start:i] in wordDict:
                    right.append(i)
                    if i == l:
                        return True
                    break
        return False