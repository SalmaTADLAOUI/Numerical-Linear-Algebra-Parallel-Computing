from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
n=8
m=8

if rank==0:
    A = np.random.rand(n,m)
else:
    A = None
    
# Scatter the data of A to all the processors
counts = [int(n*m/size) if i < size-1 else n*m-int(n*m/size)*i for i in range(size)]
displs = [int(n*m/size)*i for i in range(size)]
submat_A = np.zeros(counts[rank])

comm.Scatterv([A, counts, displs, MPI.DOUBLE], submat_A, root=0)

if rank == 1:
        submat_A = submat_A.reshape(n // 2, m // 2)[:, m // 2:]
elif rank == 2:
        submat_A = submat_A.reshape(n // 2, m // 2)[n // 2:, :]
elif rank == 3:
        submat_A = submat_A.reshape(n // 2, m // 2)[n // 2:, m // 2:]
        
#gather results to processor 0
A_gath = None
if rank == 0:
        A_gath = np.zeros((n, m))
comm.Gatherv(submat_A, [A_gath, counts, displs, MPI.DOUBLE], root=0)

if rank == 0:
    print(f" Rank {rank} matrix :\n", A)
    print("Rank 1 sub_matrix 1:\n", A_gath[:n//2, m//2:])
    print("Rank 2 sub_matrix  2:\n", A_gath[n//2:, :m//2])
    print("Rank 2 sub_matrix  3:\n", A_gath[n//2:, m//2:])
                        
    
    
