class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        valuesAndFrequency = {}
        output = set()
        for i in nums:
            if i in valuesAndFrequency:
                valuesAndFrequency[i] +=1
            else:
                valuesAndFrequency[i] = 1
        biggestNums = set()
        biggestNum = float('-inf')
        key = 0 
        while (len(biggestNums) != k):
            print("again", valuesAndFrequency)
            for i, j in valuesAndFrequency.items():
                if j>biggestNum:
                    biggestNum = j
                    key = i
            biggestNums.add(key)
            print(biggestNums)
            print(valuesAndFrequency)
            valuesAndFrequency.pop(key)
            key = 0
            biggestNum= float('-inf')
        return list(biggestNums)

        # if len(output) != k:
        #     print("len", len(output))
        #     print("key",key)
        #     print("this",valuesAndFrequency[key])
        #     output.add(valuesAndFrequency[key])
        #     print(output)
        # else:
        #     print("len", len(output))
        #     print(output)
        #     return(output)