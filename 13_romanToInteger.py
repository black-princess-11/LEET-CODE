class Solution(object):
    def romanToInt(self, s):
       sy=[("I",1),("V",5),("X",10),("L",50),("C",100),("D",500),("M",1000)]
       d=dict(sy)
       ns=list(s.upper())
       number=0
       for i in range(len(ns)):
           if i>0 and d[ns[i]]>d[ns[i-1]]:
               number+=d[ns[i]]-2*d[ns[i-1]]
           else:
               number+=d[ns[i]] 
       return number
print(Solution().romanToInt(s="IV"))
