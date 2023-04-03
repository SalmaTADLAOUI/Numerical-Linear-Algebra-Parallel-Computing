from mpi4py import MPI
COMM = MPI.COMM_WORLD
SIZE = COMM.Get_size()
RANK = COMM.Get_rank()

print("I am the proccess {RANK} among {SIZE}".format(RANK =RANK, SIZE =SIZE))
