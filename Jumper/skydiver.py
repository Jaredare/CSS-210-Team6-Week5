class Skydiver:

    def __init__(self):

          
        cartoons = self.__create_cartoon()
 
        while self.__is_a_draw(cartoons):
            self.__display_cartoon(cartoons)
            self.__make_move(cartoons)
        
        self.__display_cartoon(cartoons)
        print("You have no more parachute the game is over!")
        print() 

    def __create_cartoon(self):
        cartoon = [" ___", "/", "___", "\ ", "\ ", "/ ", "\ ", "/ ", "O", "/", "|", "\ ", "/", "\ ", "^^^^^^^"]
    
        return cartoon

    def __display_cartoon(self, cartoon):
        print()
        print(f" {cartoon[0]}")
        print(f" {cartoon[1]}{cartoon[2]}{cartoon[3]}")
        print(f" {cartoon[4]}  {cartoon[5]}")
        print(f"  {cartoon[6]}{cartoon[7]}")
        print(f"   {cartoon[8]}")
        print(f"  {cartoon[9]}{cartoon[10]}{cartoon[11]}")
        print(f"  {cartoon[12]} {cartoon[13]}")
        print()
        print(f"{cartoon[14]}")
        print()
        
    def __is_a_draw(self, cartoon):
        
        if cartoon[8] == "x" :
            return False
        return True 

    # 
    def __make_move(self, cartoon):
        
        puzzle = int(input("provisional entry puzzle (1-9): "))
        
        if puzzle == 1:
            cartoon[0] = "    "
        elif puzzle == 2:
            cartoon[1] = " "
        elif puzzle == 3:
            cartoon[2] = "   "
        elif puzzle == 4:
            cartoon[3] = "  "
        elif puzzle == 5:
            cartoon[4] = "  "
        elif puzzle == 6:
            cartoon[5] = "  "
        elif puzzle == 7:
            cartoon[6] = "  "
        elif puzzle == 8:
            cartoon[7] = "  "
        elif puzzle == 9:
            cartoon[8] = "x"
        else:
            pass

