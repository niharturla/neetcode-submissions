class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force: 
        # Time complexity: O(n^2) because it uses n iterations for outer loop and n-1 iterations for inner
            # O(n*(n-1))
        # Space complexity: O(1) because we create two variables to iterate through array
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

        # optimized solution 1: O(n * log(n))
            # 1. Sort array in non-decreasing order
            # 2. for each nums[i], find complement t-nums[i] with binary search
            # 3. If complement exists return it
        '''
        pairs={}
        j=0
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in pairs:
                return [pairs[complement], i]
            
            pairs[nums[i]] = i
                
        

