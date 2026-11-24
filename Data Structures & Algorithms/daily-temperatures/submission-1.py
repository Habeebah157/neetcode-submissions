class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res = []
        # for i in range(len(temperatures)-1):
        #     print("i",i)
        #     count = 0
        #     for j in range(i+1, len(temperatures)):
        #         print(j)
        #         currentTemp = temperatures[i]
        #         if temperatures[j] < currentTemp:
        #             print("inner", temperatures[j], "curr", currentTemp)
        #             count+=1
        #     res.append(count)
        # print(res)
        # res.append(0)
        # return res
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res