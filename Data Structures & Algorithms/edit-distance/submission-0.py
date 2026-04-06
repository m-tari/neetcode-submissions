class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        i = 0
        j = 0
        op = 0
        while i < len(word1):
            while j <len(word2):
                if word1[i] == word2[j]:
                    i += 1
                    j += 1
                #  Delete
                elif word1[i + 1] == word2[j]:  
                    i += 1
                    op += 1
                # Replace
                elif word1[i + 1] == word2[j + 1]:
                    i += 1
                    j += 1
                    op += 1
                # Insert
                elif word1[i] == word2[j + 1]:
                    j += 1
                    op += 1
                break
            if j == len(word2):
                i += 1
                op += 1

        return op
