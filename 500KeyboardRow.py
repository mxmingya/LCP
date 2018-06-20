import re
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1, row2, row3 = "[qwertyuiop]*", "[asdfghjkl]*", "[zxcvbnm]*"
        regex = "(?i)(" + row1+"|"+row2+"|"+row3 + ")$"
        res = []
        for word in words:
            if re.match(regex, word):
                res.append(word)
        return res

        # print('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$'==                               '(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$')
        # return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)

            
            
        
            
        
        
        