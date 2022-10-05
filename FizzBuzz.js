/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let arr = [];
    for(let k = 0; k < n; k++){
       let i = k + 1;
       if(i % 3 == 0 && i % 5 == 0)
            arr[k] = "FizzBuzz";
       else if(i % 3 == 0)
          arr[k] = "Fizz";
       else if(i % 5 == 0)
           arr[k] = "Buzz";
       else 
           arr[k] = i.toString();
    }
    return arr;
};
