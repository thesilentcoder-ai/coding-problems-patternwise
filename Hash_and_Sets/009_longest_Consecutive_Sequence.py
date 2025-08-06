class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in numset:
                next_num = num +1 
                templen = 1
                while next_num in numset:
                    templen += 1
                    next_num += 1
                longest = max(longest,templen)
        
        return longest
