/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
	if (divisor === 0) return 0;
	let flag = true;
	if((dividend<0&&divisor<0)||(dividend>0&&divisor>0)) flag = true;
	else flag = false;
	dividend = Math.abs(dividend);
	divisor = Math.abs(divisor);
	if(divisor>dividend) return 0;
	let prime = divisor+divisor;
	let result = 1;
	let records = [[divisor,1]];
	while (dividend - prime >= 0) {
		result+=result;
		records.push([prime,result]);
		prime+=prime;
	}
	let remain = dividend - records.pop()[0];
	while(records.length>0){
		let record = records.pop();
		if(remain-record[0]<0) {
			continue;
		}
		result+=record[1];
		remain-=record[0];
	}
	result = flag?result:-result;
	if(result>2147483647) result = 2147483647;
	return result;
};

