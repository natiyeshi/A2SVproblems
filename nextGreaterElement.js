/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(num1, num2) {
    let returns = []
    for(let itr in num1){
        for(let j in num2){
            if(num1[itr] == num2[j]){
                let inter = -1
                for(let k = j; k < num2.length; k++){
                    if(num2[k] > num2[j]){
                        inter = num2[k]
                        break;
                    }
                }
                returns.push(inter)
                break;
            }
        }
    }
    return returns
};
