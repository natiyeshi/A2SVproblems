/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    let arr = [];
    for(let i of nums){
        let counter = 0
        for(let j of nums){
            if(j < i){
                counter++;
            }
        }
        arr.push(counter);
    }
    return arr;
};
