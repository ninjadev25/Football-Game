
players = {}

class Person:
    """Constructor"""
    def __init__(self, name):
        self.name = name



    def main_menu(self):
        #menu
        print("""
        \t ---Create a player:1
        \t ---Remove a player:2
        \t ---Quit game:3

        """)

        print("Hint: You can quit the game from the main menu by pressing 3:")
        menu_option = input("Enter 1 to a create player: Enter 2 to remove a player:_")

        if menu_option == "1":
            create()

        elif menu_option == "2":
            remove()

        elif menu_option == "3":
            end()





    def create_player(self):
        #Create player:
        count = int(input("Enter how many players you would like to create: "))
        for i in range(count):
            player_name = input("Enter Player's name:")
            player_score = input("Enter Player's score:")
            print("Player Score Board")
            print("....................")
            players[player_name] = player_score
            print('Scoreboard')
            for name, score in players.items():
                print('Name:{}|Score:{}'.format(name, score))


        #Delete_player
    def Delete_player(self):

        remove_player = players.pop(input("Enter name of player you wish to delete: "))
        print('Scoreboard')
        for name, score in players.items():
            print('Name:{}|Score:{}'.format(name, score))



    def End_game(self):
        print("The game has ended")
        exit()




def main():
        """Entrypoint."""
        person_a = Person("")
        person_a.main_menu()



def create():
    person_a = Person("")
    person_a.create_player()


def remove():
    person_a = Person("")
    person_a.Delete_player()



def end():
    person_a = Person("")
    person_a.End_game()

#Greet user
print("Hello and welcome to football for fools.")
print("Please choose from the following below options:")



i = 1
while i < 22:
    main()
