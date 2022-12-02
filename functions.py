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

def rock_paper_scissors_score(file, question_part):
    choice_score = {"X":1,"Y":2,"Z":3}
    outcome_dict = {"A X":3, "A Y":6, "A Z":0, "B X":0, "B Y":3, "B Z":6, "C X":6, "C Y":0, "C Z":3}
    decision_dict = {"A":{"X":"Z", "Y":"X", "Z":"Y"}, "B":{"X":"X", "Y":"Y", "Z":"Z"}, "C":{"X":"Y", "Y":"Z", "Z":"X"},}
    score = 0
    for line in read_input(file):
        if question_part == 1:
            my_choice = line[2]
            score += choice_score[my_choice] + outcome_dict[line.strip()]
        else:
            opp_choice, result = line[0], line[2]
            my_decision = decision_dict[opp_choice][result]
            score += choice_score[my_decision] + outcome_dict[ f'{opp_choice} {my_decision}' ]
    return score