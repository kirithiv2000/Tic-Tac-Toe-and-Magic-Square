# a=[[8,1,6],[3,5,7],[4,9,2]]
# horizondal=[]
# vertical=[]
# diagonal=[]
# andiagonal=[]

# for i in a:
# 	# print(i)
# 	horizondal.append(sum(i))
# print(horizondal)
# for i in range(len(a)):
# 	diagonal.append(a[i][i])
# print(diagonal)
# l=2
# for i in range(len(a)):
# 	andiagonal.append(a[i][l])
# 	l-=1
# print(andiagonal)
# for i in range(len(a)):
# 	b=[]
# 	for j in a:
# 		b.append(j[i])
# 	vertical.append(sum(b))
# print(vertical)

# if horizondal[0]==horizondal[1]==horizondal[2]==sum(diagonal)==sum(andiagonal)==vertical[0]==vertical[1]==vertical[2] :
# 	print("Magic square")

# a=[[0,0,0],[0,1,0],[0,0,0]]

# while True:
# 	horizondal=[]
# 	vertical=[]
# 	diagonal=[]
# 	andiagonal=[]
# 	for i in a:
# 		horizondal.append(sum(i))
# 	for i in range(len(a)):
# 		diagonal.append(a[i][i])
# 	l=2
# 	for i in range(len(a)):
# 		andiagonal.append(a[i][l])
# 		l-=1
# 	for i in range(len(a)):
# 		b=[]
# 		for j in a:
# 			b.append(j[i])
# 		vertical.append(sum(b))

# 	if horizondal[0]==horizondal[1]==horizondal[2]==sum(diagonal)==sum(andiagonal)==vertical[0]==vertical[1]==vertical[2] :
# 		print("Magic square")
# 	d=[]
# 	for i in a:
# 		b=[]
# 		for i in range(len(a)):
# 			c=input("\t"*i)
# 			b.append(int(c))
# 		d.append(b)
# 	a=d
# 	for i in a:
# 		print(i)




###########################################
# import random
# a=[[0,0,0],[0,1,0],[0,0,0]]
# dd={}
# while True:
# 	horizondal=[]
# 	vertical=[]
# 	diagonal=[]
# 	andiagonal=[]

# 	for i in a:
# 		horizondal.append(sum(i))
# 	for i in range(len(a)):
# 		diagonal.append(a[i][i])
# 	l=2
# 	for i in range(len(a)):
# 		andiagonal.append(a[i][l])
# 		l-=1
# 	for i in range(len(a)):
# 		b=[]
# 		for j in a:
# 			b.append(j[i])
# 		vertical.append(sum(b))

# 	if horizondal[0]==horizondal[1]==horizondal[2]==sum(diagonal)==sum(andiagonal)==vertical[0]==vertical[1]==vertical[2] :
# 		print("Magic square")
# 		if len(dd)!=0:
# 			dd["a"*len(dd)]=d
# 			print(dd)
# 		else:
# 			print(dd)

# 			break
# 	ch=[i for i in range(1,10)]
# 	d=[]
# 	for i in a:
# 		b=[]
# 		for i in range(len(a)):
# 			c=random.choice(ch)
# 			ch.remove(c)

# 			print("\t"*i,end="\r")
# 			b.append(int(c))
# 		d.append(b)
# 	a=d

# 	print(d)
# 	for i in a:
# 		print("\t",i)

#########################################################################
########################################
# import random
# a=[[0,0,0],[0,1,0],[0,0,0]]
# dd={}
# while True:
# 	horizondal=[]
# 	vertical=[]
# 	diagonal=[]
# 	andiagonal=[]

# 	for i in a:
# 		horizondal.append(sum(i))
# 	for i in range(len(a)):
# 		diagonal.append(a[i][i])
# 	l=2
# 	for i in range(len(a)):
# 		andiagonal.append(a[i][l])
# 		l-=1
# 	for i in range(len(a)):
# 		b=[]
# 		for j in a:
# 			b.append(j[i])
# 		vertical.append(sum(b))

# 	if horizondal[0]==horizondal[1]==horizondal[2]==sum(diagonal)==sum(andiagonal)==vertical[0]==vertical[1]==vertical[2] :
# 		print("\nMagic square\n")
# 		for i in a:
# 			print("\t",i)
# 		if len(dd)!=9:
# 			dd["magic_square"*(len(dd)+1)]=d
# 			print(dd)
# 		else:
# 			print(dd)

# 			break
# 	ch=[i for i in range(1,10)]
# 	d=[]
# 	for i in a:
# 		b=[]
# 		for i in range(len(a)):
# 			c=random.choice(ch)
# 			ch.remove(c)

# 			print("\t"*i,end="\r")
# 			b.append(int(c))
# 		d.append(b)
# 	a=d

# 	print(d,end="\r")

# jj=[]
# for i in dd.values():
# 	if i not in jj:
# 		jj.append(i)
# print("------------------------------------OUR FINAL RESULT--------------------------------")
# for i in jj:
# 	for a in i:
# 		print("\t"*5,a)
# 	print("Next")



################################################################33


# import random
# a=[[0,0,0],[0,1,0],[0,0,0]]
# dd={}
# while True:
# 	horizondal=[]
# 	vertical=[]
# 	diagonal=[]
# 	andiagonal=[]

# 	for i in a:
# 		horizondal.append(sum(i))
# 	for i in range(len(a)):
# 		diagonal.append(a[i][i])
# 	l=2
# 	for i in range(len(a)):
# 		andiagonal.append(a[i][l])
# 		l-=1
# 	for i in range(len(a)):
# 		b=[]
# 		for j in a:
# 			b.append(j[i])
# 		vertical.append(sum(b))

# 	if horizondal[0]==horizondal[1]==horizondal[2]==sum(diagonal)==sum(andiagonal)==vertical[0]==vertical[1]==vertical[2] :
# 		print("\nMagic square\n")

# 		if len(dd)!=9:
# 			dd["magic_square"*(len(dd)+1)]=d
# 			# print(dd)
# 		else:
# 			print(dd)

# 			break
# 	ch=[i for i in range(1,10)]
# 	d=[]
# 	for i in a:
# 		b=[]
# 		for i in range(len(a)):
# 			c=random.choice(ch)
# 			ch.remove(c)

# 			print("\t"*i,end="\r")
# 			b.append(int(c))
# 		d.append(b)
# 	a=d

# 	print(d,end="\r")

# jj=[]
# for i in dd.values():
# 	if i not in jj:
# 		jj.append(i)
# print("------------------------------------OUR FINAL RESULT--------------------------------")
# for i in jj:
# 	for a in i:
# 		print("\t"*5,a)
# 	print("Next")
# print("------------------------------------OUR RESULT END--------------------------------")



#####################
############################################
#####################




# import random
# a=[[0,0,0],[0,1,0],[0,0,0]]
# dd={}
# n=15
# ln=1
# lln=10
# while True:

# 	ch=[i for i in range(ln,lln)]
# 	d=[]
# 	for i in a:
# 		b=[]
# 		for i in range(len(a)):
# 			c=random.choice(ch)
# 			ch.remove(c)

# 			print("\t"*i,end="\r")
# 			b.append(int(c))
# 		d.append(b)
# 	a=d

# 	print(d,end="\r")

# 	horizondal=[]
# 	vertical=[]
# 	diagonal=[]
# 	andiagonal=[]

# 	for i in a:
# 		horizondal.append(sum(i))
# 	for i in range(len(a)):
# 		diagonal.append(a[i][i])
# 	l=2
# 	for i in range(len(a)):
# 		andiagonal.append(a[i][l])
# 		l-=1
# 	for i in range(len(a)):
# 		b=[]
# 		for j in a:
# 			b.append(j[i])
# 		vertical.append(sum(b))

# 	if horizondal[0]==horizondal[1]==horizondal[2]==sum(diagonal)==sum(andiagonal)==vertical[0]==vertical[1]==vertical[2] :
# 		print("\nMagic square\n")

# 		if len(dd)!=3:
# 			dd[n]=d
# 			# print(dd)
# 		else:
# 			print(dd)
# 			break

# 		n=int(input("enter the number :"))
# 		ln=(n//3)-4
# 		lln=(n//3)+5

# print("YOU HAVE THESE OPTIONS")
# for x,i in enumerate(dd,start=1):
# 	print("\t"*2,x,".",i)
# print("SELECT ANY ONE")
# for i in dd:
# 	z=int(input(" n  :"))
# 	for j in dd[z]:
# 		print(j)


####################################################################################################################################################################
# import random
# def magic_square(a):
# 	horizondal=[]
# 	vertical=[]
# 	diagonal=[]
# 	antidiagonal=[]
# 	for i in a:
# 		horizondal.append(sum(i))
# 	for i in range(len(a)):
# 		diagonal.append(a[i][i])
# 	l=2
# 	for i in range(len(a)):
# 		antidiagonal.append(a[i][l])
# 		l-=1
# 	for i in range(len(a)):
# 		b=[]
# 		for j in a:
# 			b.append(j[i])
# 		vertical.append(sum(b))
# 	if horizondal[0]==horizondal[1]==horizondal[2]==vertical[0]==vertical[1]==vertical[2]==sum(diagonal)==sum(antidiagonal):
# 		print("magic_square")
# 		for i in a:
# 			print(i)
# 		return True
# 	return False
# def randomly_created_magic_square():
# 	allsum=int(input("(MAGIC SQUARE) ENTER A NUMBER FROM 3'S TABLE :"))
# 	while 1:
# 		start=allsum//3-4
# 		end=allsum//3+5
# 		No_in_magic_square=[i for i in range(start,end)]
# 		zz=[]
# 		for i in range(3):
# 			z=[]
# 			for j in range(3):
# 				g=random.choice(No_in_magic_square)
# 				No_in_magic_square.remove(g)
# 				z.append(g)
# 			zz.append(z)

# 		if magic_square(zz):
# 			break

# randomly_created_magic_square()

###############################################################################3
# import random
# import math
# allmagic=int(input("MAGIC SQUARE 3x3 OR 5x5 :"))
# allsum=int(input("(MAGIC SQUARE) ENTER A NUMBER FROM 3'S TABLE :"))
# while 1:
# 	start=allsum//allmagic-math.floor((allmagic**2)/2)
# 	end=allsum//allmagic+math.ceil((allmagic**2)/2)
# 	No_in_magic_square=[i for i in range(start,end)]
# 	zz=[]
# 	for i in range(allmagic):
# 		z=[]
# 		for j in range(allmagic):
# 			g=random.choice(No_in_magic_square)
# 			No_in_magic_square.remove(g)
# 			z.append(g)
# 		zz.append(z)
# 	a=zz
# 	print(a)
# 	horizondal=[]
# 	vertical=[]
# 	diagonal=[]
# 	antidiagonal=[]
# 	for i in a:
# 		horizondal.append(sum(i))
# 	for i in range(len(a)):
# 		diagonal.append(a[i][i])
# 	l=allmagic-1
# 	for i in range(len(a)):
# 		antidiagonal.append(a[i][l])
# 		l-=1
# 	for i in range(len(a)):
# 		b=[]
# 		for j in a:
# 			b.append(j[i])
# 		vertical.append(sum(b))
# 	horizondal=set(horizondal)
# 	horizondal=list(horizondal)
# 	vertical=set(vertical)
# 	vertical=list(vertical)

# 	if len(horizondal)==len(vertical)==1:
# 		if  sum(diagonal)==sum(antidiagonal)==allsum==sum(horizondal)==sum(vertical):
# 			print("magic_square")
# 			for i in a:
# 				print(i)
# 			break

########################################################################################
# import random
# a=[[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# while 1:
# 	horizondal=[]
# 	vertical=[]
# 	diagonal=[]
# 	antidiagonal=[]
# 	for i in a:
# 		horizondal.append(sum(i))
# 	for i in range(len(a)):
# 		diagonal.append(a[i][i])
# 	l=4
# 	for i in range(len(a)):
# 		antidiagonal.append(a[i][l])
# 		l-=1
# 	for i in range(len(a)):
# 		b=[]
# 		for j in a:
# 			b.append(j[i])def h(s,l):
# 	a=s
# 	b=l
# 	c=a.split(" ")
# 	d=b.split(" ")
# 	Daya=c[0]
# 	Daye=d[0]
# 	Montha=c[1]
# 	Monthe=d[1]
# 	Yeara=c[2]
# 	yeare=d[2]
# 	fine=15*(int(Daya)-int(Daye)) if int(Montha)==int(Monthe) and int(Yeara)==int(yeare) else 500*(int(Montha)-int(Monthe)) if int(Montha)>int(Monthe) and int(Yeara)==int(yeare) else 10000 if int(Yeara)>int(yeare) else 0
# 	print(fine)


# h(input(),input())
# 		vertical.append(sum(b))
# 	if vertical[0]==vertical[1]==vertical[2]==vertical[3]==vertical[4]==horizondal[0]==horizondal[1]==horizondal[2]==horizondal[3]==horizondal[4]==sum(diagonal)==sum(antidiagonal):
# 		print("magic_square")
# 		break

# 	v=[i for i in range(1,26) if i != 13]
# 	nnn=[]
# 	for i in range(len(a)):
# 		nn=[]
# 		for j in range(len(a)):
# 			if i == 2 and j==2:
# 				n=13
# 				nn.append(n)
# 			else:
# 				n=random.choice(v)
# 				nn.append(n)
# 				v.remove(n)
# 		nnn.append(nn)
# 	print(nnn)
# 	a=nnn

###################################################################################################################################################################
# import string
# import random
# def check(allsum):
# 	import string
# 	if allsum=="":
# 		return False
# 	al=list(allsum)
# 	z=len(al)
# 	count=0
# 	s=[i for i in string.digits]
# 	for i in al:
# 		if i in s:
# 			count+=1
# 	if count==z:
# 		return True
# 	return False

# def magic_square(a):
# 	horizondal=[]
# 	vertical=[]
# 	diagonal=[]
# 	antidiagonal=[]
# 	for i in a:
# 		horizondal.append(sum(i))
# 	for i in range(len(a)):
# 		diagonal.append(a[i][i])
# 	l=2
# 	for i in range(len(a)):
# 		antidiagonal.append(a[i][l])
# 		l-=1
# 	for i in range(len(a)):
# 		b=[]
# 		for j in a:
# 			b.append(j[i])
# 		vertical.append(sum(b))
# 	if horizondal[0]==horizondal[1]==horizondal[2]==vertical[0]==vertical[1]==vertical[2]==sum(diagonal)==sum(antidiagonal):
# 		print("magic_square")
# 		for i in a:
# 			print(i)
# 		return True
# 	return False
# def randomly_created_magic_square():
# 	allsum=input("(MAGIC SQUARE) ENTER A NUMBER FROM 3'S TABLE :")
# 	if not check(allsum):
# 		print("please enter a number")
# 	elif(int(allsum)%3 != 0):
# 		print("Please Enter the number comes under the 3's table")
# 	else:
# 		allsum=int(allsum)
# 		while 1:
# 			start=allsum//3-4
# 			end=allsum//3+5
# 			No_in_magic_square=[i for i in range(start,end)]
# 			zz=[]
# 			for i in range(3):
# 				z=[]
# 				for j in range(3):
# 					g=random.choice(No_in_magic_square)
# 					No_in_magic_square.remove(g)
# 					z.append(g)
# 				zz.append(z)

# 			if magic_square(zz):
# 				break

# randomly_created_magic_square()

# ###################################################################################################################################################################
# import string
# import random
# def check(allsum):
# 	import string
# 	if allsum=="":
# 		return False
# 	al=list(allsum)
# 	z=len(al)
# 	count=0
# 	s=[i for i in string.digits]
# 	for i in al:
# 		if i in s:
# 			count+=1
# 	if count==z:
# 		return True
# 	return False

# def magic_square(a):
# 	horizondal=[]
# 	vertical=[]
# 	diagonal=[]
# 	antidiagonal=[]
# 	for i in a:
# 		horizondal.append(sum(i))
# 	for i in range(len(a)):
# 		diagonal.append(a[i][i])
# 	l=2
# 	for i in range(len(a)):
# 		antidiagonal.append(a[i][l])
# 		l-=1
# 	for i in range(len(a)):
# 		b=[]
# 		for j in a:
# 			b.append(j[i])
# 		vertical.append(sum(b))
# 	if horizondal[0]==horizondal[1]==horizondal[2]==vertical[0]==vertical[1]==vertical[2]==sum(diagonal)==sum(antidiagonal):
# 		print("magic_square")
# 		for i in a:
# 			print(i)
# 		return True
# 	return False
# def randomly_created_magic_square():
# 	allsum=input("(MAGIC SQUARE) ENTER A NUMBER FROM 3'S TABLE :")
# 	if not check(allsum):
# 		print("please enter a number")
# 	elif(int(allsum)%3 != 0):
# 		print("Please Enter the number comes under the 3's table")
# 	else:
# 		allsum=int(allsum)
# 		while 1:
# 			start=allsum//3-4
# 			end=allsum//3+5
# 			No_in_magic_square=[i for i in range(start,end)]
# 			zz=[]
# 			for i in range(3):
# 				z=[]
# 				for j in range(3):
# 					g=random.choice(No_in_magic_square)
# 					No_in_magic_square.remove(g)
# 					z.append(g)
# 				zz.append(z)

# 			if magic_square(zz):
# 				break

# randomly_created_magic_square()

#########################################################################################################################
from connected_to_web_page import magic_square_ as h
import string
import random
def check(allsum):
	import string
	if allsum=="":
		return False
	al=list(allsum)
	z=len(al)
	count=0
	s=[i for i in string.digits]
	for i in al:
		if i in s:
			count+=1
	if count==z:
		return True
	return False

def magic_square(a):
	horizondal=[]
	vertical=[]
	diagonal=[]
	antidiagonal=[]
	for i in a:
		horizondal.append(sum(i))
	for i in range(len(a)):
		diagonal.append(a[i][i])
	l=2
	for i in range(len(a)):
		antidiagonal.append(a[i][l])
		l-=1
	for i in range(len(a)):
		b=[]
		for j in a:
			b.append(j[i])
		vertical.append(sum(b))
	if horizondal[0]==horizondal[1]==horizondal[2]==vertical[0]==vertical[1]==vertical[2]==sum(diagonal)==sum(antidiagonal):
		print("magic_square")
		for i in a:
			print(i)
		h(a[0],a[1],a[2])
		return True
	return False
def randomly_created_magic_square():
	allsum=input("(MAGIC SQUARE) ENTER A NUMBER FROM 3'S TABLE :")
	if not check(allsum):
		print("please enter a number")
	elif(int(allsum)%3 != 0):
		print("Please Enter the number comes under the 3's table")
	else:
		allsum=int(allsum)
		while 1:
			start=allsum//3-4
			end=allsum//3+5
			No_in_magic_square=[i for i in range(start,end)]
			zz=[]
			for i in range(3):
				z=[]
				for j in range(3):
					g=random.choice(No_in_magic_square)
					No_in_magic_square.remove(g)
					z.append(g)
				zz.append(z)

			if magic_square(zz):
				break

randomly_created_magic_square()
