/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
	nums1.sort((a,b)=>{
		return a-b;
	});
	nums2.sort((a,b)=>{
		return a-b;
	});
	var result = [];
	var s1, s2;
	if (nums1.length > nums2.length) {
		s1 = nums1;
		s2 = nums2;
	} else {
		s1 = nums2;
		s2 = nums1;
	}

	function bs(arr, start, end, n) {
		var mid = Math.floor((start + end) / 2);
		if (start <= end) {
			if (arr[mid] < n) {
				return bs(arr, mid + 1, end, n);
			} else if (arr[mid] > n) {
				return bs(arr, start, mid - 1, n);
			} else {
				return mid;
			}
		}
		return -1;
	}

	s2.forEach((v) => {
		var i = bs(s1, 0, s1.length-1, v);
		if (i !== -1) {
			result.push(v);
			s1.splice(i,1);
		}
	})
	return result;
};
