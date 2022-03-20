import queue
import sys

proc_kolv = sys.stdin.readline().split(' ')
ochered = sys.stdin.readline().split(' ')
proc = int(proc_kolv[0])
kolv = int(proc_kolv[1])
derevo = queue.PriorityQueue()

for z in range(proc):
    derevo.put([0,proc,z])
for x in ochered:
    x = int(x)
    verh = derevo.get()
    if x < 1:
        print(verh[2], verh[0])
        derevo.put(verh)
        continue
    else:
        print(verh[2], verh[0])
        verh[0] += x
        derevo.put(verh)
