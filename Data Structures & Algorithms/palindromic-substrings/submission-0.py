class Solution:
    def countSubstrings(self, s: str) -> int:
        array = [[False] * len(s) for _ in range(len(s))]
        count = 0
        for i in range(len(s)): 
            print(i)
            array[i][i] = True

            count += 1
        print(array)
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]: 
                array[i][i+1] = True
                count += 1
        
        for i in range(3, len(s) + 1):  
            for j in range(len(s) - i + 1):  
                k = j + i - 1  

                if array[j + 1][k - 1] and s[j] == s[k]:
                    array[j][k] = True
                    count +=1
        print(array)

        return count

    
