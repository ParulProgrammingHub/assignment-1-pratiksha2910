Subject1 = input ("Enter the value of Subject1:")
Subject2 = input ("Enter the value of Subject2:")
Subject3 = input ("Enter the value of Subject3:")
Subject4 = input ("Enter the value of Subject4:")
Subject5 = input ("Enter the value of Subject5:")
total = Subject1+Subject2+Subject3+Subject4+Subject5
mean = total/5
percentage=(total*100)/500
print "mean:",mean
print(total)
print "percentage:",percentage
if (percentage < 35) :
	print("Fail")
else :
	print("Pass")
