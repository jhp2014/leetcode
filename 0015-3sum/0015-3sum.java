class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if(nums.length < 3) return result;
        Arrays.sort(nums);
        int i = 0;
        while (i < nums.length - 2) {
            if (nums[i] > 0) break;
            int j = i + 1;
            int k = nums.length - 1;

            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];

                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    while (j < k && nums[j] == nums[j+1]) {
                        j++;
                    }
                    j ++;

                    while (k > j && nums[k] == nums[k-1]) {
                        k--;
                    }
                    k--;
                } else if (sum < 0) {
                    while (j < k && nums[j] == nums[j+1]) {
                        j++;
                    }
                    j ++;
                } else if (sum > 0) {
                    while (k > j && nums[k] == nums[k-1]) {
                        k--;
                    }
                    k--;
                }
            }
            while (i < nums.length - 1 && nums[i] == nums[i+1]) {
                i++;
            }
            i++;
            
        }
        return result;
    }
}
