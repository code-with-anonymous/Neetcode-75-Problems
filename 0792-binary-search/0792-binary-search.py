# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         start =0
#         end =len(nums)-1
#         if len(nums) == 1 and nums[start] != target:
#                 return -1 
#         elif len(nums) == 1 and nums[start] == target:
#             return 0        
#         while start <= end:
#             if nums [start] == target:
#                 return start
#             if nums [end] == target:
#                 return end

#             if nums[start] < target :
#                 start+=1
#             if nums[end] > target :

#                 end-=1
#         return -1 


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2  # Calculate middle element
            
            if nums[mid] == target:
                return mid  # Target found at mid
            elif nums[mid] < target:
                start = mid + 1  # Search in the right half
            else:
                end = mid - 1  # Search in the left half
                
        return -1  # Target not found
