class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def fun(i,l,tot):
            if tot==target and l.copy() not in res:
                res.append(l.copy())
                return
            if tot> target or i>= len(candidates):  
                return
            l.append(candidates[i])
            tot += candidates[i]
            fun(i+1,l,tot)
            l.pop()
            tot -= candidates[i]
            fun(i+1,l,tot)
    
        fun(0,[],0)
        return res