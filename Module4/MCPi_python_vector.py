import numpy as np
import time
def main():
	"Monte Carlo Calculation of Pi\nPython, Vectorized"
	trial=0
	trialset=[10**1,10**2,10**3,10**4,10**5,10**6,10**7]
	for value in trialset:
		inside=np.sum((np.random.rand(value)**2+np.random.rand(value)**2)<=1)
		pi=4*inside/value
		trial+=1
		print("Trials: 10 ^",trial,"\tPi Estimation: ",pi)

if __name__ == "__main__":
	print(main.__doc__)
	start=time.time()
	main()
	print("Execution Time: ",time.time()-start)
