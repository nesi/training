# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:21:24 2013

@author: Sung Bae
"""
import time
@profile
def Pi(num_steps):
	start = time.time()
	step = 1.0/num_steps

	sum = 0
	for i in range(num_steps):
		x= (i+0.5)*step
		sum = sum + 4.0/(1.0+x*x)    
    
	pi = step * sum

	end = time.time()
	print "Pi with %d steps is %.20f in %f secs" %(num_steps, pi, end-start)

if __name__ == '__main__':\
	Pi(100000000)


