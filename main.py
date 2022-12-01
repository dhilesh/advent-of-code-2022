from functions import *
 
if __name__ == "__main__":

    # Day 1
    day1_pt1_answer = top_n_elf_calories( total_calories_per_elf('puzzle-inputs/elf-calories.txt'), 1 )
    day1_pt2_answer = sum( top_n_elf_calories( total_calories_per_elf('puzzle-inputs/elf-calories.txt'), 3 ) )
    print(f'Day 1 Part 1 \nThe Elf with the most calories is: {day1_pt1_answer}')
    print(f'Day 1 Part 2 \nThe Elves with the most calories have {day1_pt2_answer} calories in total')