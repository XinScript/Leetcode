/**
 * @param {number[]} A
 * @return {number}
 */
var numberOfArithmeticSlices = function(A) {
	var result = 0;
	if (A.length < 3) {
		return 0;
	}

	for (var i = 0; i < A.length - 2; i++) {
		if (A[i + 2] - A[i + 1] === A[i + 1] - A[i]) {
			var gap = A[i + 1] - A[i];
			var count = 1;
			var index = i+3;
			while (index < A.length) {
				if (A[index] - A[index-1] === gap){
					count++;
					index++;
				}
				else{
					break;
				}
			}
			result += (count+1)*count/2;
			i = i + count;
		}
	}
	return result;
};

console.log(numberOfArithmeticSlices([1,2,3,7,5,3]));