from util import timefn


# %%
class Solution:
    @timefn
    def zero_sum_triplets_01(self, nums: list[int]) -> list[int]:
        # brute force
        print("zero_sum_triplets - brute force")
        nums.sort()

        zero_list: list[int] = []
        soln_list: list[int] = []

        cnt = 0

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    cnt += 1
                    sum: int = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        zero_list = [nums[i], nums[j], nums[k]]
                        if zero_list not in soln_list:
                            soln_list.append(zero_list)

        print(f"cnt: {cnt}")
        return soln_list

    @timefn
    def zero_sum_triplets_02(self, nums: list[int]):
        # three points
        print("zero_sum_triplets - three points")
        nums.sort()

        zero_list: list[int] = []
        soln_list: list[int] = []

        cnt = 0

        for i in range(0, len(nums)):
            left = i + 1
            right = len(nums) - 1
            for _ in range(i + 1, len(nums)):
                cnt += 1
                sum: int = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    zero_list = [nums[i], nums[left], nums[right]]
                    if zero_list not in soln_list:
                        soln_list.append(zero_list)

        print(f"cnt: {cnt}")
        return soln_list


# %%
if __name__ == "__main__":
    nums: list[int] = [-1, 0, 1, 2, -1, 4]

    soln = Solution()
    print(soln.zero_sum_triplets_01(nums))
    print()
    print(soln.zero_sum_triplets_02(nums))

# %%
# zero_sum_triplets - brute force
# cnt: 20
# @timefn: zero_sum_triplets_01 took 0.0002810955047607422 seconds
# [[-1, -1, 2], [-1, 0, 1]]

# zero_sum_triplets - three points
# cnt: 15
# @timefn: zero_sum_triplets_02 took 0.0001506805419921875 seconds
# [[-1, -1, 2], [-1, 0, 1]]
