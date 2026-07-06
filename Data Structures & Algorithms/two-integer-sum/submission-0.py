class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        temp=target-nums[0]
        d={temp:0}
        for i in range(1,len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                temp=target-nums[i]
                d[temp] = i
            
