class Solution {
    public void moveZeroes(int[] nums) {
        int pos = 0;
        int n = nums.length;
        
        for (int i = 0; i < n; i++){
            if (nums[i] != 0){
                int temp = nums[pos];
                nums[pos] = nums[i];
                nums[i] = temp;
                pos++;
            }
        }
    }
}