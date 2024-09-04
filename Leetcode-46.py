class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def fun(temp = [],dmap = dict()):
            if len(temp) == len(nums):
                res.append(temp.copy())
                return
            
            for i in range(len(nums)):
                if not dmap[i]:
                    temp.append(nums[i])
                    dmap[i] = 1
                    fun(temp,dmap)
                    dmap[i] = 0
                    temp.pop()

        dmap = [0]*(len(nums))
        fun([],dmap)
        return res