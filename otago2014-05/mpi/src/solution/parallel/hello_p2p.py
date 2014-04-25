from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
	for i in range(size):
		sendMsg = "Hello, Rank %d" %i
		comm.send(sendMsg, dest=i)
else:
	recvMsg = comm.recv(source=0)
	print recvMsg

