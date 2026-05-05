class Solution(object):
    def gcdOfStrings(self, str1, str2):
        s1=list(str1.upper())
        s2=list(str2.upper())
        sl=[]
        for i in range(len(s1)):
            if s1[i] in s2:
                    sl.append(s1[i])
        for i in range(len(s2)):
            if s2[i] in s1:
                    sl.append(s2[i])
        newsl=str("".join(sl))
        return newsl
     
print(Solution().gcdOfStrings(str1="ABCABC",str2="ABC"))    