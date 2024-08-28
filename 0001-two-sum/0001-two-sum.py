from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize pointers and index list
        index = []
        left = 0
        right = len(nums) - 1
        
        # Sort the list to use two-pointer approach
        nums_with_index = sorted((num, i) for i, num in enumerate(nums))
        
        # Reinitialize pointers based on sorted list
        left = 0
        right = len(nums_with_index) - 1

        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            
            if current_sum == target:
                index.append(nums_with_index[left][1])
                index.append(nums_with_index[right][1])
                return index  # Return as soon as we find the solution
            
            elif current_sum < target:
                left += 1  # Increase sum by moving left pointer right
            else:
                right -= 1  # Decrease sum by moving right pointer left

        return index  # Return empty list if no pair found (though usually a solution exists)
