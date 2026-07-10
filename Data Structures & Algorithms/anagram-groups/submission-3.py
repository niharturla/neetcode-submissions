class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # minimum space will be O(m * n), where m is the average len of inner lists and 
        # n is the len of total

        '''
        -Keep track of seen elements in seen map: which maps sorted key to future index in res
        -If we encounter element we haven't seen, add to seen (sorted, len(seen))
        - key represents the unique sorted string, and the value represents location in res array
        - If we encounter element we have seen, we set res[seen.get(sorted)].extend(curr)

        - Time complexity: Given m input strings, and the average length of string i is n, the
        time complexity is O(m * n log n), where for each string we sort it (n log n)
    
        res = [] # [[act], [pots]] # wil store actual current values not ordered
        seen = dict() # {(act, 0), (opst, 1) }
        for i,curr in enumerate(strs):
            sorted_curr = "".join(sorted(curr)) # opst
            if sorted_curr not in seen:
                seen[sorted_curr] = len(res)
                res.append([curr])
            else:
                index = seen.get(sorted_curr)
                res[index].append(curr)
        
        return res
        '''

        '''
        Optimal solution: Use the charCounts as the key and groups as values
    
        Let m = number of strings, n = max length of a string

        For each input string, we create a count array of alphabets -> O(m)
            -For each character in the string, we calculate ascii value -> O(n)
        Total TC: O(m * n)

        Total Space: O(26 * g), where g = num of groups, since g <= m, we have O(m), 
        because if every element in the list fell into different groups, then we would
        have m groups -> O(26 * m) = O(m)
        '''
        res = defaultdict(list) #  mapping charCount -> anagram list
        base = ord("a")
        for s in strs:
            count=[0] * 26 # [a-z]

            for c in s:
                
                count[ord(c) - base] += 1
            res[tuple(count)].append(s)
        return list(res.values())


                

        
            

        
