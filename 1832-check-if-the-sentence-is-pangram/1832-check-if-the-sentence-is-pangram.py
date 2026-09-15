class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        # check if sentence contains every alphabet at least once
        
        # there are 26 alphabets so if the len of set should be 26 else 
        
        return len(set(sentence)) == 26
        
        
        