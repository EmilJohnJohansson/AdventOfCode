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
        self.bit_counts = [0] * len(binaries[0].as_arr)
        self.cutoff = self.get_cutoff()
        self.result = self.diagnose()

    def get_cutoff(self):
        return len(self.binaries) / 2

    def diagnose(self):
        for bin in self.binaries:
            for i in range(0, len(self.bit_counts)):
                self.bit_counts[i] = self.bit_counts[i] + bin.as_arr[i]
        gamma = ""
        for sum in self.bit_counts:
            if sum > self.cutoff:
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