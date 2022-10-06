/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    let bool = true
    while(bool){
        bool = false
        for(let i = 0;i < nums.length - 1;i++){
            if((nums[i - 1] + nums[i+1])/2 == nums[i]){
                let temp = nums[i - 1];
                nums[i - 1] = nums[i]
                nums[i] = temp;
                bool = true;
            }
        }
    }
    return nums;
};
