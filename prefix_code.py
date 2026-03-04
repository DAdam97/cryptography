input = [ "010", "10", "1111", "100", "101", "110", "111", "1010" ]

code_lengths = sorted([len(l) for l in input])

Mc_Millan_sum = 0

for l in code_lengths:
    Mc_Millan_sum += 2 ** -l

print(f"McMillan sum: {Mc_Millan_sum}")

if  Mc_Millan_sum > 1:
    print("The code can not be decoded obviously.")
    exit()

q_values = [0.0] * len(code_lengths)
prefix_codes = []

for i in range(len(code_lengths)):
    if i > 0:
        q_values[i] = q_values[i - 1] + (2 ** -code_lengths[i - 1])

    l_i = code_lengths[i]
    q_i = q_values[i]

    shifted_val = int(q_i * (2 ** l_i))

    binary_val = format(shifted_val, f'0{l_i}b')
    prefix_codes.append(binary_val)

print(prefix_codes)
