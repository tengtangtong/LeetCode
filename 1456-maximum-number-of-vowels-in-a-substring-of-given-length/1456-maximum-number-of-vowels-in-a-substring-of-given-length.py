class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        # change to list
        s = list(s)
        vowels = 'AaEeIiOoUu'

        # left and right pointer 
        left, right = 0, 0
        vowel_counts = 0
        max_vowel_counts = 0

        # right pointer moves first 
        for right in range(len(s)):
            
            # counts vowels as it goes
            if s[right] in vowels:
                vowel_counts += 1
            
            # when it builds the first substring
            if right - left + 1 == k:
                max_vowel_counts = max(max_vowel_counts, vowel_counts)

            # if it hits more than the window 
            while right - left + 1 > k:
                if s[left] in vowels:
                    vowel_counts -= 1
                left += 1
                max_vowel_counts = max(max_vowel_counts, vowel_counts)
        
        return max_vowel_counts







        