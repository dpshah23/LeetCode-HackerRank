class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        decimal_num = int(s, 2)
        steps=0
        while decimal_num!=1:
            if decimal_num%2==0:
                decimal_num/=2
                
            else:
                decimal_num+=1
                steps+=1
                decimal_num/=2
                

            steps+=1

        return steps