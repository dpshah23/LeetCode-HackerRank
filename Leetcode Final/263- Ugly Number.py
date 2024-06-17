class Solution(object):
    def isUgly(self, n):
        if n==0:
            return False
        divi=[2,3,5]
        for i in divi:
            while n%i==0:
                n/=i

        return n==1
        print()