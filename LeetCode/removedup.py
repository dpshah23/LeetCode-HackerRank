class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dup_num={}
        finallist=[]
        for i in nums:
            if i not in dup_num.keys():
                finallist.append(i)
                dup_num[i]=1


            else:
                pass

        return len(finallist)


        


obj=Solution()
expected_list=[12,42,65,2,3]
xyz=False
nums=[12,42,65,12,2,3,2,2]
k=obj.removeDuplicates([12,42,65,12,2,3,2,2])
assert k == len(expected_list)
for i in range(len(expected_list)):
    nums[i] == expected_list[i]
    xyz=True

print(xyz)
