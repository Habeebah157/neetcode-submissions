class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string = string + str(len(i)) + "$" + i
        return string


    def decode(self, s: str) -> List[str]:
        newArray = []
        i=0
        while i < len(s):
            keep = i
            while s[keep] != "$":
                keep+=1
            length = int(s[i:keep])
            i=keep+1
            keep = i+length
            newArray.append(s[i:keep])
            i=keep
        return newArray




  
