# Trivia Game Project
This is a simple Python trivia project that uses only core Python modules. 

# How It Works?
    main.py file is the main file to run Trivia Game 
    player_class.py file has Player class, private and public class attributes, init() and repr() methods 
    
    Get input from user for below instance variable
        Player Name
        Language
        Team Name 
        Category
    Get the questions and answers from a file for different languages

      1. Trivia Game English text file (trivia_game_en) and (trivia_game_en_answer)
      2. Trivia Game French text file (trivia_game_fr) and (trivia_game_fr_answer)
      3. Trivia Game German text file (trivia_game_gr) and (trivia_game_gr_answer)
      4. Trivia Game Turkish text file (trivia_game_tr) and (trivia_game_tr_answer) 
      5. Trivia Game default question and answer data text file

   
# Read questions file 
    get_questions_answers.py has functions to select and read 
    Using File Read function, all questions file will be read based on player language and category selection
# Read answer file 
    Using File Read function, all anwers file will be read based on the language selection

    Convert questions and answers to the collections
        Convert questions into Python dictionary 
        Convert answers into Python lists
    Set Player score to 0 
        Set Player score to 0 so that each question will be added to player score

# Create check answer function and a result function
    game_results.py file has check_answer() and score_result() functions.
    It will check if this user choice is correct or wrong
    It will update the score based on selection
    It will show final score, player name, player team name and language


# Create a for loop to read key and value from collections 
    Create a main.py file which includes if statements for language and category selection,
    trivia_game() function to iterate through all questions and answers and get score results 
    play_again() function if player would like to test again
    unit_test() to test all existing codes variables and classes works as expected 
    Include an if __name__ block to test the class and run all function under main.

# How to run test 
    1. Go to main.py file and the file
    2. Follow instuctions 
    3. Enter Player Name, Language, Team Name
    4. There is also one feature which is country category. 
    5. If user selects they will only receive questions from countries 
    6. Do not select category and click enter 
    7. The trivia game will start and select answers from multipe choices
    8. Player will see score at the end of the game