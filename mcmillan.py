input = ["00", "01", "10", "11", "000", "001", "010", "011", "100", "101", "110", "111"]

code_lenghts = [len(l) for l in input]

Mc_Millan_sum = 0

for i in range(len(code_lenghts)):
    Mc_Millan_sum += 2 ** -code_lenghts[i]


print(f"McMillan sum: {Mc_Millan_sum}")
if  Mc_Millan_sum <= 1:
    print("The code can be decoded obviously.")
else:
    print("The code can not be decoded obviously.")
