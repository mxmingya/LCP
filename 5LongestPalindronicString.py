def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if not s or len(s) == 0:
        return 0
    
    l = len(s)
    dp = [[False]*(l+1)]*(l+1)
    maxLen = 1
    start = 0
    
    for i in range(l-1, -1, -1):
        for j in range(i, l):
            
            print("------------------------")
            if s[i] == s[j] and (i+1>j-1 or dp[i+1][j-1]):
                dp[i][j] = True
                for k in range(l+1):
                    print(dp[k])
                print("now %d %d is true, maxLen: %d" % (i,j, j-i+1>maxLen))
                if j-i+1 > maxLen:
                    maxLen = j-i+1
                    start = i
                    print("len is %d i %d j %d" % (maxLen, i, j))
    
    return s[start:start+maxLen]

print(longestPalindrome("abcda"))