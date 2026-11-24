class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        testé={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in testé.keys():
                return [testé[diff], i]
            else:
                testé[nums[i]]=i
        return [0,0]
