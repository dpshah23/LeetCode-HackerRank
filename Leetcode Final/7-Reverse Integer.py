class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed_num = 0
        is_negative = x < 0
        x = abs(x)
        
        while x != 0:
            mod = x % 10
            reversed_num = reversed_num * 10 + mod
            x //= 10
        
        if is_negative:
            reversed_num = -reversed_num

        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num
