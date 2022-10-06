/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(arr, target) {
    let numbers = []
    let bool = true
     while(bool){
        bool = false
        for(let itr = 0;itr <arr.length; itr++){
            if(arr[itr] > arr[itr + 1]){
                var temp = arr[itr]
                arr[itr]  = arr[itr + 1]
                arr[itr + 1] = temp
                bool = true
                
            }
        }
    }
    for(let i in arr){
        if(arr[i] == target){
            numbers.push(i)
        }
    }
    return numbers;
};
