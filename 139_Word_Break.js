/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) { 
	dp = [true];
	for(let i = 1;i<=s.length;i++)
		for(let j =0;j<i;j++){
			if(dp[j]&&wordDict.indexOf(s.substring(j, i))!=-1){
				dp[i] = true;
				break;
			}
			dp[i] = false;
		}
	return dp[s.length];
};
