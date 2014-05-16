from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
	for i in range(1,size):
		sendMsg = "Hello, Rank %d" %i
		comm.send(sendMsg, dest=i,tag=0)
else:
	st = MPI.Status()
	
	recvMsg = comm.recv(source=0, tag=0, status=st)
	print "%s (error=%d)" %(recvMsg,st.Get_error())

