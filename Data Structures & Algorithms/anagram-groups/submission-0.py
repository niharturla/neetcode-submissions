class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # minimum space will be O(m * n), where m is the average len of inner lists and 
        # n is the len of total

        '''
        -Keep track of seen elements in seen map: which maps sorted key to future index in res
        -If we encounter element we haven't seen, add to seen (sorted, len(seen))
        - key represents the unique sorted string, and the value represents location in res array
        - If we encounter element we have seen, we set res[seen.get(sorted)].extend(curr)

        '''
        
        res = [] # [[act], [pots]] # wil store actual current values not ordered
        seen = dict() # {(act, 0), (opst, 1) }
        unique_count = 0
        for i,curr in enumerate(strs):
            sorted_curr = "".join(sorted(curr)) # opst
            if sorted_curr not in seen:
                seen[sorted_curr] = unique_count
                res.append([curr])
                unique_count += 1
            else:
                index = seen.get(sorted_curr)
                res[index].append(curr)
        
        return res
            

                

        
            

        
