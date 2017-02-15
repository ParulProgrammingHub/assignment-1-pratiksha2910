principal = input ("Enter Principal Amount:")
time = input("Time:")
rate = input("Enter interest rate:")
def simple_interest(p,t,r) :
 Si=p*(1+((r*t)/100))
 print "Simple interst",Si
simple_interest(principal,time,rate)
