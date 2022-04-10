class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target>nums[-1]:
            for x in range(len(nums)):
                if target==nums[x]:
                    return True
        else:
            for x in range(len(nums)-1,-1,-1):
                if target==nums[x]:
                    return True
        return False