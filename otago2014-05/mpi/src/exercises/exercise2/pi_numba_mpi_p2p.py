# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:21:24 2013

@author: Sung Bae
"""
import time
from mpi4py import MPI
from numba import jit

@jit
def loop(num_steps, begin, end):
	step = 1.0/num_steps
	sum = 0

	for i in xrange(begin,end):
		x= (i+0.5)*step
		sum = sum + 4.0/(1.0+x*x)
	return sum

 
def Pi(num_steps):
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size()
    
	start = time.time()

	

	#arrange each process such that it will compute 
	# rank 0 : 0...num_steps/size
	# rank 1 : num_steps/size, 2*num_steps/size
	# rank 2 : 2*num_steps/size, 3*num_steps/size
	# rank 3 : 3*num_steps/size, 4*num_steps/size
	# ....

	local_num_steps = num_steps/size
  	local_sum = loop(num_steps, ???, ???) # Fix this line here

	end = time.time()
	#print "Rank %d is sending local_sum=%f" %(rank,local_sum)
	if rank > 0:
		comm.send(local_sum, dest=0)
	else:
		sum = local_sum
		for i in range(1,size):
			local_sum = comm.recv(source=i)
	#		print "Rank 0 received from rank %d local_sum=%f" %(rank,local_sum)
			sum += local_sum
        
		pi = sum / num_steps
		print "Pi with %d steps is %.20f in %f secs" %(num_steps, pi, end-start)
		
       

if __name__ == '__main__':
	Pi(100000000)
	
    
    
        
        

    
    
