function maxSumSubArray(arr, k) {
    if (arr.length < k) return null;
    let maxSum = 0;
    let windowSum = 0;
    for(let i =0; i<k; i++){
        windowSum += arr[i]
        console.log(windowSum)
    }
    maxSum = windowSum;
    for (let i = k; i<arr.length;i++){
        windowSum = windowSum-arr[i-k]+arr[i]
        console.log(windowSum)
        maxSum = Math.max(maxSum, windowSum)
    }
    return maxSum;
}

// console.log(maxSumSubArray([2, 1, 5, 1, 3, 2], 3)) // 9
// console.log(maxSumSubArray([2, 3, 4, 1, 5], 2)) // 7
console.log(maxSumSubArray([1,12,-5,-6,50,3], 4)) // 49