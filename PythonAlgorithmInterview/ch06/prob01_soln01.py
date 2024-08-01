class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True


if __name__ == "__main__":
    str_example = "A man, a plan, a canal: Panama"

    soln = Solution()
    print(soln.isPalindrome(str_example))
    print()
    
    # TEST
    print("FUNCTION TEST")
    print("a".isalnum())
    print("1".isalnum())
    print("?".isalnum())
