'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'insertionSort1' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY arr
 */

function insertionSort1(n, arr) {
    // Write your code here
    let file = arr[arr.length - 1];
    for(let i = arr.length - 1; i > -1; i--){
        if(arr[i - 1] > file){
            arr[i] = arr[i - 1]
            console.log(arr.join(" "))
        } else{
            arr[i] = file
            break
        }
    }
        console.log(arr.join(" "))
    
}

function main() {
    const n = parseInt(readLine().trim(), 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    insertionSort1(n, arr);
}
