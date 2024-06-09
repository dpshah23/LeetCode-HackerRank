class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        currentOccupancy = 0
        maxOccupancy = 0

        for event in s:
            if event == 'E':
                currentOccupancy += 1
            else:
                currentOccupancy -= 1
            if currentOccupancy > maxOccupancy:
                maxOccupancy = currentOccupancy

        return maxOccupancy


        