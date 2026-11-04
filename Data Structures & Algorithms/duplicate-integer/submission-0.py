class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        L=[]
        for i in nums:
            if i not in L:
                L.append(i)
            else:
                return True
        return False