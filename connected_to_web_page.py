oht="<html>"
cht="</html>"
oh="<head>"
ch="</head>"
ob="<body>"
cb="</body>"
line1="<!DOCTYPE html>"
ot="<title>"
title0="PYTHON"
ct="</title>"
r="<meta http-equiv=\"refresh\" content=\"3\">"
p="<p>"
pc="</p>"
h1="<h1>"
h1c="</h1>"

def g():
	a=[line1,oht,oh,ot,title0,ct,r,ch,ob,cb,cht]
	with open("connected_html.html","w+") as k:
		for i in a:
			k.write(i+"\n")

# lis=[line1,oht,oh,ot,title,ct,r,ch,ob,cb,cht]

# with open("connected_html.html","w+") as k:
# 	for i in lis:
# 		k.write(i+"\n")

# ####################################################################


# oht="<html>"
# cht="</html>"
# oh="<head>"
# ch="</head>"
# ob="<body>"
# cb="</body>"
# line1="<!DOCTYPE html>"
# ot="<title>"
# title="PYTHON"
# ct="</title>"
# r="<meta http-equiv=\"refresh\" content=\"3\">"
# p="<p>"
# pc="</p>"
# h1="<h1>"
# h1c="</h1>"


# lis=[line1,oht,oh,ot,title,ct,r,ch,ob,h1,"MAGIC SQUARE",h1c,cb,cht]

# with open("connected_html.html","w+") as k:
# 	for i in lis:
# 		k.write(i+"\n")


######################################################################


# oht="<html>"
# cht="</html>"
# oh="<head>"
# ch="</head>"
# ob="<body>"
# cb="</body>"
# line1="<!DOCTYPE html>"
# ot="<title>"
# title="PYTHON"
# ct="</title>"
# r="<meta http-equiv=\"refresh\" content=\"1\">"
# p="<p>"
# pc="</p>"
# h1="<h1>"
# h1c="</h1>"


# def magic_square_(a1,a2,a3):
# 	lis=[line1,oht,oh,ot,title,ct,r,ch,ob,h1,"MAGIC SQUARE",h1c,p,a1,pc,p,a2,pc,p,a3,pc,cb,cht]

# 	with open("connected_html.html","w+") as k:
# 		for i in lis:
# 			k.write(i+"\n")


######################################################################


oht="<html>"
cht="</html>"
oh="<head>"
ch="</head>"
ob="<body bgcolor=\"brown\">"
cb="</body>"
line1="<!DOCTYPE html>"
ot="\t<title>"
title="\t\tPYTHON magic_square_"
ct="\t</title>"
r="<meta http-equiv=\"refresh\" content=\"1\">"
p="\t<p>"
pc="\t</p>"
h1="\t<h1>"
h1c="\t</h1>"
table="\t<table>"
tr="\t\t<tr>"
trc="\t\t</tr>"
tablec="\t</table>"
td="\t\t\t<td>"
tdc="\t\t\t</td>"
div="<div>"
divc="</div>"
hr="<hr>"
center="<center>"
centerc="</center>"
style="<style type=\"text/css\">\n\ttable{border:1px dashed red;width: 100px;height: 100px;background-color: gold;}\n\ttd{border:1px solid blue;}</style>"
def magic_square_(a1,a2,a3):
	lis=[line1,oht,oh,ot,title,ct,r,style,ch,ob,center,h1,"\t\tMAGIC SQUARE",h1c,hr,table,tr,td,str(a1[0]),tdc,td,str(a1[1]),tdc,td,str(a1[2]),tdc,trc,tr,td,str(a2[0]),tdc,td,str(a2[1]),tdc,td,str(a2[2]),tdc,trc,tr,td,str(a3[0]),tdc,td,str(a3[1]),tdc,td,str(a3[2]),tdc,trc,tablec,centerc,cb,cht]

	with open("connected_html.html","w+") as k:
		for i in lis:
			k.write(i+"\n")

######################################################################


oht="<html>"
cht="</html>"
oh="<head>"
ch="</head>"
ob="<body bgcolor=\"brown\">"
cb="</body>"
line1="<!DOCTYPE html>"
ot="\t<title>"
title1="\t\tPYTHON tic_tac_toe"
ct="\t</title>"
r="<meta http-equiv=\"refresh\" content=\"1\">"
p="\t<p>"
pc="\t</p>"
h1="\t<h1>"
h1c="\t</h1>"
table="\t<table>"
tr="\t\t<tr align=\"center\">"
trc="\t\t</tr>"
tablec="\t</table>"
td="\t\t\t<td>"
tdc="\t\t\t</td>"
div="<div>"
divc="</div>"
hr="<hr>"
center="<center>"
centerc="</center>"
style="<style type=\"text/css\">\n\ttable{border:1px dashed red;width: 100px;height: 100px;background-color: gold;}\n\ttd{border:1px solid blue;}</style>"

def ti(b,win):
	lis=[line1,oht,oh,ot,title1,ct,r,style,ch,ob,center,h1,"TIC TAC TOE",h1c,hr,table,tr,td,b[0],tdc,td,b[1],tdc,td,b[2],
	tdc,trc,tr,td,b[3],tdc,td,b[4],tdc,td,b[5],tdc,trc,tr,td,b[6],tdc,td,b[7],tdc,td,b[8],tdc,trc,h1,win,h1c,cb,centerc,cht]
	with open("connected_html.html","w+") as k:
		for i in lis:
			k.write(i+"\n")

