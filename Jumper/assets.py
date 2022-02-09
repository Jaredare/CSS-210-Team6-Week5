class JumperGraphic():
    
   
    def display_jumper_graphic(self, parachute_damage):
        """Contains the jumper graphics of losing the parachute, 0 being undamaged and 4 being a fail state. """
        if parachute_damage == 0:
            # Unharmed parachute [0]
            parachute_graphic = "  ___  \n /___\ \n \   / \n  \ /  \n   O   \n  /|\  \n  / \  \n\n^^^^^^^"
        elif parachute_damage == 1:
            # [1]
            parachute_graphic = "       \n /___\ \n \   / \n  \ /  \n   O   \n  /|\  \n  / \  \n\n^^^^^^^"
        elif parachute_damage == 2:
            # [2]
            parachute_graphic = "       \n       \n \   / \n  \ /  \n   O   \n  /|\  \n  / \  \n\n^^^^^^^"
        elif parachute_damage == 3:
            # [3]
            parachute_graphic = "       \n       \n       \n  \ /  \n   O   \n  /|\  \n  / \  \n\n^^^^^^^"
        elif parachute_damage == 4:
            # Fail state [4]
            parachute_graphic = "       \n       \n       \n       \n   x   \n  /|\  \n  / \  \n\n^^^^^^^"
        else:
            parachute_graphic = "Something bad happened, you went past our failure state. \nI guess your jumper is dead. :("
        return parachute_graphic






# ----- OLD ASSETS.PY -----

# from Jumper.support import word
# from Jumper.terminal_service import TerminalService

# class JumperGraphic():
    
   
#     def display_jumper_graphic(self, parachute_damage):
#         """Contains the jumper graphics of losing the parachute, 0 being undamaged and 4 being a fail state. """
#         if parachute_damage == 0:
#             # Unharmed parachute [0]
#             parachute_graphic = "  ___  \n /___\ \n \   / \n  \ /  \n   0   \n  /|\  \n  / \  \n\n^^^^^^^"
#         elif parachute_damage == 1:
#             # [1]
#             parachute_graphic = "       \n /___\ \n \   / \n  \ /  \n   0   \n  /|\  \n  / \  \n\n^^^^^^^"
#         elif parachute_damage == 2:
#             # [2]
#             parachute_graphic = "       \n       \n \   / \n  \ /  \n   0   \n  /|\  \n  / \  \n\n^^^^^^^"
#         elif parachute_damage == 3:
#             # [3]
#             parachute_graphic = "       \n       \n       \n  \ /  \n   0   \n  /|\  \n  / \  \n\n^^^^^^^"
#         elif parachute_damage == 4:
#             # Fail state [4]
#             parachute_graphic = "       \n       \n       \n       \n   x   \n  /|\  \n  / \  \n\n^^^^^^^"
#         return parachute_graphic



    
    