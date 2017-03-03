/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    var compare = function(a,b){
        A = String(a)
        B = String(b)
        return A+B>B+A?false:true;
    }
    arr = [nums[0]]
    for (i = 1;i<nums.length;i++){
        for(j = 0;j<arr.length;j++){
            if (compare(arr[j],nums[i])){
                arr.splice(j,0,nums[i]);
                break;
            }
        }
        if (j ==arr.length){
            arr.push(nums[i])
        }
    }
    return arr[0] == '0' ?'0':arr.join("");
};
