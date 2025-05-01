from util import timefn


# %%
class Solution:
    @timefn
    def zero_sum_triplets_01(self, nums: list[int]) -> list[int]:
        # brute force
        print("zero_sum_triplets - brute force")
        nums.sort()

        soln_list: list[int] = []

        cnt = 0

        # TODO 1. 종료 시점 확인 len(nums) - 2
        # TODO 2. 중복된 값을 처리하는 방법
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    cnt += 1
                    if nums[i] + nums[j] + nums[k] == 0:
                        if [nums[i], nums[j], nums[k]] not in soln_list:
                            soln_list.append([nums[i], nums[j], nums[k]])

        print(f"cnt: {cnt}")
        return soln_list

    @timefn
    def zero_sum_triplets_02(self, nums: list[int]) -> list[int]:
        # three points
        print("zero_sum_triplets - three points")
        nums.sort()

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
                    if [nums[i], nums[left], nums[right]] not in soln_list:
                        soln_list.append([nums[i], nums[left], nums[right]])

        print(f"cnt: {cnt}")
        return soln_list

    @timefn
    def zero_sum_triplets_03(self, nums: list[int]) -> list[int]:
        print("zero_sum_triplets - (soln) brute force")
        results = []
        nums.sort()

        cnt = 0

        # brute force n^3
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    cnt += 1

                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])

        print(f"cnt: {cnt}")
        return results

    @timefn
    def zero_sum_triplets_04(self, nums: list[int]) -> list[list[int]]:
        print("zero_sum_triplets - (soln) three points")
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 `sum` 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # `sum = 0`인 경우이므로 정답 및 스킵 처리
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results


# %%
if __name__ == "__main__":
    nums: list[int] = [-1, 0, 1, 2, -1, 4]

    soln = Solution()
    print(soln.zero_sum_triplets_01(nums))
    print()
    print(soln.zero_sum_triplets_02(nums))
    print()
    print(soln.zero_sum_triplets_03(nums))

# %%
# zero_sum_triplets - brute force
# cnt: 20
# @timefn: zero_sum_triplets_01 took 0.0002357959747314453 seconds
# [[-1, -1, 2], [-1, 0, 1]]

# zero_sum_triplets - three points
# cnt: 15
# @timefn: zero_sum_triplets_02 took 6.651878356933594e-05 seconds
# [[-1, -1, 2], [-1, 0, 1]]

# zero_sum_triplets - (soln) brute force
# cnt: 14
# @timefn: zero_sum_triplets_03 took 3.504753112792969e-05 seconds
# [[-1, -1, 2], [-1, 0, 1]]
