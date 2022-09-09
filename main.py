class CPU:
    def __init__(self, Socket, PerfCores=0, EffCores=0, Threads=0, Cache=0, L2Cache=0, BaseFreq=0.0, MaxRAMSupport=0,
                 MaxPCIELanes=0, BuiltInGPU=None):
        self.Socket = Socket
        self.PerfCores = PerfCores
        self.EffCores = EffCores
        self.TotalCores = PerfCores + EffCores
        self.Threads = Threads
        self.Cache = Cache
        self.L2Cache = L2Cache
        self.BaseFreq = BaseFreq
        self.MaxRAMSupport = MaxRAMSupport
        self.MaxPCIELanes = MaxPCIELanes
        self.BuiltInGPU = BuiltInGPU


i9_12900KS = CPU("FCLGA1700", 8, 8, 24, 30, 14, 3.4, 128, 20, "UHD Graphics 770")
