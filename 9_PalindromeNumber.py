class Solution(object):
    def isPalindrome(self, x):
        dep=x
        r=0
        while dep>0:
            rem=dep%10
            r=rem+(r*10)
            dep=dep//10
        if r==x:
            return True
        else:            
            return False
print(Solution().isPalindrome(x=-121))
    