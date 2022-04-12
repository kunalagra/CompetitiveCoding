import copy
class Solution:
	def gameOfLife(self, board: list[list[int]]) -> None:
		temp=copy.deepcopy(board)
		l0=len(temp[0])

		for x in range(len(temp)):
			for y in range(l0):
				sum1=0
			
				if x>0:
					sum1+=temp[x-1][y]
					if y<l0-1:
						sum1+=temp[x-1][y+1]
					if y>0:
						sum1+=temp[x-1][y-1]
			
				if y<l0-1:
					sum1+=temp[x][y+1]
				if y>0:
					sum1+=temp[x][y-1]
			
				if x<len(temp)-1:
					sum1+=temp[x+1][y]
					if y<l0-1:
						sum1+=temp[x+1][y+1]
					if y>0:
						sum1+=temp[x+1][y-1]
			
				if sum1<2:
					board[x][y]=0
				elif sum1==3 and temp[x][y]==0:
					board[x][y]=1
				elif sum1>3:
					board[x][y]=0	