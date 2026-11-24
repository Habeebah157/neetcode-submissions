class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # So maybe first sort the array. 
        # And then subtract the previous from the next one and see. 
        #If it is greater than one, then do not add. 
        # counter = 0
        # finalCounter = 0
        # checker= 0 
        # print (nums)
        # nums.sort()
        # print(nums)
        # for i in range(len(nums)-2):
        #     checker = nums[i] - nums[i+1]
        #     if (checker == -1):
        #         counter+=1
        #     elif(checker != -1):
        #         if finalCounter < counter:
        #             finalCounter = counter
        #         if(checker != 0):
        #             counter = 0
        #     else:
        #         checker = 0
        #     checker = 0
        #     print(i)
        # print("counter",finalCounter)

        #so bvasically going through the array and putting it in a set, 
        #After puttinjg it in a set, for each value, check if it has a previous 
        #value or an after value, if it has a previous value, Then 
        #add it to a counter or something
        #If it has an after value, then add one to the temporary counter unitil the n
        # one is not in the set
        largest = 0
        numSet = set()
        for i in nums:
            numSet.add(i)

        for i in numSet:
            if i-1 not in numSet:
                length = 1
                while i + length in numSet:
                    length+=1
                largest = max(largest, length)


        print(numSet)
        return largest

        