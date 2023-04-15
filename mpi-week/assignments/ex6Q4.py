from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

partial_sums = []
N = 840
start_time = MPI.Wtime()

# Perform the calculation several times
for i in range(1000):
    if rank == 0:
        sum1 = 0
        for i in range(0, int(N/2)):
            sum1 += 1/(1 + ((i-1/2)/N)**2)
        sum1 = (4/N)*sum1
        partial_sums.append(sum1)

    if rank == 1:
        sum2 = 0
        for i in range(int(N/2),N):
            sum2 += 1/( 1 + ((i-1/2)/N)**2)
        sum2 = (4/N)*sum2
        partial_sums.append(sum2)

    # Wait for all processes to finish before proceeding
    comm.Barrier()

# send partial sums to controller (rank 0)
final_sum = comm.reduce(partial_sums, op=MPI.SUM, root=0)

# controller (rank 0) prints final sum and time taken
if rank == 0:
    end_time = MPI.Wtime()
    print("Final sum: {}".format(sum(final_sum)))
    print("Time taken: {} seconds".format(end_time - start_time))
