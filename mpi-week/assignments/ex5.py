from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
def pi(N):
    sum = 0
    for i in range(1,N):
        sum += 1/( 1 + ((i-1/2)/N)**2)
    return (4/N)*sum
N= 840
print("rank {} value {} ".format(rank,pi(N)))
