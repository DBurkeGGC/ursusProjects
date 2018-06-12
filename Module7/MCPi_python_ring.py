from mpi4py import MPI
import numpy as np

def main():

	"Module 6 (Non-blocking, Ring)"

	#Begin timing
	start = MPI.Wtime()	

	#Communication
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size()

	#Vector size for x and y
	ARRSIZE = 10**7

	#Buffer for receiver
	buffer = np.empty(ARRSIZE*2, dtype=np.float64)

	#Var initialization
	result = []
	next = 0
	
	#Create vector
	data = np.random.rand(ARRSIZE*2).astype(np.float64)

	#Evaluate next in ring
	if rank != size - 1:
		next = rank + 1
	
	#Send and receive vector
	reqout = comm.Isend([data, ARRSIZE*2, MPI.DOUBLE], dest = next, tag = 11)	
	reqin = comm.Irecv([buffer, ARRSIZE*2, MPI.DOUBLE], source = MPI.ANY_SOURCE, tag = 11)
	MPI.Request.Waitall([reqout, reqin])

	#Process vector
	inside = np.sum((buffer[:ARRSIZE]**2 + buffer[ARRSIZE:]**2) <= 1)
	pi = 4 * inside / ARRSIZE
	time = MPI.Wtime() - start
	data = {'pi':pi, 'time':time, 'rank':rank}

	#If master
	if rank == 0:

		#Append this result
		result.append(data)

		#Gather other results
		for i in range(1, size):	
			reqin = comm.irecv(source = MPI.ANY_SOURCE, tag = 22)
			result.append(reqin.wait())
		
		#Output results
		print("Module 6 (Non-blocking, Ring)\n")
		print("RAW ARRAY:\t", result, "\n")
		print("Average Pi Estimation:\t", (sum(i['pi'] for i in result) / len(result)))
		print("Average Execution Time:\t", (sum(i['time'] for i in result) / len(result)))
		print("Total Execution Time:\t", MPI.Wtime() - start, "\n")

		for i in result:
			print("Rank:\t", i['rank'], "\tPi Estimation:\t", i['pi'], "\tExecution Time:\t", i['time'])
	else:

		#Send result to master
		comm.isend(data, dest = 0, tag = 22)

if __name__ == "__main__":
	main()
