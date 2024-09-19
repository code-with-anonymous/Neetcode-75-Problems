class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        longest = 0

        for n in num_set:  # Loop through num_set instead of nums
            if (n - 1) not in num_set:  # Check if n is the start of a sequence
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)
                
        return longest
