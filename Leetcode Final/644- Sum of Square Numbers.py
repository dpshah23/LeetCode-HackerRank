class Solution(object):
    def judgeSquareSum(self, c):
        a, b = 0, int(c**0.5)
        while a <= b:
            sum = a * a + b * b
            if sum < c:
                a += 1
            elif sum > c:
                b -= 1
            else:
                return True
        return c == 1