# CPU2С
#### A CPU made using Python class
## Defining

    Name = CPU(Name, Socket, PerfCores, EffCores, Threads, Cache, L2Cache, BaseFreq, MaxRAMSupport, MaxPCIELanes, BuiltInGPU)

##  Functions

    toggle(returnState=True, force=False)
Toggles the CPU. If returnState is enabled, returns new state of CPU. If force enabled, CPU skips checking of cores and socket and powers on.
    
    stats()
Prints statistics of CPU

    togglePerfCores(returnState=True):
Toggles Performance cores on the CPU. If returnState is enabled, returns new state of Performance cores of the CPU.