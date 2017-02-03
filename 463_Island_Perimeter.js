/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function(grid) {
	var result = 0;
	for (var i in grid) {
		for (var j in grid[i]) {
			if (grid[i][j] === 1) {
				result += 4;
				if (j != 0 && grid[i][j - 1] === 1) {
					result -= 2;
				}
				if (i != 0 && grid[i - 1][j] === 1) {
					result -= 2;
				}
			}
		}
	}
	return result;
};
