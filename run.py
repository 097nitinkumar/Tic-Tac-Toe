import os

game=[[-1,-1,-1],
      [-1,-1,-1],
      [-1,-1,-1]]
n=0
player=0
curr_player=0

def initialise():
	global game,n
	n=int(input("input grid size "))
	game = [[-1 for j in range(n)] for i in range(n)]
	
	
def board_game(data=-1,row=-1,column=-1,move=False):
	global game
	try:
		os.system('cls||clear')
		if move!=False:
			game[row][column]=data
		for i in range(0,n):
			print(" ",i,end=" ")
		print("")
		for count,row in enumerate(game):
			print(count,row)
		winner()
	except Exception as e:
		print("Something went wrong",e)
		
def winner():
	flag=-1
	global winner_found
	a=diagonally(n)
	if (a  in range(0,n)):
		print("Winner cis ",a)
		winner_found=True
	else:
		a=horizontally(n)
		if a in range(0,n):
			print("Winner bis ",a)
			winner_found=True
		else:
			a=vertically(n)
			if a in range(0,n):
				print("Winner ais ",a)
				winner_found=True
		

def diagonally(n):
	if(game[0][n-1]>=0):
		a=game[0][0]
		if(all(list(game[i][i]==a for i in range(0,n)))):
			return a

	if(game[0][n-1]>=0):
		b=game[0][n-1]
		if(all(list(game[j][n-j-1]==b for j in range(0,n)))):
			return b

def horizontally(n):
	for row in game:
		if ((row.count(row[0]) == len(row)) and row[0]>=0):
			return row[0]

def vertically(n):
	a=game
	a=list(map(list, zip(*a)))
	for row in a:
		if ((row.count(row[0]) == len(row)) and row[0]>=0):
			return row[0]
def no_player():
	global player
	player=int(input("Enter No of players "))



Keep_playing=True
while Keep_playing:
	
	winner_found=False
	initialise()
	board_game()
	no_player()
	p=n*n
	while (not (winner_found) and (p>0)):
		board_game()
		print("player ",curr_player)
		rows_choice=int(input("Enter Row Number "))
		cols_choice=int(input("Enter Col Number "))
		if (   0 <= rows_choice  and  rows_choice < n  and  0 <= cols_choice  and  cols_choice < n  ):
			if(game[rows_choice][cols_choice] == -1  ):
				board_game(curr_player,rows_choice,cols_choice,True)
				curr_player=(curr_player+1)%player
				p-=1
			else:
				print("Location Occupied ,reattempt")
		else:
			print("Invalid location,reattempt")
	board_game()
	Keep_playing=bool(int(input("Want To Continue Playing? '0':No '1':Yes ")))

	

	
	

