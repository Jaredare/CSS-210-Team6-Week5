import sys
class TerminalService():
    """A service that handles terminal operations
    
    The responsibility of the TerminalService is to provide any needed input and output operations for the terminal"""
    
    def __init__(self):
        """Constructs a new TerminalService
        
        Args:
            self (Director): an instance of Director"""
        pass


    # def read_text(self, prompt):
    #     return input(prompt)

    # def write_text(self, text):
    #     print(text)
        

    def clear_lines(self, lines):
        """Clears as many lines from the terminal as you want.
        
        Args:
            self (TerminalService): an instance of TerminalService
            lines: integer, how many lines you want cleared.
        """
        
        for _ in range(lines):
            # Deletes the last "height" lines

            # Cursor up 1 line
            sys.stdout.write(f'\x1b[1A')
            # Delete last line
            sys.stdout.write(f'\x1b[2K')


    def print_printable_word(self, printable_word):
        """Prints the word the player will see.
        
        Args:
            self (TerminalService): an instance of TerminalService
            printable_word: list, a list of the letters and underscores that make up the word the viewer will see.
        """
        print("Word:", end="")
        for i in printable_word:
            print(" ", i, end="")
        print()


    def print_guessed_letters(self, guessed_letters):
        """Prints the word the player will see.
        
        Args:
            self (TerminalService): an instance of TerminalService
            printable_word: list, a list of the letters the player has guessed.
        """
        if len(guessed_letters) < 1:
            pass

        elif len(guessed_letters) == 1:
            print(f"Guessed letter: {guessed_letters[0]}")

        elif len(guessed_letters) > 1:
            
            guessed_letters.sort()
            # print(guessed_letters)
            print("Guessed letters: ", end="")
            for i in guessed_letters:
                print(i, ", ", end="")
            print()

        else:
            print("terminal_service.py -> TerminalService -> print_guessed_letters has failed to find a length of guessed_letters")






# -- OLD TERMINAL_SERVICE.PY -- 

# class TerminalService():
#     """A service that handles terminal operations
    
#     The responsibility of the TerminalService is to provide input and output operations for the terminal"""
    
#     def read_text(self, prompt):
#         return input(prompt)

#     def write_text(self, text):
#         print(text)