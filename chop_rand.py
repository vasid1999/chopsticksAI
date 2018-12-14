import choplib

print("Welcome to Chopsticks!")

x1=1
x2=1
y1=1
y2=1
ch=0
print("(%d,%d)\t(%d,%d)\tSTART!\n"%(x1,x2,y1,y2))

while True:
	#COMrand MOVE STARTS
	(x1,x2,y1,y2),ch=choplib.randomMove(x1,x2,y1,y2)
	if ch==0:
		print("\n(%d,%d)\t(%d,%d)\tPlayer 1 Self Move\n"%(x1,x2,y1,y2))
	else:
		print("\n(%d,%d)\t(%d,%d)\tPlayer 1 Opponent Move\n"%(x1,x2,y1,y2))
	#COMrand MOVE ENDS
	
	if (y1,y2)==(0,0):
			print("Game over! Player 1 wins!")
			break
	
	#COM-AI MOVE STARTS
	(y1,y2,x1,x2),ch=choplib.bestOutcome(y1,y2,x1,x2)
	if ch==0:
		print("\n(%d,%d)\t(%d,%d)\tPlayer 2 Self Move\n"%(x1,x2,y1,y2))
	else:
		print("\n(%d,%d)\t(%d,%d)\tPlayer 2 Opponent Move\n"%(x1,x2,y1,y2))
	#COM-AI MOVE ENDS
	if (x1,x2)==(0,0):
			print("Game over! Player 2 wins!")
			break
