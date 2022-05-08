"""
Battal Cevik
Class: CS 521 - Spring Semester
Date: 04/25/2022
CS-521 Project Final Project - World Tour of Trivia

User-defined class. The class must be imported by your main program and have
the following required structures.
− at least 1 private and 2 public self attributes
− at least 1 private and 1 public method that take arguments, return values and are used by your program
− an init() method that takes at least 1 argument
− a repr() method
"""


def player_status_test():
    player_status = "Player Status: Playing"
    return player_status


def player_name_test():
    user_name_test = input("Player Name: ")
    return user_name_test


class Player:
    user_level = []
    # one private class attribute
    __wrong_answer = " "

    def __init__(self, user_name, language, team_name, user_level):
        # self.category = None
        self.user_name = user_name
        self.language = language
        self.team_name = team_name
        self.player_level = user_level

    # Repr method that returns the attributes of organ instance
    def __repr__(self):
        return f'\nPlayer Name: {self.user_name}' \
               f'\nLanguage: {self.language}\nTeam Name: {self.team_name}' \
               f'\nPlayer Level: {self.player_level}\n'.format(self)

    def user_name(self):
        return "{}".format(self.user_name)

    def select_language(self):
        return "{}".format(self.language)

    def select_team_name(self):
        return self.team_name

    def player_level(self):
        return self.player_level

    # one private method
    @staticmethod
    def __display_wrong_answer():
        print("Other users can not see the wrong answers".format(Player.__wrong_answer))

    def display(self):
        self.__display_wrong_answer()

    @classmethod
    def player_name_test(cls):
        pass


user_name = input("Player Name: ")
player_language = input("Language: ")
player_team_name = input("Team Name: ")
player_level = 0
player_obj = Player(user_name, player_language, player_team_name, player_level)
