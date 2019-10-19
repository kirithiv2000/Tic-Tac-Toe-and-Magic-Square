# A=[["x","o","x"],
#    ["x","o","x"],
#    ["o","x","o"]]
# horizondal=[]
# vertical=[]
# diagonal=[]
# antidiagonal=[]
# for i in A:
# 	h=""
# 	for j in i:
# 		h+=j
# 	horizondal.append(h)

# print(horizondal)
# for i in range(3):
# 	v=""
# 	for j in A:
# 		v+=j[i]
# 	vertical.append(v)
# print(vertical)
# for i in range(len(A)):
# 	diagonal.append(A[i][i])
# print(diagonal)
# l=2
# for i in range(len(A)):
# 	antidiagonal.append(A[i][l])
# 	l-=1
# print(antidiagonal)

############################################################################################3
# A=[["x","o","x"],
#    ["x","o","x"],
#    ["o","x","x"]]
# horizondal=[0,0,0]
# vertical=[0,0,0]
# diagonal=[]
# antidiagonal=[]
# for i in range(len(A)):
# 	h=""
# 	for j in range(i):
# 		h+=A[i][j]
# 	horizondal[i]=h


# for i in range(3):
# 	v=""
# 	for j in A:
# 		v+=j[i]
# 	vertical[i]=v

# for i in range(len(A)):
# 	diagonal.append(A[i][i])


# l=2
# for i in range(len(A)):
# 	antidiagonal.append(A[i][l])
# 	l-=1

# for i in horizondal:
# 	if i=="xxx":
# 		print("player X is the winner")
# 	elif i=="ooo":
# 		print("player O is the winner")

# for i in vertical:
# 	if i=="xxx":
# 		print("player X is the winner")
# 	elif i=="ooo":
# 		print("player O is the winner")		
# a=""
# for i in diagonal:
# 	a+=i

# if a=="xxx":
# 	print("player X is the winner")
# elif a=="ooo":
# 	print("player O is the winner")	


# a=""
# for i in antidiagonal:
# 	a+=i

# if a=="xxx":
# 	print("player X is the winner")
# elif a=="ooo":
# 	print("player O is the winner")	
#####################################################################################################3
# A=[["x","o","x"],
#    ["x","o","x"],
#    ["x","x","o"]]


# A=[	['_', '_', '_'],
# 	['_', '_', '_'],
# 	['_', '_', '_']]



# horizondal=[0,0,0]
# vertical=[0,0,0]
# diagonal=[0,0,0]
# antidiagonal=[0,0,0]
# for i in A:
# 	print(i)
# for x in range(9):
# 	if x%2==0:
# 		playerx=input("1st or 2nd or 3rd line 1st or 2nd or 3rd POSITION    playerx :").split(" ")
# 		A[int(playerx[0])-1][int(playerx[1])-1]="x"
# 	else:
# 		playero=input("1st or 2nd or 3rd line 1st or 2nd or 3rd POSITION    playero :").split(" ")
# 		A[int(playero[0])-1][int(playero[1])-1]="o"
# 	for i in A:
# 		print(i)
# 	for i in range(len(A)):
# 		h=""
# 		for j in range(3):
# 			h+=A[i][j]
# 		horizondal[i]=h


# 	for i in range(3):
# 		v=""
# 		for j in A:
# 			v+=j[i]
# 		vertical[i]=v


# 	for i in range(len(A)):
# 		diagonal[i]=A[i][i]
	
# 	l=2
# 	for i in range(len(A)):
# 		antidiagonal[i]=A[i][l]
# 		l-=1
	
# 	for i in horizondal:
# 		if i=="xxx":
# 			print("player X is the winner horizondal")
# 			break
# 			break
# 		elif i=="ooo":
# 			print("player O is the winner horizondal")
# 			break
# 			break

# 	for i in vertical:
# 		if i=="xxx":
# 			print("player X is the winner vertical")
# 			break
# 			break
# 		elif i=="ooo":
# 			print("player O is the winner vertical")
# 			break
# 			break		
# 	a=""
# 	for i in diagonal:
# 		a+=i


# 	if a=="xxx":
# 		print("player X is the winner diagonal")
# 		break
# 	elif a=="ooo":
# 		print("player O is the winner diagonal")
# 		break	


# 	a=""
# 	for i in antidiagonal:
# 		a+=i

# 	if a=="xxx":
# 		print("player X is the winner antidiagonal")
# 		break
# 	elif a=="ooo":
# 		print("player O is the winner antidiagonal")
# 		break	

# else:
# 	print("MATCH TIE")


























# #board
# board=["_","_","_",
# 	   "_","_","_",
# 	   "_","_","_"]


# a=("~~~~~~~")
# b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
# c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
# d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"


# board1=[a,b,c,d,a]
# for i in board1:
# 	print(i)


# #gameisgoing
# gameisgoing=True
# import random
# while gameisgoing:
# 	player1=int(input(" CHOOSE THE POSITION 1-9  playerx:"))
# 	board[player1-1]="x"
# 	a=("~~~~~~~")
# 	b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
# 	c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
# 	d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"
# 	board1=[a,b,c,d,a]
# 	for i in board1:
# 		print(i)
# 	if "_" in board:
# 		pass
# 	else:
# 		print("MATCH TIE")
# 		gameisgoing=False
		
# 	horizondal=[]
# 	h=""
# 	for i in range(len(board)):
# 		h+=board[i]
# 		if len(h)==3:
# 			horizondal.append(h)
# 			h=""
# 	print(horizondal)
# 	for i in horizondal:
# 		if i=="xxx":
# 			print("playerx is the winner")
# 		if i=="ooo":
# 			print("playero is the winner")
# 	vertical=[]
# 	for i in range(3):
# 		v=""
# 		v+=board[i]+board[i+3]+board[i+6]
# 		vertical.append(v)	

# 	print(vertical)
# 	for i in vertical:
# 		if i=="xxx":
# 			print("playerx is the winner")
# 		if i=="ooo":
# 			print("playero is the winner")

# 	diagonal=[]
# 	diagonal.append(board[0]+board[4]+board[8])
# 	print(diagonal)
# 	if diagonal[0]=="xxx":
# 		print("playerx is the winner")
# 	if diagonal[0]=="ooo":
# 		print("playero is the winner")

		
# 	andiagonal=[]
# 	andiagonal.append(board[6]+board[4]+board[2])
# 	print(andiagonal)
# 	if andiagonal[0]=="xxx":
# 		print("playerx is the winner")
# 	if andiagonal[0]=="ooo":
# 		print("playero is the winner")




# 	player2=int(input(" CHOOSE THE POSITION 1-9  playero:"))
# 	board[player2-1]="o"
# 	a=("~~~~~~~")
# 	b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
# 	c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
# 	d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"


# 	board1=[a,b,c,d,a]
# 	for i in board1:
# 		print(i)

# 	if "_" in board:
# 		pass
# 	else:
# 		print("MATCH TIE")
# 		gameisgoing=False

# 	horizondal=[]
# 	h=""
# 	for i in range(len(board)):
# 		h+=board[i]
# 		if len(h)==3:
# 			horizondal.append(h)
# 			h=""
# 	print(horizondal)
# 	for i in horizondal:
# 		if i=="xxx":
# 			print("playerx is the winner")
# 		if i=="ooo":
# 			print("playero is the winner")
# 	vertical=[]
# 	for i in range(3):
# 		v=""
# 		v+=board[i]+board[i+3]+board[i+6]
# 		vertical.append(v)	

# 	print(vertical)
# 	for i in vertical:
# 		if i=="xxx":
# 			print("playerx is the winner")
# 		if i=="ooo":
# 			print("playero is the winner")

# 	diagonal=[]
# 	diagonal.append(board[0]+board[4]+board[8])
# 	print(diagonal)
# 	if diagonal[0]=="xxx":
# 		print("playerx is the winner")
# 	if diagonal[0]=="ooo":
# 		print("playero is the winner")

		
# 	andiagonal=[]
# 	andiagonal.append(board[6]+board[4]+board[2])
# 	print(andiagonal)
# 	if andiagonal[0]=="xxx":
# 		print("playerx is the winner")
# 	if andiagonal[0]=="ooo":
# 		print("playero is the winner")


########################################################################################################################3


# board
# board=["_","_","_",
# 	   "_","_","_",
# 	   "_","_","_"]


# a=("~~~~~~~")
# b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
# c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
# d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"


# board1=[a,b,c,d,a]
# for i in board1:
# 	print(i)


# #gameisgoing
# gameisgoing=True
# import random
# while gameisgoing:
# 	player1=int(input(" CHOOSE THE POSITION 1-9  playerx:"))
# 	board[player1-1]="x"
# 	a=("~~~~~~~")
# 	b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
# 	c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
# 	d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"
# 	board1=[a,b,c,d,a]
# 	for i in board1:
# 		print(i)
		
# 	horizondal=[]
# 	h=""
# 	for i in range(len(board)):
# 		h+=board[i]
# 		if len(h)==3:
# 			horizondal.append(h)
# 			h=""
# 	for i in horizondal:
# 		if i=="xxx":
# 			print("playerx is the winner")
# 			break
# 	if i=="xxx":
# 		break
# 	vertical=[]
# 	for i in range(3):
# 		v=""
# 		v+=board[i]+board[i+3]+board[i+6]
# 		vertical.append(v)	


# 	for i in vertical:
# 		if i=="xxx":
# 			print("playerx is the winner")
# 			break
# 	if i=="xxx":
# 		break
# 	diagonal=[]
# 	diagonal.append(board[0]+board[4]+board[8])
# 	if diagonal[0]=="xxx":
# 		print("playerx is the winner")
# 		break

		
# 	andiagonal=[]
# 	andiagonal.append(board[6]+board[4]+board[2])
# 	if andiagonal[0]=="xxx":
# 		print("playerx is the winner")
# 		break

# 	if "_" in board:
# 		pass
# 	else:
# 		print("MATCH TIE")
# 		gameisgoing=False
# 		break


# 	player2=int(input(" CHOOSE THE POSITION 1-9  playero:"))
# 	board[player2-1]="o"
# 	a=("~~~~~~~")
# 	b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
# 	c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
# 	d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"


# 	board1=[a,b,c,d,a]
# 	for i in board1:
# 		print(i)

# 	horizondal=[]
# 	h=""
# 	for i in range(len(board)):
# 		h+=board[i]
# 		if len(h)==3:
# 			horizondal.append(h)
# 			h=""
# 	for i in horizondal:
# 		if i=="ooo":
# 			print("playero is the winner")
# 			break
# 	if i=="ooo":
# 		break
# 	vertical=[]
# 	for i in range(3):
# 		v=""
# 		v+=board[i]+board[i+3]+board[i+6]
# 		vertical.append(v)	

# 	for i in vertical:
# 		if i=="ooo":
# 			print("playero is the winner")
# 			break
# 	if i=="ooo":
# 		break

# 	diagonal=[]
# 	diagonal.append(board[0]+board[4]+board[8])
# 	if diagonal[0]=="ooo":
# 		print("playero is the winner")
# 		break

		
# 	andiagonal=[]
# 	andiagonal.append(board[6]+board[4]+board[2])
# 	if andiagonal[0]=="ooo":
# 		print("playero is the winner")
# 		break

# 	if "_" in board:
# 		pass
# 	else:
# 		print("MATCH TIE")
# 		gameisgoing=False
# 		break

######################################################################################################################################################

# board=["_","_","_",
# 	   "_","_","_",
# 	   "_","_","_"]


# a=("~~~~~~~")
# b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
# c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
# d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"


# board1=[a,b,c,d,a]
# for i in board1:
# 	print(i)


# #gameisgoing
# gameisgoing=True
# import random
# while gameisgoing:
# 	player1=int(input(" \t\tCHOOSE THE POSITION 1-9  playerx:"))
# 	board[player1-1]="x"
# 	a=("~~~~~~~")
# 	b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
# 	c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
# 	d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"
# 	board1=[a,b,c,d,a]
# 	g=""
# 	for i in board1:
# 		g+=i+"\n"
# 	print(g,end="\r")
		
# 	horizondal=[]
# 	h=""
# 	for i in range(len(board)):
# 		h+=board[i]
# 		if len(h)==3:
# 			horizondal.append(h)
# 			h=""
# 	for i in horizondal:
# 		if i=="xxx":
# 			print("playerx is the winner")
# 			break
# 	if i=="xxx":
# 		break
# 	vertical=[]
# 	for i in range(3):
# 		v=""
# 		v+=board[i]+board[i+3]+board[i+6]
# 		vertical.append(v)	


# 	for i in vertical:
# 		if i=="xxx":
# 			print("playerx is the winner")
# 			break
# 	if i=="xxx":
# 		break
# 	diagonal=[]
# 	diagonal.append(board[0]+board[4]+board[8])
# 	if diagonal[0]=="xxx":
# 		print("playerx is the winner")
# 		break

		
# 	andiagonal=[]
# 	andiagonal.append(board[6]+board[4]+board[2])
# 	if andiagonal[0]=="xxx":
# 		print("playerx is the winner")
# 		break

# 	if "_" in board:
# 		pass
# 	else:
# 		print("MATCH TIE")
# 		gameisgoing=False
# 		break


# 	player2=int(input(" \t\tCHOOSE THE POSITION 1-9  playero:"))
# 	board[player2-1]="o"
# 	a=("~~~~~~~")
# 	b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
# 	c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
# 	d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"


# 	board1=[a,b,c,d,a]
# 	g=""
# 	for i in board1:
# 		g+=i+"\n"
# 	print(g,end="\r")
# 	horizondal=[]
# 	h=""
# 	for i in range(len(board)):
# 		h+=board[i]
# 		if len(h)==3:
# 			horizondal.append(h)
# 			h=""
# 	for i in horizondal:
# 		if i=="ooo":
# 			print("playero is the winner")
# 			break
# 	if i=="ooo":
# 		break
# 	vertical=[]
# 	for i in range(3):
# 		v=""
# 		v+=board[i]+board[i+3]+board[i+6]
# 		vertical.append(v)	

# 	for i in vertical:
# 		if i=="ooo":
# 			print("playero is the winner")
# 			break
# 	if i=="ooo":
# 		break

# 	diagonal=[]
	# diagonal.append(board[0]+board[4]+board[8])
	# if diagonal[0]=="ooo":
	# 	print("playero is the winner")
	# 	break

	
	# andiagonal=[]
	# andiagonal.append(board[6]+board[4]+board[2])
	# if andiagonal[0]=="ooo":
	# 	print("playero is the winner")
	# 	break

	# if "_" in board:
	# 	pass
	# else:
	# 	print("MATCH TIE")
	# 	gameisgoing=False
	# 	break

####################################################################################################################################


# board=["_","_","_",
# 	   "_","_","_",
# 	   "_","_","_"]


# a=("~~~~~~~")
# b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
# c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
# d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"


# board1=[a,b,c,d,a]
# for i in board1:
# 	print(i)																											#important this is the final code
# player1choice=[]
# player2choice=[]


# #gameisgoing
# gameisgoing=True
# import random
# while gameisgoing:
# 	player1=int(input(" CHOOSE THE POSITION 1-9  playerx:"))
# 	if player1 not in player1choice and player1 not in player2choice:
# 		board[player1-1]="x"
# 		player1choice.append(player1)
# 		a=("~~~~~~~")
# 		b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
# 		c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
# 		d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"
# 		board1=[a,b,c,d,a]
# 		for i in board1:
# 			print(i)
			
# 		horizondal=[]
# 		h=""
# 		for i in range(len(board)):
# 			h+=board[i]
# 			if len(h)==3:
# 				horizondal.append(h)
# 				h=""
# 		for i in horizondal:
# 			if i=="xxx":
# 				print("playerx is the winner")
# 				break
# 		if i=="xxx":
# 			break
# 		vertical=[]
# 		for i in range(3):
# 			v=""
# 			v+=board[i]+board[i+3]+board[i+6]
# 			vertical.append(v)	


# 		for i in vertical:
# 			if i=="xxx":
# 				print("playerx is the winner")
# 				break
# 		if i=="xxx":
# 			break
# 		diagonal=[]
# 		diagonal.append(board[0]+board[4]+board[8])
# 		if diagonal[0]=="xxx":
# 			print("playerx is the winner")
# 			break

			
# 		andiagonal=[]
# 		andiagonal.append(board[6]+board[4]+board[2])
# 		if andiagonal[0]=="xxx":
# 			print("playerx is the winner")
# 			break

# 		if "_" in board:
# 			pass
# 		else:
# 			print("MATCH TIE")
# 			gameisgoing=False
# 			break
# 	else:
# 		print("\v\vThat place is already CHOOSEen")

# 	player2=int(input(" CHOOSE THE POSITION 1-9  playero:"))
# 	if player2 not in player2choice and player2 not in player1choice:
# 		board[player2-1]="o"
# 		player2choice.append(player2)
# 		a=("~~~~~~~")
# 		b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
# 		c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
# 		d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"


# 		board1=[a,b,c,d,a]
# 		for i in board1:
# 			print(i)

# 		horizondal=[]
# 		h=""
# 		for i in range(len(board)):
# 			h+=board[i]
# 			if len(h)==3:
# 				horizondal.append(h)
# 				h=""
# 		for i in horizondal:
# 			if i=="ooo":
# 				print("playero is the winner")
# 				break
# 		if i=="ooo":
# 			break
# 		vertical=[]
# 		for i in range(3):
# 			v=""
# 			v+=board[i]+board[i+3]+board[i+6]
# 			vertical.append(v)	

# 		for i in vertical:
# 			if i=="ooo":
# 				print("playero is the winner")
# 				break
# 		if i=="ooo":
# 			break

# 		diagonal=[]
# 		diagonal.append(board[0]+board[4]+board[8])
# 		if diagonal[0]=="ooo":
# 			print("playero is the winner")
# 			break

			
# 		andiagonal=[]
# 		andiagonal.append(board[6]+board[4]+board[2])
# 		if andiagonal[0]=="ooo":
# 			print("playero is the winner")
# 			break

# 		if "_" in board:
# 			pass
# 		else:
# 			print("MATCH TIE")
# 			gameisgoing=False
# 			break
# 	else:
# 		print("\v\vThat place is already CHOOSEen")


############################################################################################################################
# import time

# board=["_","_","_",
# 	   "_","_","_",
# 	   "_","_","_"]

# def display():
# 	a=("~~~~~~~")
# 	b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
# 	c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
# 	d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"


# 	board1=[a,b,c,d,a]
# 	for i in board1:
# 		print(i)

# display()
# player1choice=[]
# player2choice=[]
# time.sleep(0.5)

# #gameisgoing
# gameisgoing=True
# import random
# while gameisgoing:
# 	player1=int(input("\t\t\t CHOOSE THE POSITION 1-9  playerx:"))
# 	if player1 not in player1choice and player1 not in player2choice:
# 		board[player1-1]="x"
# 		player1choice.append(player1)
# 		display()
# 		time.sleep(1)
			
# 		horizondal=[]
# 		h=""
# 		for i in range(len(board)):
# 			h+=board[i]
# 			if len(h)==3:
# 				horizondal.append(h)
# 				h=""
# 		for i in horizondal:
# 			if i=="xxx":
# 				print("playerx is the winner")
# 				break
# 		if i=="xxx":
# 			break
# 		vertical=[]
# 		for i in range(3):
# 			v=""
# 			v+=board[i]+board[i+3]+board[i+6]
# 			vertical.append(v)	


# 		for i in vertical:
# 			if i=="xxx":
# 				print("playerx is the winner")
# 				break
# 		if i=="xxx":
# 			break
# 		diagonal=[]
# 		diagonal.append(board[0]+board[4]+board[8])
# 		if diagonal[0]=="xxx":
# 			print("playerx is the winner")
# 			break

			
# 		andiagonal=[]
# 		andiagonal.append(board[6]+board[4]+board[2])
# 		if andiagonal[0]=="xxx":
# 			print("playerx is the winner")
# 			break

# 		if "_" in board:
# 			pass
# 		else:
# 			print("MATCH TIE")
# 			gameisgoing=False
# 			break
# 	else:
# 		print("\v\vThat place is already CHOOSEen")

# 	player2=int(input(" CHOOSE THE POSITION 1-9  playero:"))
# 	if player2 not in player2choice and player2 not in player1choice:
# 		board[player2-1]="o"
# 		player2choice.append(player2)
# 		display()
# 		time.sleep(1)
# 		horizondal=[]
# 		h=""
# 		for i in range(len(board)):
# 			h+=board[i]
# 			if len(h)==3:
# 				horizondal.append(h)
# 				h=""
# 		for i in horizondal:
# 			if i=="ooo":
# 				print("playero is the winner")
# 				break
# 		if i=="ooo":
# 			break
# 		vertical=[]
# 		for i in range(3):
# 			v=""
# 			v+=board[i]+board[i+3]+board[i+6]
# 			vertical.append(v)	

# 		for i in vertical:
# 			if i=="ooo":
# 				print("playero is the winner")
# 				break
# 		if i=="ooo":
# 			break

# 		diagonal=[]
# 		diagonal.append(board[0]+board[4]+board[8])
# 		if diagonal[0]=="ooo":
# 			print("playero is the winner")
# 			break

			
# 		andiagonal=[]
# 		andiagonal.append(board[6]+board[4]+board[2])
# 		if andiagonal[0]=="ooo":
# 			print("playero is the winner")
# 			break

# 		if "_" in board:
# 			pass
# 		else:
# 			print("MATCH TIE")
# 			gameisgoing=False
# 			break
# 	else:
# 		print("\v\vThat place is already CHOOSEen")

#########################################################################################################33
# import time
# board=["_","_","_",
# 	   "_","_","_",
# 	   "_","_","_"]


# a=("~~~~~~~")
# b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
# c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
# d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"


# e=a+"\n"+b+"\n"+c+"\n"+d+"\n"+a
# print(e,end="\r")
# print("kirithiv")


#############################################################################
from connected_to_web_page import ti as t
board=["_","_","_",
	   "_","_","_",
	   "_","_","_"]

a=("~~~~~~~")
b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"


board1=[a,b,c,d,a]
for i in board1:
	print(i)
player1choice=[]
player2choice=[]
win=" "
t(board,win)

#gameisgoing
gameisgoing=True
import random
while gameisgoing:
	player1=int(input(" CHOOSE THE POSITION 1-9  playerx:"))
	if player1 not in player1choice and player1 not in player2choice:
		board[player1-1]="x"
		player1choice.append(player1)
		a=("~~~~~~~")
		b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
		c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
		d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"
		t(board,win)

		board1=[a,b,c,d,a]
		for i in board1:
			print(i)
			
		horizondal=[]
		h=""
		for i in range(len(board)):
			h+=board[i]
			if len(h)==3:
				horizondal.append(h)
				h=""
		for i in horizondal:
			if i=="xxx":
				print("playerx is the winner")
				win="playerx is the winner"
				break
		if i=="xxx":
			t(board,win)
			
			break
		vertical=[]
		for i in range(3):
			v=""
			v+=board[i]+board[i+3]+board[i+6]
			vertical.append(v)	


		for i in vertical:
			if i=="xxx":
				print("playerx is the winner")
				win="playerx is the winner"
				break
		if i=="xxx":
			t(board,win)

			break
		diagonal=[]
		diagonal.append(board[0]+board[4]+board[8])
		if diagonal[0]=="xxx":
			print("playerx is the winner")
			win="playerx is the winner"
			t(board,win)
			break

			
		andiagonal=[]
		andiagonal.append(board[6]+board[4]+board[2])
		if andiagonal[0]=="xxx":
			print("playerx is the winner")
			win="playerx is the winner"
			t(board,win)

			break

		if "_" in board:
			pass
		else:
			win="MATCH TIE"
			print("MATCH TIE")
			gameisgoing=False
			t(board,win)

			break
	else:
		print("\v\vThat place is already CHOOSEen")

	player2=int(input(" CHOOSE THE POSITION 1-9  playero:"))
	if player2 not in player2choice and player2 not in player1choice:
		board[player2-1]="o"
		player2choice.append(player2)
		a=("~~~~~~~")
		b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
		c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
		d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"
		t(board,win)

		board1=[a,b,c,d,a]
		for i in board1:
			print(i)

		horizondal=[]
		h=""
		for i in range(len(board)):
			h+=board[i]
			if len(h)==3:
				horizondal.append(h)
				h=""
		for i in horizondal:
			if i=="ooo":
				print("playero is the winner")
				break
		if i=="ooo":
			win="playero is the winner"
			t(board,win)
			
			break
		vertical=[]
		for i in range(3):
			v=""
			v+=board[i]+board[i+3]+board[i+6]
			vertical.append(v)	

		for i in vertical:
			if i=="ooo":
				print("playero is the winner")
				break
		if i=="ooo":
			win="playero is the winner"
			t(board,win)

			break

		diagonal=[]
		diagonal.append(board[0]+board[4]+board[8])
		if diagonal[0]=="ooo":
			win="playero is the winner"
			print(win)
			t(board,win)

			break

			
		andiagonal=[]
		andiagonal.append(board[6]+board[4]+board[2])
		if andiagonal[0]=="ooo":
			win="playero is the winner"
			print(win)
			t(board,win)

			break

		if "_" in board:
			pass
		else:
			win="MATCH TIE"
			print("MATCH TIE")
			gameisgoing=False
			t(board,win)
			break

	else:
		print("\v\vThat place is already CHOOSEen")










