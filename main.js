//counting sort
function countingSort(arr, min, max)
{
    var i;
    var z = 0; 
    var count = [];

    for(i = min; i <= max ; i++)
    {
        count[i] = 0;
    }

    for(i = min; i < arr.length; i++)
    {
        count[arr[i]]++;
    }

    for(i = min; i <= max; i++)
    {
        while(count[i]-- > 0)
        {
            arr[z++] = i;
        }
    }
    return arr;
}


var arr1 = [ 3, 0, 2, 5, 4, 1];
console.log(arr1.length);
console.log("Original array elements:")
console.log(arr1)
console.log("sorted array elements")
console.log(countingSort(arr1, 0, 5))
