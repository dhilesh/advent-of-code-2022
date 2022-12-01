def read_input(filename):
    with open(filename,'r') as f:
        data = f.readlines()
    return data

def total_calories_per_elf(filename):
    data = read_input(filename)
    individual_elf = ''.join(data).split('\n\n')
    elf_split = [x.split('\n') for x in individual_elf]
    elf_sums  = []
    for elf in elf_split:
        elf_sum = 0
        for item in elf:
            elf_sum += int(item)
        elf_sums.append(elf_sum)

    return elf_sums

def top_n_elf_calories(elf_sums, n):
    return sorted(elf_sums, reverse=True)[:n]