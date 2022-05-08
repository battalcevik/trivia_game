"""
Battal Cevik
Class: CS 521 - Spring Semester
Date: 04/25/2022
CS-521 Project Final Project - World Tour of Trivia

"""
from Player import player_obj, Player
from get_questions_answers import get_questions


# Create a function to check if the answer is correct or not
def check_answer(user_guess, answer):
    if user_guess == answer:
        correct_answer = "Correct Answer"
        print(correct_answer)
        return 1
    else:
        wrong_answer = "Wrong Answer"
        print(wrong_answer)
        return 0


# Create a function to show score result at the end of the game
def score_result(self, user_guesses):
    print("\nTrivia Game Results: ")
    print("\nCorrect Answers of Game: ", end="")
    for each_question in get_questions():
        print(get_questions().get(each_question), end="")

    print("\n------------------------------------")
    print("\n---User Answers of Game: ", end="")
    for each_question in user_guesses:
        print(each_question, end="")

    user_score = int((self / len(get_questions())) * 100)
    player_obj2 = Player.user_name(player_obj)
    player_obj3 = Player.select_language(player_obj)
    player_obj4 = Player.select_team_name(player_obj)
    player_obj5 = Player.player_level(player_obj)
    print("\n-------------------------------------")
    print("\nPlayer name is:", player_obj2)
    print("Player language is:", player_obj3)
    print("Player team name is:", player_obj4)
    print("Player level:", player_obj5)
    print("{}, your score is: ".format(player_obj2) + str(user_score))
    if user_score >= 70:
        player_obj5 += 1
        print("Player new level:", player_obj5)
