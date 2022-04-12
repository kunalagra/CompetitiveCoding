import copy
class Solution:
	def gameOfLife(self, board: list[list[int]]) -> None:
		temp=copy.deepcopy(board)
		for x in range(len(temp)):
			for y in range(len(temp[0])):
				sum1=0
				try:
					if x>0:
						sum1+=temp[x-1][y]
						if y<len(temp[0])-1:
							sum1+=temp[x-1][y+1]
						if y>0:
							sum1+=temp[x-1][y-1]
				except:
					pass
				try:
					if y<len(temp[0])-1:
						sum1+=temp[x][y+1]
					if y>0:
						sum1+=temp[x][y-1]
				except:
					pass
				
				try:
					sum1+=temp[x+1][y]
					if y<len(temp[0])-1:
						sum1+=temp[x+1][y+1]
					if y>0:
						sum1+=temp[x+1][y-1]
				except:
					pass
				if sum1<2:
					board[x][y]=0
				elif sum1==3 and temp[x][y]==0:
					board[x][y]=1
				elif sum1>3:
					board[x][y]=0