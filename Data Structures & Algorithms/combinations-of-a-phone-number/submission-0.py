class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        word_num_map =letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res, ele = [],[]

        DIGITS = len(digits)

        def backtrack(i=0):
            if i == DIGITS:
                res.append("".join(ele))
                return
            for letter in word_num_map[digits[i]]:
                ele.append(letter)
                backtrack(i + 1)
                ele.pop()
        backtrack(0)
        return res
        



      

        