/*
 * Complete the 'countingSort' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function countingSort(arr) {
    // Write your code here
    let index = [];
    for(let i = 0;i < 100;i++)
        index.push(0);
    let couter = 0;
    for(let itr of arr){
        index[itr] += 1;
    }
    return index;
}
