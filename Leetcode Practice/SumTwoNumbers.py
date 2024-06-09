class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return_list=[]
        flag=0

        len_num=len(nums)
        for i in range(len_num):
            for j in range(len_num-1):
                sum=nums[i]+nums[j]
                if(sum==target):
                    return_list=[i,j]
                    return return_list

        
            