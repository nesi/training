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
	l = range(size)
x=comm.scatter(l, root=0)
print "Rank %d received a scattered int "%rank +str(x)

x = x*10

l2 = comm.gather(x,root=0)
if rank == 0:
	print "Rank %d collected a list" %rank + str(l2)
	#l2 is None at other ranks
 
	

s=""
if rank == 0:
	s="abcdefghijklmnopqrstuvwxyz"
	s=s[:size]
c=comm.scatter(s, root=0)
print "Rank %d: received a scattered character "%rank +str(c)

c=c*10

s2 = comm.gather(c,root=0)
if rank == 0:
	print "Rank %d collected a list of strings" %rank + str(s2)

l=[]
if rank == 0:
	for i in range(size):
		l.append([i]*3)
x=comm.scatter(l, root=0)

print "Rank %d received a scattered list "%rank + str(x)

x= x*2

l2 = comm.gather(x,root=0)
if rank == 0:
	print "Rank %d collected a list" %rank + str(l2)
	#l2 is None at other ranks
 

