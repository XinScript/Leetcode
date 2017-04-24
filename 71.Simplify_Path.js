/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
  paths = path.split('/');
  const arr = [];
  for(let i in paths){
  	switch (paths[i]){
  		case '':break;
  		case '/':break;
  		case '.':break;
  		case '..':
  			if(arr.length)arr.pop();
  			break;
  		default:
  			arr.push(paths[i]);
  			break;
  	}
  }
  return '/'+arr.join('/');
};

console.log(simplifyPath('/../////'))