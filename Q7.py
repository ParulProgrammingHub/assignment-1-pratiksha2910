Angle1 = input ("Enter first angle=")
Angle2 = input("Enter second angle=")
def Angle3(Angle1,Angle2) :
	Angle3 = 180 - Angle1 - Angle2
	print(Angle3) 
	return;
if (Angle1 > 180 or Angle2 > 180 or (Angle1 + Angle2)>180) :
	print ("Invalid Input")
else :
	Angle3(Angle1,Angle2)

