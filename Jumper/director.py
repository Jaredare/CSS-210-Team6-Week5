class Director():
    """-"""
    
    def __init__(self):
        """Constructs a new Director
        
        Args:
            self (Director): an instance of Director"""
            
        from Jumper.support import word
        from Jumper.terminal_service import TerminalService
        from Jumper.skydiver import Skydiver
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
            self._handle_screen(self.guessed_letters, self.parachute_damage, self.printable_word) # the printable word, the jumper, the already guessed letters, 
            playerGuess = self._get_inputs()   # and an input to guess a letter.
            
            # The player's guess is added to the list of guessed letters and the printable word is returned.
            self.printable_word = self._do_updates(playerGuess)


            # self._do_outputs(self.guessed_letters, self.parachute_damage)
            

    def _get_inputs(self):
        """Asks the player to guess a letter from a-z. 
        
        Args:
            self (Director): An instance of Director.
        """
        playerGuess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        return playerGuess
        

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
        
        self._terminal_service.clear_screen()
        # print("Start of self._in_playing loop")
        # print(f"The word you are trying to guess is: {self._word.word}")   

        # The player receives a pop up with:
        self._terminal_service.print_printable_word(printable_word)    # the printable word,
        print(self._jumper.display_jumper_graphic(parachute_damage))   # the jumper, 
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