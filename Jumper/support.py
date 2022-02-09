import random


class word:


    def __init__(self):
        with open("Jumper/words.txt") as f:
            lines = f.readlines()

            temp_list = []
            for line in lines:
        
                temp_list.append((line.strip("\n")).upper())
        self.words_list = temp_list
        self.word = list(random.choice(self.words_list))


    def formulate_printable_word(self, guessed_letters):
        """ 
        
        Call this into a variable. "variable = formulate_printable_word(guessed_letters)"
        guessed_letters variable should be a list of capital letters that the player has guessed.
        Output example: list, ["E", "X", "_", "M", "P", "_", "E"]
        Args:
            self (word): an instance of word
            guessed_letters (list): A list of the guessed letters so far.
        """

        # print(f"Formulating printable word: {self.word}")


        final_print = []
        for i in self.word:
            if guessed_letters.count(i) > 0:
                final_print.append(i)
            elif guessed_letters.count(i) <= 0:
                final_print.append("_")
            else:
                print("An error occured in checking the guessed letters against the letters in the word. - Support.py->class word->def formulate_printable_word")

        # print(f"Formulated printable word: {final_print}")

        return final_print

    def handle_parachute_damage(self, guessed_letters):
        """
        
        Call this into self.parachute_damage. "self.parachute_damage = handle_parachute_damage(guessed_letters)"
        Checks each letter that has been guessed, and returns how many are not in the word that is supposed to be guessed. 


        Output example: integer, 2
        
        """



# -- OLD SUPPORT.PY --


# import random
# from typing import final

# class word:


#     def __init__(self):
#         with open('Week 5/CSS-210-Team6-Week5/Jumper/words.txt') as f:
#             lines = f.readlines()

#             temp_list = []
#             for line in lines:
        
#                 temp_list.append((line.strip("\n")).upper())
#         self.words_list = temp_list
#         self.word = list(random.choice(self.words_list))


#     def formulate_printable_word(self, guessed_letters):
#         """ 
        
#         Call this into a variable. "variable = formulate_printable_word(guessed_letters)
#         guessed_letters variable should be a list of capital letters that the player has guessed.

#         Output example: list, ["E", "X", "_", "M", "P", "_", "E"]
#         """


#         final_print = []
#         for i in self.word:
#             if guessed_letters.count(i) > 0:
#                 final_print.append(i)
#             elif guessed_letters.count(i) <= 0:
#                 final_print.append("_")
#             else:
#                 print("An error occured in checking the guessed letters against the letters in the word. - Support.py->class word->def formulate_printable_word")

#         return final_print


# class TerminalService():
#     """A service that handles terminal operations
    
#     The responsibility of the TerminalService is to provide input and output operations for the terminal"""
    
#     def __init__(self):
        
#         pass

#     def clear_and_print_screen(self):

#         pass



