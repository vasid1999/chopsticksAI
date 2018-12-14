from random import randint
sni=(0,0,0,0,1,2,3,4)
snf=(1,2,3,4,4,4,4,4)

def playerMove(x1,x2,y1,y2):
	while True:
		ch=int(input("Enter (0) for self-move and (1) for opponent move: "))
		if ch==0:
			if x1+x2==1:
				print("Self-move not possible\n")
			else:
				while True:
					ch=int(input("\nEnter new left value: "))
					if ch<0 or ch>4 or ch>x1+x2 or ch==x1 or ch==x2:
						print("Please enter a valid value")
					else:
						x2=(x1+x2-ch)%5
						x1=ch%5
						return (x1,x2,y1,y2),0
		
		elif ch==1:
			while True:
				ch=int(input("\nEnter (1) for left-handed attack and (3) for right-handed attack: "))
				if x1>0 and ch==1:
					ch2=int(input("Enter (7) for attack on left hand and (9) for attack on right hand: "))
					if ch2==7:
						y1=(y1+x1)%5
						return (x1,x2,y1,y2),1
					elif ch2==9:
						y2=(y2+x1)%5
						return (x1,x2,y1,y2),1
					else:
						print("Please enter a valid value")
				elif x2>0 and ch==3:
					ch2=int(input("Enter (7) for attack on left hand and (9) for attack on right hand: "))
					if ch2==7:
						y1=(y1+x2)%5
						return (x1,x2,y1,y2),1
					elif ch2==9:
						y2=(y2+x2)%5
						return (x1,x2,y1,y2),1
					else:
						print("Please enter a valid value")
				else:
					print("Please enter a valid value")
		else:
			print("Please enter a valid value\n")

def payoffCalc(moveTuple):
	x1=moveTuple[0]
	x2=moveTuple[1]
	y1=moveTuple[2]
	y2=moveTuple[3]
	payoff=0
	
	if (y1+x1)%5==0:
		payoff-=1
	if (y1+x2)%5==0:
		payoff-=1
	if (y2+x1)%5==0:
		payoff-=1
	if (y2+x2)%5==0:
		payoff-=1
	if x1==0:
		payoff-=1
	if x2==0:
		payoff-=1
	
	if y1==0:
		payoff+=1
	if y2==0:
		payoff+=1
	return payoff

def bestOutcome(X1,X2,Y1,Y2):
	s=X1+X2
	moveList=[]
	payoff=payoffmax=i=imax=0
	if X1*X2==0:
		moveList=[(X1,X2,(Y1+s)%5,Y2),(X1,X2,Y1,(Y2+s)%5)]
		for x in range(sni[s-1],snf[s-1]):
			if x==X1 or x==X2:
				continue
			moveList.append((x,s-x,Y1,Y2))
		while i<len(moveList):
			payoff=payoffCalc(moveList[i])
			if i>0:
				if payoff>payoffmax:
					imax=i
					payoffmax=payoff
			else:
				payoffmax=payoff=payoffCalc(moveList[i])
			i+=1
		if imax>1:
			return moveList[imax],0
		else:
			return moveList[imax],1
	else:
		moveList=[(X1,X2,(Y1+X1)%5,Y2),(X1,X2,(Y1+X2)%5,Y2),(X1,X2,Y1,(Y2+X1)%5),(X1,X2,Y1,(Y2+X2)%5)]
		for x in range(sni[s-1],snf[s-1]):
			if x==X1 or x==X2:
				continue
			moveList.append((x,s-x,Y1,Y2))
		while i<len(moveList):
			payoff=payoffCalc(moveList[i])
			if i>0:
				if payoff>payoffmax:
					imax=i
					payoffmax=payoff
			else:
				payoffmax=payoff=payoffCalc(moveList[i])
			i+=1
		if imax>3:
			return moveList[imax],0
		else:
			return moveList[imax],1

def randomMove(X1,X2,Y1,Y2):
	s=X1+X2
	moveList=[]
	payoff=payoffmax=i=imax=0
	if X1*X2==0:
		moveList=[(X1,X2,(Y1+s)%5,Y2),(X1,X2,Y1,(Y2+s)%5)]
		for x in range(sni[s-1],snf[s-1]):
			if x==X1 or x==X2:
				continue
			moveList.append((x,s-x,Y1,Y2))
		i=randint(0,len(moveList)-1)
		if i>1:
			return moveList[i],0
		else:
			return moveList[i],1
	else:
		moveList=[(X1,X2,(Y1+X1)%5,Y2),(X1,X2,(Y1+X2)%5,Y2),(X1,X2,Y1,(Y2+X1)%5),(X1,X2,Y1,(Y2+X2)%5)]
		for x in range(sni[s-1],snf[s-1]):
			if x==X1 or x==X2:
				continue
			moveList.append((x,s-x,Y1,Y2))
		i=randint(0,len(moveList)-1)
		if i>3:
			return moveList[i],0
		else:
			return moveList[i],1
