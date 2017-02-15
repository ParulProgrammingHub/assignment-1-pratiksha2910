principal = input ("Enter Principal Amount:")
time = input("Time:")
rate = input("Enter interest rate:")
def ci(p,t,R,n) :
	
	r = R/100
	float(r)
	
	a1 = (1+(r/n))
	float(a1)
	print(a1)
	
	a2 = n * t
	float(a2)
	print(a2)
	
	
	C1 = a1 ** a2
	float(C1)
	C2 = p * C1
	float(C2)
	print(C2)
ci(principal,time,rate,12)
