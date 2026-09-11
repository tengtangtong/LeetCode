class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        word_list = list(word)

        left, right = 0, word_list.index(ch) if ch in word else 0

        # once u hit the right end 
        while left < right:
            word_list[left],word_list[right] = word_list[right], word_list[left]
            left +=1
            right -= 1
        
        return "".join(word_list)