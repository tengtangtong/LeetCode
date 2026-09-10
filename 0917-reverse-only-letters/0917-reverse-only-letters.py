class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        # intiate two pointer and ans array
        ans = list(s)
        left, right = 0, len(s) - 1

        # whlie the right pointer does not go past the left pointer
        while left < right:
            # if both left and right are alpha 
            if s[left].isalpha() and s[right].isalpha():
                ans[left], ans[right] = s[right], s[left] 
                left += 1
                right -= 1
            # if left is not alpha
            elif not s[left].isalpha():
                ans[left] = s[left]
                left += 1
            # if right is not alpha
            elif not s[right].isalpha():
                ans[right] = s[right]
                right -= 1


        return "".join(ans)
