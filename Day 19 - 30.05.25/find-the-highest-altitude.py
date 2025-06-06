# ARRAYS - Easy

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. 
# The biker starts his trip on point 0 with altitude equal 0.
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). 
# Return the highest altitude of a point.

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        altitude = [0] * (n+1)
        for i in range(1,n+1):
            altitude[i] = altitude[i-1] + gain[i-1]
        return max(altitude)
      
