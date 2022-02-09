from Jumper.assets import JumperGraphic
from Jumper.terminal_service import TerminalService
from Jumper.support import word

class Director():
    """-"""
    
    def __init__(self):
        """Constructs a new Director
        
        Args:
            self (Director): an instance of Director"""
            
        self._jumper = JumperGraphic()
        self._is_playing = True
        self._word = word()
        self._terminal_service = TerminalService()
        
        
    def start_game(self):
        """Starts the game by running the main loop.
        
        Args:
            self (Director): an instance of Director.
        """
        
        while self._is_playing:
            playerGuess = self._get_inputs()
            GuessedLetters = self._do_updates(playerGuess)
            self._do_outputs()
            
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
        guessedLetters = list(playerGuess.upper())
        return self._word.formulate_printable_word(guessedLetters)
        
    
    def _do_outputs(self, guessed_letters, parachute_damage = 0):
        """Displays jumper graphic, and a bank of guessed letters. """
        self._jumper.display_jumper_graphic(parachute_damage)