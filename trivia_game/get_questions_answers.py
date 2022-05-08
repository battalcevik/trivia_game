"""
Battal Cevik
Class: CS 521 - Spring Semester
Date: 04/25/2022
CS-521 Project Final Project - World Tour of Trivia

"""
import sys


# Get questions from text file to receive dynamic file for anytime
def get_questions():
    questions = {}
    try:
        question_file = open("question_data")
        for line in question_file:
            # Split line into a tuple
            key, value = line.strip().split(":")
            # Add tuple values to dictionary
            questions[key] = value
        question_file.close()
        return questions
    except FileNotFoundError as e:
        sys.exit("Error: This file does not exist: ", e)
    except IOError as e:
        sys.exit("Error: This file does not found: ", e)


# Get answers from text file to receive dynamic file for anytime
def get_answers():
    answers = []
    try:
        answer_file = open("answer_data")
        for a_line in answer_file:
            answer = a_line.strip().split('!')
            answers.append(answer)
            # print(answer)
        answer_file.close()
        return answers
    except FileNotFoundError as e:
        sys.exit("Error: This file does not exist: ", e)
    except IOError as e:
        sys.exit("Error: This file does not found: ", e)


def en_questions():
    questions = {}
    try:
        question_file = open("trivia_game_en")
        for line in question_file:
            # Split line into a tuple
            key, value = line.strip().split(":")
            # Add tuple values to dictionary
            questions[key] = value
        question_file.close()
        return questions
    except FileNotFoundError as e:
        sys.exit("Error: This file does not exist: ", e)
    except IOError as e:
        sys.exit("Error: This file does not found: ", e)


# Get answers from text file to receive dynamic file for anytime
def en_answers():
    answers = []
    try:
        answer_file = open("trivia_game_en_answer")
        for a_line in answer_file:
            answer = a_line.strip().split('!')
            answers.append(answer)
        answer_file.close()
        return answers
    except FileNotFoundError as e:
        sys.exit("Error: This file does not exist: ", e)
    except IOError as e:
        sys.exit("Error: This file does not found: ", e)


def fr_questions():
    questions = {}
    try:
        question_file = open("trivia_game_fr")
        for line in question_file:
            # Split line into a tuple
            key, value = line.strip().split(":")
            # Add tuple values to dictionary
            questions[key] = value
        question_file.close()
        return questions
    except FileNotFoundError as e:
        sys.exit("Error: This file does not exist: ", e)
    except IOError as e:
        sys.exit("Error: This file does not found: ", e)


# Get answers from text file to receive dynamic file for anytime
def fr_answers():
    answers = []
    try:
        answer_file = open("trivia_game_fr_answer")
        for a_line in answer_file:
            answer = a_line.strip().split('!')
            answers.append(answer)
        answer_file.close()
        return answers
    except FileNotFoundError as e:
        sys.exit("Error: This file does not exist: ", e)
    except IOError as e:
        sys.exit("Error: This file does n ot found: ", e)


def gr_questions():
    questions = {}
    try:
        question_file = open("trivia_game_gr")
        for line in question_file:
            # Split line into a tuple
            key, value = line.strip().split(":")
            # Add tuple values to dictionary
            questions[key] = value
        question_file.close()
        return questions
    except FileNotFoundError as e:
        sys.exit("Error: This file does not exist: ", e)
    except IOError as e:
        sys.exit("Error: This file does n ot found: ", e)


# Get answers from text file to receive dynamic file for anytime
def gr_answers():
    answers = []
    try:
        answer_file = open("trivia_game_gr_answer")
        for a_line in answer_file:
            answer = a_line.strip().split('!')
            answers.append(answer)
        answer_file.close()
        return answers
    except FileNotFoundError as e:
        sys.exit("Error: This file does not exist: ", e)
    except IOError as e:
        sys.exit("Error: This file does n ot found: ", e)


def tr_questions():
    questions = {}
    try:
        question_file = open("trivia_game_tr")
        for line in question_file:
            # Split line into a tuple
            key, value = line.strip().split(":")
            # Add tuple values to dictionary
            questions[key] = value
        question_file.close()
        return questions
    except FileNotFoundError as e:
        sys.exit("Error: This file does not exist: ", e)
    except IOError as e:
        sys.exit("Error: This file does n ot found: ", e)


# Get answers from text file to receive dynamic file for anytime
def tr_answers():
    answers = []
    try:
        answer_file = open("trivia_game_tr_answer")
        for a_line in answer_file:
            answer = a_line.strip().split('!')
            answers.append(answer)
        answer_file.close()
        return answers
    except FileNotFoundError as e:
        sys.exit("Error: This file does not exist: ", e)
    except IOError as e:
        sys.exit("Error: This file does n ot found: ", e)


def country_questions():
    questions = {}
    try:
        question_file = open("trivia_game_country")
        for line in question_file:
            # Split line into a tuple
            key, value = line.strip().split(":")
            # Add tuple values to dictionary
            questions[key] = value
        question_file.close()
        return questions
    except FileNotFoundError as e:
        sys.exit("Error: This file does not exist: ", e)
    except IOError as e:
        sys.exit("Error: This file does n ot found: ", e)


def country_answers():
    answers = []
    try:
        answer_file = open("trivia_game_country_answer")
        for a_line in answer_file:
            answer = a_line.strip().split('!')
            answers.append(answer)
        answer_file.close()
        return answers
    except FileNotFoundError as e:
        sys.exit("Error: This file does not exist: ", e)
    except IOError as e:
        sys.exit("Error: This file does n ot found: ", e)
