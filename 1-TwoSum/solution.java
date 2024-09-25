class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i =0; i< nums.length - 1; i++){
            int check = target - nums[i];
            if (nums.contains(check) = true){
                return (nums[i] + nums.indexOf[check]);
            }
        } 
    }
}