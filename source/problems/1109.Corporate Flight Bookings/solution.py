from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        count = [0] * (n + 1)
        for start, end, seats in bookings:
            count[start - 1] += seats
            count[end] -= seats
        for i in range(1, n):
            count[i] += count[i - 1]
        return count[:-1]
