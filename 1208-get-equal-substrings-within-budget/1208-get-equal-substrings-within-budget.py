class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        # build the cost array cus apparently two pointer dont work on s and t
        cost_array = []

        for i in range(len(t)):

            cost = abs(ord(s[i]) - ord(t[i]))
            cost_array.append(cost)

        # use sliding window on the array 
        left , curr_cost = 0,0
        maximum_length = 0

        for right in range(len(s)):

            curr_cost += cost_array[right]

            while curr_cost > maxCost:

                curr_cost -= cost_array[left]
                left += 1

            maximum_length = max(maximum_length, right - left + 1)

        return maximum_length