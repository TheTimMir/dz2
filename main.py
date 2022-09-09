class CPU:
    def __init__(self, Name=None, Socket=None, PerfCores=0, EffCores=0, Threads=0, Cache=0, L2Cache=0, BaseFreq=0.0,
                 MaxRAMSupport=0,
                 MaxPCIELanes=0, BuiltInGPU=None):
        self.Name = Name
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
        self.Enabled = False
        self.PerfCoresEnabled = False

    def toggle(self, returnState=True, force=False):
        if self.Enabled:
            self.Enabled = False
            self.PerfCoresEnabled = False
        elif force:
            self.Enabled = True
            self.PerfCoresEnabled = True
        elif self.TotalCores > 0 and self.Socket is not None:
            self.Enabled = True
            self.PerfCoresEnabled = True
        if returnState:
            return self.Enabled

    def stats(self):
        print(f"     Stats: \n> Name:{self.Name}\n> Socket: {self.Socket}\n> Toggled: {self.Enabled}\n> Performance "
              f"cores toggled: {self.PerfCoresEnabled}\n> Built-in graphics: {self.BuiltInGPU}")

    def togglePerfCores(self, returnState=True):
        if self.PerfCoresEnabled:
            self.PerfCoresEnabled = False
        elif self.Enabled:
            self.PerfCoresEnabled = True
        if returnState:
            return self.PerfCoresEnabled


i9_12900KS = CPU("I9-12900KS", "FCLGA1700", 8, 8, 24, 30, 14, 3.4, 128, 20, "UHD Graphics 770")
print(i9_12900KS.toggle())  # enable
print(i9_12900KS.togglePerfCores())  # switch off performance cores
i9_12900KS.stats()
print(i9_12900KS.toggle())  # disable
print(i9_12900KS.togglePerfCores(), "\n")  # try to turn on perf cores

i9_12900K = CPU("I9-12900K", None, 8, 8, 24, 30, 14, 3.4, 128, 20, "UHD Graphics 770")
print(i9_12900K.toggle())  # Doing nothing bc the CPU isn't plugged into socket
i9_12900KS.stats()
