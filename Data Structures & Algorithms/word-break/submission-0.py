class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # so for this I want to start by taking each letter by the number and until
        #it gets to the point where the word is in the wordDict
        #After that I return true??? I 
        # I am not sure exactly, I forgot how to solve it. 
        # Then check for the next ones and then see if they are in, if they are not in keey going
        # create a dp with the length of the word + 1
        # After that, go through each of the previous range to check 
        # if it is true and then check if the array is true. 
        # and then at then end if it is true. 
        
        
        #now the numbering is confusing me. 
        #first make the dp array. 
        # then loop through to each section to see if it woks 
        n = len(s) + 1
        dp = [False]*n
        dp[0] = True

        for i in range(n): 
            for j in range(i): 
                if dp[j] and s[j:i] in wordDict: 
                    dp[i] = True
        return dp[-1]