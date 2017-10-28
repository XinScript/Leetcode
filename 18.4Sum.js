/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums,target) {
	nums.sort((a,b)=>a-b);
	var result = [];
    for (var j = 0; j <nums.length-3;j++){
        if (j === 0 || (j > 0 && nums[j] != nums[j - 1])) {
            for (var i = j+1; i < nums.length - 2; i++) {
                if (i === j+1 || nums[i] != nums[i - 1]) {
                    var low = i + 1;
                    var high = nums.length - 1;
                    var sum = target - nums[i] - nums[j];
                    while (low < high) {
                        if (nums[low] + nums[high] < sum) low++
                        else if (nums[low] + nums[high] > sum) high--;
                        else  {
                            result.push([nums[j],nums[i], nums[low], nums[high]]);
                            while (low < high && nums[low] == nums[low + 1]) low++;
                            while (low < high && nums[high] == nums[high - 1]) high--;
                            low++;
                            high--;
                        } 
                    }
                }
            }        
        }
    }
	return result;
};