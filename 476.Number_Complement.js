/**
 * @param {number} num
 * @return {number}
 */
var findComplement = function(num) {
	if (num === 1) return 0;
	var init = 1;
	while(init<num){
		init = (init << 1 )+1;
	}
	return num ^ init;
};
