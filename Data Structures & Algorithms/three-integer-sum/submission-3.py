class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol_set = set()

        nums.sort()

        for curr in range(len(nums)-2):
            if curr > 0 and nums[curr] == nums[curr-1]:
                continue

            t = nums[curr] * -1
                
            left = curr + 1
            right = len(nums)-1

            while left < right:

                sum = nums[left] + nums[right]
                if sum > t:
                    right-=1
                elif sum < t:
                    left+=1
                else:
                    sol_set.add((nums[curr],nums[left], nums[right]))
                    left+=1
                    right-=1
        return [list(triplet) for triplet in sol_set]


        