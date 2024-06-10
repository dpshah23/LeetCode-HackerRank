class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        print(expected)
        print(heights)
        counter=0
        for i in range(len(heights)):
            if heights[i]!=expected[i]:
                counter+=1

        return counter
