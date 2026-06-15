class Solution(object):
    def isValid(self, s):
       d={"(":")", "[":"]", "{":"}"}
       if 1 <= len(s) <= 10**4:
              stack=[]
              for i in s:
                if i in d:
                     stack.append(i)
                elif len(stack)==0 or d[stack.pop()]!=i:
                     return False
              return len(stack)==0
print(Solution().isValid(s="("))