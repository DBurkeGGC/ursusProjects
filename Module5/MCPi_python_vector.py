from joblib import Parallel, delayed
import numpy as np
import time


def main():
	"\nMonte Carlo Calculation of Pi\nPython, Vectorized, Parallel\n"
	trialset=[10**7]*8
	result=Parallel(n_jobs=4)(delayed(processInput)(value) for value in trialset)
	return result

def processInput(value):
	start=time.time()
	inside=np.sum((np.random.rand(value)**2+np.random.rand(value)**2)<=1)
	pi=4*inside/value
	end=time.time()
	return [pi,start,end]
		
if __name__ == "__main__":
	print(main.__doc__)
	result=main()
	print("RAW ARRAY:\t",result,"\n")
	print("Average Pi Estimation:\t",(sum([i[0] for i in result]) / len(result)),"\n")
	print("Average Execution Time:\t",(sum([value[2]-value[1] for value in result]) / len(result)),"\n")
	for value in result:
		print("Pi Estimation:\t",value[0],"\tExecution Time:\t",value[2]-value[1],"\n")
