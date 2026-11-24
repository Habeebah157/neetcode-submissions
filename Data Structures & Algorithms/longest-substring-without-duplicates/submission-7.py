class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        seen = set()
        start = 0 
        end = 0
        seen.add(s[start])
        max_len = 1  # Start with 1 since we have at least one character
        
        while end < len(s) - 1:  # Changed condition to process all characters
            end += 1
            if s[end] in seen: 
                # Move start forward until the duplicate is removed
                while s[start] != s[end]:
                    seen.remove(s[start])
                    start += 1
                start += 1  # Move past the duplicate character
            else: 
                seen.add(s[end])
            
            max_len = max(end - start + 1, max_len)  # Update max_len every iteration
        
        return max_len