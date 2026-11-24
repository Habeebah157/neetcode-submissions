class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        numDiff = {}
        for i in range(len(numbers)):
            numDiff[target - numbers[i]] = i
        for i in range(len(numbers)):
            if numbers[i] in numDiff and numDiff[numbers[i]] != i:
                print(i+1)
                return [i+1, numDiff[numbers[i]]+1]