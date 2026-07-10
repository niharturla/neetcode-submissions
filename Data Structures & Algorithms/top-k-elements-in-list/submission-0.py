class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        1,
        1,2,2,3,3,3
        
        # first idea approach:
        '''
        Allocate memory for hashmap(element, freq)

        1. Run through n elements and store the counts
        2. sort values by descending order
        3. return first k keys
        '''

        res={}
        for num in nums:
            res[num] = res.get(num, 0) + 1
        sorted_data = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_data.keys())[:k]
        

        
       




        





            