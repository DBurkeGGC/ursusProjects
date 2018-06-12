from random import *
from math import sqrt
import time
def main():
	"Monte Carlo Calculation of Pi\nPython, Non-Vectorized"
	trial=0
	trialset=[10**1,10**2,10**3,10**4,10**5,10**6,10**7]
	for value in trialset:
		inside=0
		for i in range(0,value):
			x=random()
			y=random()
			if sqrt(x*x+y*y)<=1:
				inside+=1
		pi=4*inside/value
		trial+=1
		print("Trials: 10 ^",trial, "\tPi Estimation:",pi)

if __name__ == "__main__":
	print(main.__doc__)
	start=time.time()
	main()
	print("Execution Time: ",time.time()-start)
