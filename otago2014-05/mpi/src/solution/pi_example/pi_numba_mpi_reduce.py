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
        num_steps2 = num_steps/size
        local_sum = loop(num_steps, \
                                rank*num_steps2, \
                                (rank+1)*num_steps2)

        end = time.time()
        sum = comm.reduce(local_sum, root=0)
        if (rank == 0):
                pi = sum / num_steps
                print "Pi with %d steps is %.20f in %f secs" %(num_steps, pi, end-start)


if __name__ == '__main__':
        Pi(100000000)

