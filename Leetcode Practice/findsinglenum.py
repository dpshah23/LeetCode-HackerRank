class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        repeat_num={}
        final_list=[]
        for i in nums:
            if i not in repeat_num.keys():
                repeat_num[i]=1
                final_list.append(i)

            else:
                repeat_num.pop(i)
                final_list.remove(i)

        return final_list
    