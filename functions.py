import json
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

def rucksack_priority(file):
    base_letters = 'abcdefghijklmnopqrstuvwxyz'
    all_letters = base_letters + base_letters.upper()
    all_numbers = [x for x in range(1,53)]
    sum_priority = 0

    for line in read_input(file):        
        line = line.strip()
        halfway_index = int((len(line)/2))
        compartment1, compartment2 = line[:halfway_index], line[halfway_index:]
        intersect_letter = list(set(compartment1).intersection(set(compartment2)))[0]
        sum_priority += all_numbers[all_letters.find(intersect_letter)]
        
    return sum_priority

def common_badge_priority(file):
    base_letters = 'abcdefghijklmnopqrstuvwxyz'
    all_letters = base_letters + base_letters.upper()
    all_numbers = [x for x in range(1,53)]
    sum_priority = 0
    rucksacks = []

    for line in read_input(file):
        rucksacks.append(set(line.strip()))
        if len(rucksacks) == 3:
            intersect_letter = list(rucksacks[0].intersection(rucksacks[1]).intersection(rucksacks[2]))[0]
            sum_priority += all_numbers[all_letters.find(intersect_letter)]
            rucksacks = [] # reset
    return sum_priority

def find_redudant_cleaning_pairs(file, question_part):
    redundant_count = 0
    for line in read_input(file):
        line = line.strip()
        elf1_section, elf2_section = line.split(',')[0], line.split(',')[1]       
        elf1_min, elf1_max = int(elf1_section.split('-')[0]), int(elf1_section.split('-')[1])
        elf2_min, elf2_max = int(elf2_section.split('-')[0]), int(elf2_section.split('-')[1])
        if question_part==1:
            if ((elf1_min <= elf2_min and elf1_max >= elf2_max) or (elf2_min <= elf1_min and elf2_max >= elf1_max)):
                redundant_count += 1
        else:
            if len(list(set([x for x in range(elf1_min,elf1_max+1)]).intersection(set([x for x in range(elf2_min,elf2_max+1)])))) > 0:
                redundant_count += 1

    return redundant_count 

def find_crates_on_top(file, crate_model):
    start_state = {
        '1': ['H','R','B','D','Z','F','L','S'],
        '2': ['T','B','M','Z','R'],
        '3': ['Z','L','C','H','N','S'],
        '4': ['S','C','F','J'],
        '5': ['P','G','H','W','R','Z','B'],
        '6': ['V','J','Z','G','D','N','M','T'],
        '7': ['G','L','N','W','F','S','P','Q'],
        '8': ['M','Z','R'],
        '9': ['M','C','L','G','V','R','T'],
    }

    for line in read_input(file)[10:]:
        items = line.split(' ')
        num_to_move = items[1].strip()
        from_move = items[3].strip()
        to_move = items[5].strip()

        if crate_model == '3000':
            for i in range(0, int(num_to_move)):
                start_state[to_move].append( start_state[from_move].pop() )
        else:
            for i in start_state[from_move][-int(num_to_move):]:
                start_state[to_move].append( i )
            start_state[from_move] = start_state[from_move][:-int(num_to_move)]
    
    top_letters = ''
    for v in start_state.values():
        top_letters += v.pop()
    
    return top_letters

def packet_marker(file, num_distinct_chars=0):
    datastream = read_input(file)[0]
    for i in range(num_distinct_chars,len(datastream)):
        window = datastream[i-num_distinct_chars:i]
        if len(set(window)) == num_distinct_chars:
            return i

def create_filesystem(file):
    filesystem = {}
    prev_dir = ''
    curr_dir = ''
    list_mode, cd_mode = False, False
    for line in read_input(file)[1:]:
        parts = line.strip().split(' ')

        # if cd and dir name 
        if parts[1] == 'cd' and parts[2] != '..':
            curr_dir += parts[2] + '/' # keep track of current dir
            print('curr dir is:', curr_dir)
            continue

        # if cd and not dir name 
        if parts[1] == 'cd' and parts[2] == '..':
            curr_dir = '/'.join(curr_dir.split('/')[:-2]) # remove folder from curr dir
            print('new curr dir is', curr_dir)

        # if list function
        if parts[1] == 'ls': # skip line
            continue

        # deal with output from list function
        if parts[0] == 'dir':
            filesystem[parts[1]] = {} # create a new dir
            prev_dir = parts[1] # keep track of prev dir
        else:
            filesystem[prev_dir][parts[1]] = parts[0] # append file to dir
    
    print(json.dumps(filesystem, indent=3))
    # NEW APPROACH SHOULD BE TO KEEP A STRING OF EACH FILENAME AND THE SUBFOLDER
    # JUST LIKE YOU HAVE IN BLOB STORAGE
    # CAN MAKE USE OF THE CURR DIR TRACKING TO PREPEND TO THE FLIENAME
    # MAKES SENSE CAUSE WE ONLY CARE ABOUT THE FOLDERS WITH FILES IN THEM, NOT THE EMPTY ONES