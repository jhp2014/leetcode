class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        result=[]
        last=[]
        for i in range(2, len(nums)):
            if nums[i-2] - nums[i-1] == nums[i-1] - nums[i]:
                for lst in last:
                    lst.append(nums[i])
                    result.append(lst[:])
                result.append(nums[i-2:])
                last.append(nums[i-2:])
            else:
                last.clear()
        
        return len(result)