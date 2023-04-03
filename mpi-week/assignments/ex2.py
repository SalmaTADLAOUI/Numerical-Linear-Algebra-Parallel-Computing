from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank ==0:
      data = int(input("enter a number "))
else:
      data = None

data = comm.bcast(data, root=0)
if data < 0:
      print('Invalid input')
else :
      print('Process ',rank ,"got ",data )
