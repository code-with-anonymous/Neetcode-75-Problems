class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        return Counter(s) == Counter(t)
# point to ponder that sort and and sorted are diffrent fuction        
#                 Key Differences:
#  Modification of Original Data:

# sort(): Modifies the list in place.
# sorted(): Does not modify the original iterable; returns a new sorted list.
# Return Value:

# sort(): Returns None.
# sorted(): Returns a new sorted list.
# Applicability:

# sort(): Only works on lists.
# sorted(): Can work on any iterable (e.g., lists, tuples, strings).