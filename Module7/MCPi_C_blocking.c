#include <stdio.h>
#include <mpi.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

main(int argc, char **argv) {
	int num_procs, rank;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &num_procs);
	MPI_Status status;

	srand(time(NULL) + rank);
	clock_t start = clock(), end;

	int ARRSIZE = pow(10,7);

	float *values, inside, pi, total, result[3];
	values = malloc(ARRSIZE * 2 * sizeof(float));

	if (rank == 0) {
		for(int proc=1; proc<num_procs; proc++) {
			for(int i=0; i<ARRSIZE*2; i++) {
				values[i] = (float) rand() / (float) RAND_MAX;
			}
			MPI_Send(values, ARRSIZE*2, MPI_FLOAT, proc, 11, MPI_COMM_WORLD);
			MPI_Recv(result, 3, MPI_FLOAT, MPI_ANY_TAG, 22, MPI_COMM_WORLD, &status);
			printf("Rank: %i\t Pi: %f\t Time: %f\n", (int) result[0], result[1], result[2]);
		}
		printf("Total Execution Time: %f SEC\n", ((double) clock() - start) / CLOCKS_PER_SEC);
	}
	else {
		MPI_Recv(values, ARRSIZE*2, MPI_FLOAT, 0, 11, MPI_COMM_WORLD, &status);
		for(int i=0; i<ARRSIZE; i++) {
			if(((values[i]*values[i]) + (values[(i+ARRSIZE)]*values[(i+ARRSIZE)])) <= 1) {
				inside += 1.0;
			}
		}
		pi = 4.0 * inside / ARRSIZE;
		end = clock() - start;
		total = (double) end / CLOCKS_PER_SEC;
		result[0] = rank;
		result[1] = pi;
		result[2] = total;
		MPI_Send(result, 3, MPI_FLOAT, 0, 22, MPI_COMM_WORLD);
		free(values);
	}
	MPI_Finalize();
}
