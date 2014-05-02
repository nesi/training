from mpi4py import MPI

comm = MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()

val = (rank+1)*10
print "Rank %d has value %d" %(rank, val)


req = comm.isend(val, dest=0)

if rank == 0:
	sum = 0 
	for i in range(size):
		sum += comm.recv(source=i)
		status = MPI.Status()
		req.wait(status)
	
	print "Rank 0 worked out the total %d" %sum

