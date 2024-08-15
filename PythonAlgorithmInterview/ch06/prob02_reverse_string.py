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
    src_str = list_str

    soln = Solution()
    soln.reverseString(src_str)
    print(src_str)

    str_example = "A man, a plan, a canal: Panama"
    src_str = list(str_example)
    print(src_str)

    soln.reverseString(src_str)
    print(str_example)
    print("".join(src_str))
