
/*
 * Complete the 'countSwaps' function below.
 *
 * The function accepts INTEGER_ARRAY a as parameter.
 */

function countSwaps(arr) {
    // Write your code here
    let counter = 0;
    let bool = true;
    while(bool){
        bool = false
        for(let itr = 0;itr <arr.length; itr++){
            if(arr[itr] > arr[itr + 1]){
                var temp = arr[itr]
                arr[itr]  = arr[itr + 1]
                arr[itr + 1] = temp
                bool = true
                counter++
            }
        }
    }
    console.log("Array is sorted in "+counter+" swaps.");
    console.log("First Element: "+arr[0]);
    console.log("Last Element: "+arr[arr.length - 1]);
}
