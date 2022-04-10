class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(0,len(nums),1):
            for b in range(0,len(nums),1):
                if a == b:
                    continue
                if nums[a] + nums[b] == target:
                    c = [a,b]
                    return c