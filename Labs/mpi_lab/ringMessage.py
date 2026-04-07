from mpi4py import MPI
import numpy as np
from numpy import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    message = f"hello world! {random.randint(1, 10)}"
    comm.send(message, dest=1)
    final = comm.recv(source=size-1)
    print(final)
 
else:
    message = comm.recv(source=rank-1)

    current = int(message.split()[-1])
    message += f" { current * rank}"
    
    if rank == size - 1:
        message += " goodbye world!"
        comm.send(message, dest=0)
    else:
        comm.send(message, dest=rank+1)



