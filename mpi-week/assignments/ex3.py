from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank ==0:
       data = int(input("enter a number "))
       comm.send(data, dest = 1)
else:
       data = None

for i in range(1,size):
    if rank == i:
        data = comm.recv(source = i-1)
        print(f"Process {rank} reveiced {data}")
        data += rank
        comm.send(data, dest=(i+1)%size)

#process 0 receive the last ring from the last rank
if rank == 0 :
    data = comm.recv(source = size-1)
    print(f"Process {rank} reveiced {data}")
      
