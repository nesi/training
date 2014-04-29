from mpi4py import MPI

comm = MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()

val = (rank+1)*10
print "Rank %d has value %d" %(rank, val)

if rank == 0:
	sum = val 
	for i in range(1,size):
		sum += comm.recv(source=i)
	print "Rank 0 worked out the total %d" %sum

else:
	comm.send(val, dest=0)

