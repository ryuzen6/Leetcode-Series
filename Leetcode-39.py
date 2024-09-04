class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,l,tot):
            if tot == target:
                res.append(l.copy())
                return
            
            if i>= len(candidates) or tot>target:
                return
            
            l.append(candidates[i])
            dfs(i,l,tot+candidates[i])
            l.pop()
            dfs(i+1,l,tot)
        
        dfs(0,[],0)
        return res  