class Director():
    """-"""
    
    def __init__(self):
        """Constructs a new Director and populates variables.
        
        Args:
            self (Director): an instance of Director"""
            
        from Jumper.support import word
        from Jumper.terminal_service import TerminalService
        # from Jumper.skydiver import Skydiver
        from Jumper.assets import JumperGraphic


        self._jumper = JumperGraphic()
        self._word = word()
        self._terminal_service = TerminalService()

        self._is_playing = True

        self.parachute_damage = 0
        self.guessed_letters = []
        self.printable_word = self._word.formulate_printable_word(self.guessed_letters)
        
        
    def start_game(self):
        """Starts the game by running the main loop.
        
        Args:
            self (Director): an instance of Director.
        """
        
        while self._is_playing:
            # Needed steps:
            # The player receives a pop up with:
            self._handle_screen(self.guessed_letters, self.parachute_damage, self.printable_word) # the jumper, the printable word, the already guessed letters, 
            playerGuess = self._get_inputs()   # and an input to guess a letter.
            
            # The player's guess is added to the list of guessed letters and the printable word is returned.
            self.printable_word = self._do_updates(playerGuess)


            # self._do_outputs(self.guessed_letters, self.parachute_damage)
            

    def _get_inputs(self):
        """Asks the player to guess a letter from a-z and validates it.
        
        Args:
            self (Director): An instance of Director.
        """
        get_input_loop = True
        while get_input_loop:
            # playerGuess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
            playerGuess = input(f"Guess a letter [a-z]: ")
            if playerGuess.isalpha() and len(playerGuess) == 1 and self.guessed_letters.count(playerGuess.upper()) < 1:
                get_input_loop = False
            elif playerGuess.isalpha() and len(playerGuess) == 1 and self.guessed_letters.count(playerGuess.upper()) >= 1:
                print("You already guessed that letter, please try a different letter.")
            elif playerGuess.isalpha() and len(playerGuess) > 1 and self.guessed_letters.count(playerGuess.upper()) < 1:
                print("Sorry, that was more than one character. Please input one letter.")
            elif not playerGuess.isalpha() and len(playerGuess) > 1:
                print("Wow, that was both too many characters *and* wasn't alphabetical. Please put just one letter.")
            else:
                print("Sorry, that wasn an invalid character. Please try a letter.")
            

        return playerGuess.upper()
        

    def _do_updates(self, playerGuess):
        """Puts the guessed letters in a list.
        Calls the formulate_printable_word to check the guessed letters against the letters in the word.
        
        Args: 
            self (Director): An instance of Director.
        """
        # guessedLetters = list(playerGuess.upper())
        self.guessed_letters.append(playerGuess.upper())
        return self._word.formulate_printable_word(self.guessed_letters)
        

    def _handle_screen(self, guessed_letters, parachute_damage, printable_word):
        """Displays the jumper, word, and already guessed letters after clearing the screen.

        Args:
            self (Director): An instance of Director.
            guessed_letters: list, a list of what letters have been guessed
            parachute_damage: int, a number 0-4 to represent how close you are to failing.
            printable_word: list, the word you're trying to guess with _s instead of any letters you haven't guessed.        
        """
        
        self._terminal_service.clear_lines(100)
        # print("Start of self._in_playing loop")
        # print(f"The word you are trying to guess is: {self._word.word}")   

        # The player receives a pop up with:
        print(self._jumper.display_jumper_graphic(parachute_damage))   # the jumper, 
        self._terminal_service.print_printable_word(printable_word)    # the printable word,
        self._terminal_service.print_guessed_letters(guessed_letters)  # the already guessed letters, 

    
    # def _do_outputs(self, guessed_letters, parachute_damage):
    #     """Displays jumper graphic, and a bank of guessed letters. """
    #     print()
    #     print(f"parachute_damage = {parachute_damage}\nPrinting Jumper:")
    #     self._jumper.display_jumper_graphic(parachute_damage)
    #     print(f"Printing guessed letters:")
    #     self._terminal_service.print_guessed_letters(guessed_letters)
    #     print()




# ---- OLD DIRECTOR.PY ----


# from Jumper.assets import JumperGraphic
# from Jumper.terminal_service import TerminalService
# from Jumper.support import word

# class Director():
#     """-"""
    
#     def __init__(self):
#         """Constructs a new Director
        
#         Args:
#             self (Director): an instance of Director"""
            
#         self._jumper = JumperGraphic()
#         self._is_playing = True
#         self._word = word()
#         self._terminal_service = TerminalService()
        
        
#     def start_game(self):
#         """Starts the game by running the main loop.
        
#         Args:
#             self (Director): an instance of Director.
#         """
        
#         while self._is_playing:
#             playerGuess = self._get_inputs()
#             GuessedLetters = self._do_updates(playerGuess)
#             self._do_outputs()
            
#     def _get_inputs(self):
#         """Asks the player to guess a letter from a-z. 
        
#         Args:
#             self (Director): An instance of Director.
#         """
#         playerGuess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
#         return playerGuess
        
#     def _do_updates(self, playerGuess):
#         """Puts the guessed letters in a list.
#         Calls the formulate_printable_word to check the guessed letters against the letters in the word.
        
#         Args: 
#             self (Director): An instance of Director.
#         """
#         guessedLetters = list(playerGuess.upper())
#         return self._word.formulate_printable_word(guessedLetters)
        
    
#     def _do_outputs(self, guessed_letters, parachute_damage = 0):
#         """Displays jumper graphic, and a bank of guessed letters. """
#         self._jumper.display_jumper_graphic(parachute_damage)