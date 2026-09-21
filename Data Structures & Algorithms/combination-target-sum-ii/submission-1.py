class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def gs(i,curr,total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i == len(candidates):
                return
            # we either include current num or skip it
            curr.append(candidates[i])
            gs(i+1, curr, total + candidates[i])
            curr.pop()

            # not to explore, we don't want to explore the same element
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            gs(i+1, curr, total)
        gs(0,[],0)
        return [list(combo) for combo in res]