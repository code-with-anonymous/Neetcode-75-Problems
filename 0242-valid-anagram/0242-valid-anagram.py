class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True



# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # return sorted(s) == sorted(t)

        # return Counter(s) == Counter(t)      

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