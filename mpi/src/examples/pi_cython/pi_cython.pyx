# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:21:24 2013

@author: Sung Bae
"""
def loop(int num_steps):
	cdef int i
	cdef double sum, step, x
	step = 1.0/num_steps
	sum = 0
	for i in xrange(num_steps):
		x= (i+0.5)*step
		sum = sum + 4.0/(1.0+x*x)
	return sum



