class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        students.sort()
        seats.sort()
        ans=0
        for i in range(len(seats)):
            ans+=abs(seats[i]-students[i])

        return ans        