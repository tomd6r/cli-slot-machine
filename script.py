from player import Player
from slotmachine import SlotMachine


class Game:
    playing = False

    def __init__(self):
        print("Welcome to the casino!")

    def start_game(self):
        self.playing = True
        self.slot_machine = SlotMachine()

        name = input("What is your name? ")
        self.player = Player(name)
        bet = input(
            "Hi {}, how much do you want to bet per spin? ".format(self.player.name))
        self.player.bet = int(bet)

        while self.playing and self.player.budget > 0:
            move = input(
                "Do you want to (p)lay, see your (b)udget or (c)ash out? ")

            if move == 'b':
                print("Your current budget is {}.".format(self.player.budget))
                continue

            if move == 'c':
                print("Thank you for playing, you won {}!".format(
                    self.player.budget))
                self.playing = False
                continue

            if move == 'p':
                self.player.budget -= self.player.bet
                row = self.slot_machine.spin()
                print([face[1] for face in row])
                self.player.budget += self.slot_machine.payout(
                    row, self.player.bet)
                continue

            print(
                "That option was not recognized. Do you want to (p)lay, see your (b)udget or (c)ash out? ")

        if self.player.budget <= 0:
            print("You're out of money!")
            self.playing = False


game = Game()
game.start_game()
