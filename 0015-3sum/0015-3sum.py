class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left, mid, right = 0, len(nums) - 2, len(nums) - 1
        result = []
        
        while right > 1:

            while left < mid:
                total = nums[left] + nums[mid] + nums[right]

                if total == 0:
                    result.append([nums[left], nums[mid], nums[right]])

                    left += 1
                    while left < mid and nums[left] == nums[left-1]:
                        left += 1
                    
                    mid -= 1
                    while mid > left and nums[mid] == nums[mid+1]:
                        mid -= 1


                elif total > 0:
                    mid -= 1

                elif total < 0:
                    left += 1

            right -= 1
            while right > 0 and nums[right] == nums[right + 1]:
                right -= 1
            
            mid = right - 1
            left = 0

        return result