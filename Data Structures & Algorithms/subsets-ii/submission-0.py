class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        temp=[]
        res=[]
        def backtrack(i):
            if i>=len(nums):
                print(temp)
                if sorted(temp) not in res:
                    res.append(sorted(temp[:]))
                return 
            temp.append(nums[i])
            backtrack(i+1)
            temp.pop()
            backtrack(i+1)
        backtrack(0)
        print(temp)
        print(res)
        return res


        