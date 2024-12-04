# %%
from typing import List

# %%
class Solution:
    # soln01
    def reverseString_swap(self, s: List[str]) -> None:
        left, right = 0, len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    # soln02
    def reverseString_pythonic(self, s: List[str]) -> None:
        s.reverse()

    # soln03
    def reverseString_slicing(self, s: List[str]) -> None:
        # s = s[::-1]
        # assignment?
        s[:] = s[::-1]

# %%
if __name__ == "__main__":
    # list_str = ["H", "a", "n", "n", "a", "h"]
    list_str = ["h", "e", "l", "l", "o"]
    src_str = list_str
    print("original")
    print(src_str)

    soln = Solution()
    soln.reverseString_swap(src_str)
    print("reverseString_swap")
    print(src_str)

    print("reverseString_pythonic")
    soln.reverseString_pythonic(src_str)
    print(src_str)
    
    print("reverseString_slicing")
    soln.reverseString_slicing(src_str)
    print(src_str)
    print()

    # TypeError: 'str' object does not support item assignment
    # string -> list -> "".join
    str_example = "A man, a plan, a canal: Panama"
    src_str = list(str_example)
    # print(src_str)

    soln.reverseString_swap(src_str)
    print(str_example)
    print("".join(src_str))


