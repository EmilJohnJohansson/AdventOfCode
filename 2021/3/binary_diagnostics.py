import sys

def run():
    puzzleInputPath = sys.argv[1]
    binaries = parse_input(puzzleInputPath)
    diagnostics = Diagnostics(binaries)
    print(diagnostics.result)

class BinaryNumber:
    def __init__(self, line):
        self.bin = int(line, 2)
        self.as_arr = [int(x) for x in list(line.strip())]

class Diagnostics:
    def __init__(self, binaries):
        self.binaries = binaries
        self.sums = [0] * len(binaries[0].as_arr)
        self.result = self.diagnose()

    def diagnose(self):
        for bin in self.binaries:
            for i in range(0, len(self.sums) - 1):
                self.sums[i] = self.sums[i] + bin.as_arr[i]  
        gamma = ""
        half = len(self.binaries) / 2
        for sum in self.sums:
            if sum >= half:
                gamma = gamma + "1"
            else:
                gamma = gamma + "0"
        epsilon = gamma.replace('0', 'x').replace('1', '0').replace('x','1')
        return int(gamma, 2) * int(epsilon, 2)    

def parse_input(path):
    return [BinaryNumber(line) for line in get_input(path)]

def get_input(path):
    with open(path) as f:
        return f.readlines()

if __name__ == "__main__":
    run()