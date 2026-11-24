class Solution:
    def isPalindrome(self, s: str) -> bool:
        #First I am thinking of filter out removing the space and jsut
        # leaving out the alphanumeric. How do I do that? 
        # I also have to change everything to lower case. 
        #Maybe two pointers, one from the left and one from the right
        #And when they are not the same, just return false. 
        #empty list, true or false. 
        newString = s.replace(" ", "")
        newString = newString.strip()
        newString = re.sub(r'\W+', '', newString)
        newString = newString.lower()
        first = 0
        last = len(newString)-1
        while(first < last):
            if newString[first] != newString[last]:
                return False
            first+=1
            last-=1
        return True
        print(newString)
        # Plust time complexity
        