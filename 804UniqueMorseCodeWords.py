from sets import Set
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        def getIndex(a):
            return ord(a) - ord('a')
        res, set = "", Set()
        
        for word in words:
            set.add("".join(map(lambda n: morse[getIndex(n)], list(word))))
        
        # print(set)
        return len(set)
        
        