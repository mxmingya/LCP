def mergeMaps(m1, m2):
    if not m1 or not m2:
        return m2
    for key in m1:
        m2[key] = m1[key]
    for key, value in sorted(m2.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        print("%s, %s" % (key, value))

# mergeMaps({"bobby":"200", "fred": "300"}, {"abby":"250"})

def chooseLunch(l1, l2):
    lunch, index = "YelpWich", 100000000000
    for i in range(len(l1)):
        cur = l1[i]
        if cur in l2:
            if l2.index(cur) + i < index:
                lunch = cur
                index = l2.index(cur) + i
    return lunch

# print(chooseLunch(["a", "b", "c"], ["c", "a"]))

def compressString(string):
    res = ""
    i = 0
    while i < len(string):
        l = 1
        cur = string[i]
        while (i+l < len(string) and string[i+l] ==cur):
            l += 1
        res += str(l)
        res += cur
        
        i += l

    return res
# print(compressString("aaabbc"))
# print(compressString("aaaa"))