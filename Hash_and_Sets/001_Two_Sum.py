class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetdict = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in targetdict:
                return [targetdict[temp],i]
            targetdict[nums[i]] = i
        
