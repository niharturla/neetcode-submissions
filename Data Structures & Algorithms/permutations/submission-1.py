class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def gen(curr, remaining):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for num in remaining:
                curr.append(num)

                new_rem = [x for x in remaining if x != num]
                gen(curr, new_rem)
                curr.pop()
            return res
        return gen([],nums)


        

            