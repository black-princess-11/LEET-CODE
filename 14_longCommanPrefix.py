class Solution(object):
    def longestCommonPrefix(self, strs):
     
     if strs==[]or strs==[""]:
        return ""
     else:
        fisrt=strs[0]
        i=0
        if 1 <= len(strs) <= 200 or 0 <= len(strs[0]) <= 200 and strs[0]==strs[0].lower():
            while i<len(fisrt):
                for s in strs:
                    if i>len(s)-1 or s[i]!=fisrt[i]:
                        return fisrt[:i]
                i+=1
            return fisrt
print(Solution().longestCommonPrefix(strs=["a"]))