class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        l = []
        def dfs(i,l):
            if i>= len(nums):
                res.append(l.copy())
                return
            
            l.append(nums[i])
            dfs(i+1,l)
            l.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1,l)

        dfs(0,l)
        return res