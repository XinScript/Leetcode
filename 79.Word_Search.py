class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def search(i,j,k):
        	if k == len(word):
        		return True
        	if 0 <= i <= len(board) - 1 and 0<= j <= len(board[0]) - 1:
	        	if board[i][j] == word[k]:
	        		board[i][j] = ord(board[i][j])
	        		# mask!
		        	rs = search(i-1,j,k+1) or search(i+1,j,k+1) or search(i,j-1,k+1) or search(i,j+1,k+1)
		        	board[i][j] = chr(board[i][j])
		        	return rs
	        return False

       	for i,row in enumerate(board):
       		for j,ele in enumerate(row):
       				if search(i,j,0):
       					return True
       	return False

