"""

Queue : [1,2,3]
- FIFO (First In,First Out ) :::   [1,2,3] -> [1,2,3]
- LIFO (Last In, First Out)  :::   [1,2,3] -> [3,2,1]
"""
from collections import deque

q_lifo = deque()
q_fifo = deque()


for i in range(4):
    q_lifo.append(i)
    q_fifo.append(i)

# Remove


print(f'Queue Lifo: {q_lifo} | Remove :{q_lifo.popleft()} | Queue now: {q_lifo}')
print(f'Queue Fifo: {q_fifo} | Remove :{q_fifo.pop()} | Queue now: {q_fifo}') #Stack

###
from queue import Queue

q_ini = Queue(maxsize = 100)
q_ini.put(10)
q_ini.put(5)

print(f"Queue: {q_ini} | Size : {q_ini.qsize()} | Full :{q_ini.full()} | {q_ini.get()}")
print(f"Queue: {q_ini} | Size : {q_ini.qsize()} | Full :{q_ini.full()} | {q_ini.get()}")