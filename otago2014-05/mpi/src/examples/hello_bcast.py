from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
	comm.bcast("Hello from Rank 0", root=0)
else:
	msg=comm.bcast(root=0)
	print "Rank %d received: %s" %(rank, msg)



