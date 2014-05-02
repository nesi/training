"""
Created on Thu May 2 17:06:24 2014

@author: Sung Bae
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# scatter assumes a list at root to have EXACTLY "size" elements.

l=[] #needs initalization for all processes to know what "l" is

if rank == 0:
	l = range(size) #l is [0,1,2,3] at rank 0 if size = 4
x=comm.scatter(l, root=0) #rank 0 scatters l and each process gets one element from l.
print "Rank %d received a scattered int "%rank +str(x)

x = x*10 ##each process updates the value

l2 = comm.gather(x,root=0)
if rank == 0:
	print "Rank %d collected a list" %rank + str(l2)
	#l2 is None at other ranks
 

# you can scatter a list of lists
l=[]
if rank == 0:
	for i in range(size):
		l.append([i]*3)
	#l is [ [0,0,0],[1,1,1],[2,2,2],[3,3,3]] at rank 0 if size = 4
x=comm.scatter(l, root=0) #rank 0 scatters l and each process gets one element from l

print "Rank %d received a scattered list "%rank + str(x)

x= x*2 #double x. eg. [0,0,0] becomes [0,0,0,0,0,0]

l2 = comm.gather(x,root=0)
if rank == 0:
	print "Rank %d collected a list" %rank + str(l2)
	#l2 is None at other ranks
 	


