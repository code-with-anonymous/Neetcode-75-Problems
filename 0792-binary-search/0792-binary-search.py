class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start =0
        end =len(nums)-1
        if len(nums) == 1 and nums[start] != target:
                return -1 
        elif len(nums) == 1 and nums[start] == target:
            return 0        
        while start <= end:
            if nums [start] == target:
                return start
            if nums [end] == target:
                return end

            if nums[start] < target :
                start+=1
            if nums[end] > target :

                end-=1
        return -1 






            # if len(nums) == 1 and nums[start] != target:
            #     return -1