#!C:/Python/python.exe

import cgi, cgitb
print ("Content-type:text/html\r\n\r\n")

cgitb.enable()
form=cgi.FieldStorage()

age=form.getvalue('age')
height=form.getvalue('ht')
weight=form.getvalue('wt')
glucose=form.getvalue('gl')
insulin=form.getvalue('ins')
bp=form.getvalue('bp')
preg=form.getvalue('pg')
tricep=form.getvalue('tri')

DD=form.getvalue('DD')
MD=form.getvalue('MD')
FD=form.getvalue('FD')

print ("<html>")
print ("<head>")
print ("<title>")
print ("Diabetes Prediction System")
print ("</title>")
print ("</head><style>h1 {font-size:55px;color: white; text-shadow: 2px 3px 3px black, 0 0 50px aqua, 0 0 15px crimson;}</style>")
print ("<body style=\"background:linear-gradient(to left, rgba(255,0,0,0), rgba(255,0,0,0.7)); \">")
print ("<center><h1 style=\"padding:20px\">Diabetes Prediction System</h1></center>")

#print (("%s %s %s %s %s %s %s %s %s %s %s") % (age,height,weight,glucose,insulin,bp,preg,tricep,DD,MD,FD))
#print ("<h2>Hello \n %s %s %s</h2>" % (age, height, weight))

#w2=int(weight)
#h2=int(height)
bmi=(float(weight)/((float(height)/100)*(float(height)/100)))
#bmi=(w2/(h2*h2))
#print (("%f")%(bmi))

pdgfn=0.00
if DD=="both":
	if MD=="mb50":
		if FD=="fb50":
			pdgfn=1.25
		elif FD=="fa50":
			pdgfn=0.70
	elif MD=="ma50":
		if FD=="fb50":
			pdgfn=0.63
		elif FD=="fa50":
			pdgfn=0.47
elif DD=="none":
	pdgfn=0.08
elif DD=="m":
	if MD=="ma50":
		pdgfn=0.18
	else:
		pdgfn=0.30
elif DD=="f":
	if FD=="fa50":
		pdgfn=0.15
	else:
		pdgfn=0.25
else:
	pdgfn=0.00

#print (("%f")%(pdgfn))

npreg=float(preg)
gluco=float(glucose)
pressure=float(bp)
skintri=float(tricep)
insu=float(insulin)
cage=float(age)

#input=[npreg,gluco,pressure,skintri,insu,bmi,pdgfn,cage]

file=open("input_file.csv","w+")
file.write(("%f;%f;%f;%f;%f;%f;%f;%f")%(npreg,gluco,pressure,skintri,insu,bmi,pdgfn,cage))
file.close()


from keras.models import load_model
import numpy as np

loaded_model=load_model('Model1.hdf5')
#a = np.asarray(input, dtype = float)
#prediction=loaded_model.predict(a)
#prediction=loaded_model.predict(npreg,gluco,pressure,skintri,insu,bmi,pdgfn,cage)
predicdata=np.loadtxt('input_file.csv',delimiter=';')
prediction=loaded_model.predict(predicdata[None,0:8])

#print ("Prediction = ",prediction[0])
result=float(prediction[0])
#print ("\n",result)
Predict_Percent=(result*100.0)

print ("<table align=\"center\" style=\"width:70%; height:45%; border-radius: 200px 50px; border: 5px solid crimson; padding: 20px;\">")
print ("<tr style=\"vertical-align:center\"><td>")
print ("<br><br><br><center>")
print("<h2 style=\"color:steelblue\">Chances of being diagnosed with diabetes are<br><font color=maroon size=20px>",Predict_Percent,"%</font></h2>")
print ("</center>")
print ("</td></tr>")
print ("</table>")
print ("</body>")
print ("</html>")
