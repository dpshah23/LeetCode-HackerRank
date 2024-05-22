# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        print(l1," ",l2)
    
    def __init__(self,data):
        self.data=data
        self.next=None

        


Node1=Solution(15)
Node2=Solution(17)
Node3=Solution(11)
Node4=Solution(12)

Node1.next=Node2
Node2.next=Node3
Node3.next=Node4



        

        