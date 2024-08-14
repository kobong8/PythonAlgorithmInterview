from typing import List


class Solution:
    # soln01
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    # list_str = ["H", "a", "n", "n", "a", "h"]
    list_str = ["h", "e", "l", "l", "o"]
    print(list_str)

    soln = Solution()
    soln.reverseString(list_str)
    print(list_str)
