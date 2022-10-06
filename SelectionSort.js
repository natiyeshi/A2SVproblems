//Function to sort the array using selection sort algorithm.
  selectionSort(arr,n){
   //code here
    for(let i in arr){
        let temp = arr[i]
        let index = i
        for(let j = i; j < arr.length; j++){
            if(arr[j] < temp){
                temp = arr[j]
                index = j
            }
        }
        arr[index] = arr[i]
        arr[i] = temp 
    }
    return arr 
  }
  
