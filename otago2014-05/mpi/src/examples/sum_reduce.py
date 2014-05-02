from mpi4py import MPI

comm = MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()

val = (rank+1)*10
print "Rank %d has value %d" %(rank, val)
sum = comm.reduce(val, op=MPI.SUM, root=0)
if rank==0:
	print "Rank 0 worked out the total %d" %sum

