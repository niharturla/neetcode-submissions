class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tab = set()
        for i in range(len(nums)):
            if nums[i] not in tab:
                tab.add(nums[i])
            else:
                return True
        return False