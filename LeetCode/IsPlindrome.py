class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        tempnum=x
        print(tempnum)
        reversed_num=0
        if(x<0):
            tempnum=x-x+x

        while(tempnum!=0):
            n1=tempnum%10
            reversed_num=reversed_num*10+n1
            tempnum//=10
        
        if reversed_num==x and x<0:
            return True
        elif reversed_num==x:
            return True
        else:
            return False
        
obe=Solution()
print(obe.isPalindrome(-121))