class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = {}
        for domain in cpdomains:
            click =int( domain.split(" ")[0])
            first = domain[domain.index(".")+1:]
            
            
            d = domain.split(" ")[1]
            if d not in dic:
                dic[d] = 0
            dic[d] += click
            if first not in dic:
                dic[first] = 0
            dic[first] += click
            if domain.rindex(".") != domain.index("."):
                second = domain[domain.rindex(".")+1:]
                if second not in dic:
                    dic[second] = 0
                dic[second] += click
            
        ret = []
        for d in dic.keys():
            s = ""
            s += str(dic[d]) + " " + d
            ret.append(s)
            # print("key:%s, value:%s " % (d, str(dic[d])))
        return ret
                