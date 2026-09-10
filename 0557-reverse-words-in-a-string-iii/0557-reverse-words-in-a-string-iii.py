class Solution:
    def reverseWords(self, s: str) -> str:

        # split the string into words
        s = s.split(' ')
        ans = []
        count = 0

        for word in s: 

            count += 1

            left, right = 0, len(word) - 1

            while left < right: 
                ans.append(word[right])
                right -= 1
            ans.append(word[left])

            if count < len(s):
                ans.append(' ')
                
        return "".join(ans)
        