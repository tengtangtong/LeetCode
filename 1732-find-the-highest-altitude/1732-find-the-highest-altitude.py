class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        highest = 0 
        prefix_sum = [0]

        for i in gain:
            prefix_sum.append(prefix_sum[-1] + i)
            highest = max(prefix_sum[-1] , highest)

        return highest
        
        