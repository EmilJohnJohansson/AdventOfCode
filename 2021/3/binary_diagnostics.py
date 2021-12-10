import sys
import copy

def run():
    puzzleInputPath = sys.argv[1]
    binaries = parse_input(puzzleInputPath)
    diagnostics = Diagnostics(binaries)
    print(diagnostics.diagnose_gamma_and_epsilon())
    print(diagnostics.diagnose_oxy_and_co2())

class BinaryNumber:
    def __init__(self, line):
        self.bin = int(line, 2)
        self.as_arr = [int(x) for x in list(line.strip())]

class Diagnostics:
    def __init__(self, binaries):
        self.binaries = binaries
        self.bit_counts = self.set_bit_counts(binaries)
        self.cutoff = self.set_cutoff()

    def set_bit_counts(self, binaries):
        bit_counts = [0] * len(binaries[0].as_arr)
        for bin in binaries:
            for i in range(0, len(bit_counts)):
                bit_counts[i] = bit_counts[i] + bin.as_arr[i]
        return bit_counts

    def set_cutoff(self):
        return len(self.binaries) / 2

    def diagnose_gamma_and_epsilon(self):
        gamma = ""
        for sum in self.bit_counts:
            if sum > self.cutoff:
                gamma = gamma + "1"
            else:
                gamma = gamma + "0"
        epsilon = gamma.replace('0', 'x').replace('1', '0').replace('x','1')
        return int(gamma, 2) * int(epsilon, 2)    

    def diagnose_oxy_and_co2(self):
        oxy = self.find_oxy()
        co2 = self.find_co2()
        print (oxy, co2)
        return  oxy * co2

    def find_oxy(self):
        print("OXY")
        terminate = False
        index = 0
        oxy = copy.deepcopy(self.binaries)
        while terminate == False:
            sums = self.set_bit_counts(oxy)
            if sums[index] >= cutoff(len(oxy)):
                oxy = filter(oxy, 1, index)
            else:
                oxy = filter(oxy, 0, index)
            index = index + 1 
            if len(oxy) <= 1 or len(self.bit_counts) == index:
                return oxy[0].bin

    def find_co2(self):
        print("CO2")
        terminate = False
        index = 0
        co2 = copy.deepcopy(self.binaries)
        while terminate == False:
            sums = self.set_bit_counts(co2)
            if sums[index] >= cutoff(len(co2)):
                co2 = filter(co2, 0, index)
            else:
                co2 = filter(co2, 1, index)
            index = index + 1 
            if len(co2) <= 1 or len(self.bit_counts) - 1 == index:
                return co2[0].bin

def cutoff(length):
    if length % 2 == 0:
        return length / 2
    else:
        return length / 2 + 1

def filter(list, value, index):
    print("old list:")
    for l in list:
        print(l.as_arr)
    print("value = ", value, "index = ", index)
    new_list = []
    for l in list:
        # print("l = ", l.as_arr)
        # print(l.as_arr[index], value)
        if l.as_arr[index] == value:
            new_list.append(l)
    print("new list:")
    for l in new_list:
        print(l.as_arr)
    return new_list

def parse_input(path):
    return [BinaryNumber(line) for line in get_input(path)]

def get_input(path):
    with open(path) as f:
        return f.readlines()

if __name__ == "__main__":
    run()