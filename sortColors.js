/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(arr) {
    
    let bool = true;
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
    for(let i of arr)
        console.log(i)
};
