class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        final_list=[]
        
       
        for i in range(len(nums)):
          
            if nums[i]!=val:
                
                final_list.append(nums[i])
            
            

        return len(final_list)



obj=Solution()
print(obj.removeElement([12,42,65,12,2,3,2,2],2))