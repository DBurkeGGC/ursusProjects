from mpi4py import MPI
import numpy as np

def main():
	"Module 6 (Non-blocking)"

	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size()
	ARRSIZE = 10**7
	result = []
	
	if rank == 0:
		start = MPI.Wtime()
		for i in range(1,size):
			reqin = comm.irecv(source = MPI.ANY_SOURCE, tag = 22)
			data = reqin.wait()
			result.append(data)
		print("Module 6 (Non-blocking)\n")
		print("RAW ARRAY:\t",result,"\n")
		print("Average Pi Estimation:\t",(sum(i['pi'] for i in result)/len(result)))
		print("Average Execution Time:\t",(sum(i['time'] for i in result)/len(result)))
		print("Total Execution Time:\t",MPI.Wtime()-start,"\n")
		for i in result:
			print("Pi Estimation:\t",i['pi'],"\tExecution Time:\t",i['time'])
		return result
	else:
		start = MPI.Wtime()
		data = np.random.rand(ARRSIZE*2)
		inside = np.sum((data[:ARRSIZE]**2 + data[ARRSIZE:]**2) <= 1)
		pi = 4 * inside / ARRSIZE
		time = MPI.Wtime()-start
		data = {'pi':pi,'time':time} 
		reqout = comm.isend(data, dest = 0, tag = 22)
		reqout.wait()

if __name__ == "__main__":
        main()
