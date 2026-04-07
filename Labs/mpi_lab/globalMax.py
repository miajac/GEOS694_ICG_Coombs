from mpi4py import MPI
import numpy as np
from numpy import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

value = random.randint(0,1000)

global_max = comm.reduce(value, op=MPI.MAX, root=0)

global_max = comm.bcast(global_max, root=0)

if value == global_max:
    print(f"Rank {rank} has value {value} which is the global max {global_max}")
else:
    print(f"Rank {rank} has value {value} which is less than global max {global_max}")
