class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # count=0
        # for i in nums:
        #     if i in nums:
        #         count+=1
        #         if count >=2:
        #             return True
        #     else:
        #         return False    

        s = set(nums)
        if len(nums) == len(s):
            return False
        else:
            return True    

        # start=0
        # end=len(nums)-1
        # for start in  range(len(nums)):
        #     if nums[start] == nums[end]:
        #         return True
        #         break
        #     else:
        #         start+=1
        #         end-=1
        # return False

    #     class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     seen = set()  # Initialize an empty set to track seen elements
    #     for num in nums:  # Iterate over each element in the list
    #         if num in seen:  # If the element is already in the set, we have a duplicate
    #             return True
    #         seen.add(num)  # Otherwise, add the element to the set
    #     return False  # If no duplicates are found, return False
        


        