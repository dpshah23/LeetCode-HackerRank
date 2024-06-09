class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def int_to_bin(n) :
            if n==0:
                return 0
            binary = ''
            while (n>0):
                binary = str(n%2)+binary
                n = n//2
            return binary
        def ispallindrome(n):
            binaryn = int_to_binary(n)
            if binaryn == binaryn.reverse() :
                return true
            else :
                return false


        