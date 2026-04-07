from mpi4py import MPI
import numpy as np
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n= int(sys.argv[1])
expected_sum = (n*(n+1))/2

if rank == 0:
    data = np.arange(1, n+1, dtype='i') 
    data_split = np.array_split(data, size)
else:
    data_split = None

local = comm.scatter(data_split, root = 0)
sums = np.sum(local)
sums_gather = comm.gather(sums, root = 0)


if rank == 0:
    all_sum = sum(sums_gather)
    message = f"The sum of 1-{n} is {all_sum} == {expected_sum}."
    print(message)

# run using mpiexec -n 4 python parallelSum.py 1000000

 







