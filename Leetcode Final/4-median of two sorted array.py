class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        final_list=nums1+nums2

        final_list.sort()

        n=len(final_list)
        # for i in range(n-1):
        #     swapped = False
        #     for j in range(0, n-i-1):
        #         if final_list[j] > final_list[j + 1]:
        #             swapped = True
        #             final_list[j], final_list[j + 1] = final_list[j + 1], final_list[j]


        
        if n%2==0:
            median = (final_list[n // 2 - 1] + final_list[n // 2]) / 2.0

            return median

        else:
            median=n//2

            return final_list[median]