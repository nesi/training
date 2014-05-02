# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:21:24 2013

@author: Sung Bae
"""
import time
import pi_cython as cpi
from mpi4py import MPI

#@profile
def Pi(num_steps):
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size()

	sum = 0
	start = time.time()

	# Call the function implemented in the C extention here
	num_steps2 = num_steps/size
	begin = num_steps2 * rank
	end = num_steps2 * (rank+1)
	local_sum = cpi.loop(num_steps,begin,end)

	sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

	if rank == 0:

		end = time.time()
		pi = sum/num_steps
		print "Pi with %d steps is %.20f in %f secs"\
			 %(num_steps,\
			 pi, end-start)


if __name__ == '__main__':\
	Pi(100000000)

