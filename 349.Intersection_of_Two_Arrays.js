/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
	var result = [];
  var s1 = new Set(nums1);
  var s2 = new Set(nums2);
  s1.forEach((v)=>{
  	if(s2.has(v)){
  		result.push(v);
  	}
  });
  return result;
};
