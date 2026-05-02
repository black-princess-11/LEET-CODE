# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode(0)
        carry=0
        current=dummy
        while l1 or l2 or carry:
            val1= l1.val if l1 else 0
            val2= l2.val if l2 else 0
            total = val1+val2+carry
            carry= total//10
            current.next=(ListNode(total%10))
            current=current.next
            if l1: l1=l1.next
            if l2: l2=l2.next 
        print(dummy.next)
Solution().addTwoNumbers(l1=ListNode(2, ListNode(4, ListNode(3))), l2=ListNode(5, ListNode(6, ListNode(4))))
'''  def addTwoNumbers(self, l1, l2):
        lr=[]
        add=[]
        for i in range(len(l1)):
            add.append(l1[i]+l2[i])
        for i in range(len(add)):
             if add[i]>9:
                carry=add[i]//10
                add[i]=add[i]%10
                add[i+1]=add[i+1]+carry   
        print(add)
Solution().addTwoNumbers(l1=[2,4,3],l2=[5,6,4])'''
        
        