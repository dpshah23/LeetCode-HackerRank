# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result=[]
        result=list1+list2
        length=len(result)
        for i in range(len(result)):

            for j in range(0, len(result) - i - 1):

      
                if result[j] > result[j + 1]:
                    temp = result[j]
                    result[j] = result[j+1]
                    result[j+1] = temp
        
        return result
    

obj1=Solution()
print(obj1.mergeTwoLists([1,356,86],[221,64,2]))