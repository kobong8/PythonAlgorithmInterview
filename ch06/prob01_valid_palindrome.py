# %%
import collections
from typing import Deque
import re

# %%
class Solution:
    # soln01
    def isPalindrome_list(self, s: str) -> bool:
        strs: list = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True
    
    # soln02
    def isPalindrome_deque(self, s: str) -> bool:
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True
    
    # soln03
    def isPalindrome_slicing(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]  # 슬라이싱

# %%
if __name__ == "__main__":
    str_example = "A man, a plan, a canal: Panama"

    soln = Solution()
    print(soln.isPalindrome_list(str_example))
    print()
    print(soln.isPalindrome_deque(str_example))
    print()
    print(soln.isPalindrome_slicing(str_example))
    print()
    
    # TEST
    print("FUNCTION TEST")
    print("a".isalnum())
    print("1".isalnum())
    print("?".isalnum())


