class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        # vowels
        vowels = 'AaEeIiOoUu'

        # start left pointer and right pointer alrady in position k-1
        left = 0 
        vowel_counts = sum( 1 for l in s[:k] if l in vowels)
        max_vowel_counts = vowel_counts

        # loop and add
        for right in range(k, len(s)):

            if s[right] in vowels:
                vowel_counts += 1
            if s[left] in vowels:
                vowel_counts -=1 

            max_vowel_counts = max(max_vowel_counts, vowel_counts)

            left += 1

        return max_vowel_counts

        
        







        