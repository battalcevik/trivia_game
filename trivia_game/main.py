"""
Battal Cevik
Class: CS 521 - Spring Semester
Date: 04/25/2022
CS-521 Project Final Project - World Tour of Trivia

"""

from game_results import check_answer, score_result
from get_questions_answers import get_questions, get_answers, en_questions, en_answers, fr_questions, fr_answers, \
    gr_questions, gr_answers, tr_questions, tr_answers
from Player import player_language, Player, player_obj, player_team_name, player_status_test, user_name

questions_function = ''
answers = ''

if player_language == "English":
    questions_function = en_questions()
    answers = en_answers()

elif player_language == "French":
    questions_function = fr_questions()
    answers = fr_answers()
elif player_language == "German":
    questions_function = gr_questions()
    answers = gr_answers()
elif player_language == "Turkish":
    questions_function = tr_questions()
    answers = tr_answers()
else:
    questions_function = get_questions()
    answers = get_answers()


def trivia_game():
    number_of_questions = 1
    user_guesses = []
    right_answers = 0
    print("====Trivia Game Start====")
    for each_question in questions_function:
        print("\n", each_question)
        for answer in answers[number_of_questions - 1]:
            print("    ", answer)
        select_choices = input("Please select from choices: (A, B, C or D): ")
        select_choices = select_choices.upper()
        user_guesses.append(select_choices)
        right_answers += check_answer(questions_function.get(each_question), select_choices)
        number_of_questions += 1

    score_result(right_answers, user_guesses)
    player_level = 0
    player_object = Player(user_name, player_language, player_team_name, player_level)
    print(player_object)


def play_again():
    user_input = input("Would you like to play again? yes or no:")
    user_input = user_input.lower()
    if user_input == 'yes':
        print(player_status_test())
        return True
    else:
        return False


# Create Unit Tests for the game
def unit_test():
    # Print Player object -
    print("======================================")
    print("==============UNIT TEST===============")
    print("======================================")
    print("Unit Test ", player_obj)
    player_level = 0
    player_object = Player(user_name, player_language, player_team_name, player_level)
    print(player_object)
    assert player_status_test() == player_status_test()
    assert Player.player_name_test() == player_object.player_name_test()


# # Main function
def main():
    pass


# Include a unit test in an if __name__ block to test the class.
if __name__ == '__main__':
    trivia_game()
    while play_again():
        trivia_game()
    print("\nThe Trivia game has ended.")
    main()
    unit_test()
