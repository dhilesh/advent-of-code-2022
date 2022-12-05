from functions import *
 
if __name__ == "__main__":

    # Day 1
    # day1_pt1_answer = top_n_elf_calories( total_calories_per_elf('puzzle-inputs/elf-calories.txt'), 1 )
    # day1_pt2_answer = sum( top_n_elf_calories( total_calories_per_elf('puzzle-inputs/elf-calories.txt'), 3 ) )
    # print(f'Day 1 Part 1 \nThe Elf with the most calories is: {day1_pt1_answer[0]}')
    # print(f'Day 1 Part 2 \nThe Elves with the most calories have {day1_pt2_answer} calories in total')

    # Day 2
    # print('\n---------------\n')
    # day2_pt1_answer = rock_paper_scissors_score('puzzle-inputs/strategy-guide.txt',1)
    # day2_pt2_answer = rock_paper_scissors_score('puzzle-inputs/strategy-guide.txt',2)
    # print(f'Day 2 Part 1 \n The score with the first strategy is {day2_pt1_answer}')
    # print(f'Day 2 Part 2 \n The score with the second strategy is {day2_pt2_answer}')

    # Day 3
    # print('\n---------------\n')
    # day3_pt1_answer = rucksack_priority('puzzle-inputs/rucksacks.txt')
    # day3_pt2_answer = common_badge_priority('puzzle-inputs/rucksacks.txt')
    # print(f'Day 3 Part 1 \n The sum of priorities for the misplaced items is {day3_pt1_answer}')
    # print(f'Day 3 Part 2 \n The sum of priotities for the common badges is {day3_pt2_answer}')
    
    # Day 4
    print('\n---------------\n')
    day4_pt1_answer = find_redudant_cleaning_pairs('puzzle-inputs/cleanup-pairs.txt',1)
    day4_pt2_answer = find_redudant_cleaning_pairs('puzzle-inputs/cleanup-pairs.txt',2)
    print(f'Day 4 Part 1 \n The sum of fully overlapping sections is {day4_pt1_answer}')
    print(f'Day 4 Part 2 \n The sum of fully and partially overlapping sections is {day4_pt2_answer}')