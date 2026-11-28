class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # UMPIRE METHOD
        # racecar, carrace
        # If they are not the same length they cannot be anagrams of each other
        # what comes to my mind is maybe a dictionary. 
        # There would always be two strings being compared to each other correct? 

        # dictionary. time (0(1)? )
        # sort (o(n)? )
        # r  a   c 1   e   c  a   r
        # r- 2,2  a- 2,2  c- 2,2  e- 1,1


        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t




         