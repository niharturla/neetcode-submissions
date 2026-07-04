class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort() # O(n log n) -> Why is this the case?
        # Runs TimSort algorithm (combo of merge and insertion sort)

        for curr in range(len(nums)-2): # O(n)
            # since arr is sorted if curr element is positive
            # its impossible for sum = 0
            if nums[curr] > 0:
                break
            if curr > 0 and nums[curr] == nums[curr-1]:
                continue

            t = ~nums[curr] + 1
                
            left = curr + 1
            right = len(nums)-1

            while left < right: # total moves is at most n -> O(n)

                pair_sum = nums[left] + nums[right]
                if pair_sum > t:
                    right-=1
                elif pair_sum < t:
                    left+=1
                else:
                    res.append([nums[curr], nums[left], nums[right]])
                    left+=1
                    # move left forward if we have same element
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
                    right -= 1
                    # move right forward if we have same element
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
             
        return res

        # total complexting: O(n * n + n log n) = O(n^2 + n log n) = O(n^2)
        # total auxillary: O(1) without output list
        # total space: O(k) with output, where k is the triplet count


        