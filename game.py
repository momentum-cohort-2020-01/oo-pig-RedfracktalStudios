from random import randint
# count to 100 is needed
# passes from computer to player is needed


class Pig:
    def __init__(self):
        self.computer = Computer  # this will be a class
        self.player = Player  # this will be a class
        self.die = Die  # this will be a class


class Die:
    def __inti__(self):
        self.value = randint(1, 6)

    def __str__(self):
        return f"{self.value}"


class Player():
    def __init__(self, name):
        self.name = name
        self.turn = 0
        self.score = 0

    def __str__(self):
        return f"{self.name}"

    def turn(self):
        choice = input("Would you like to roll? Yes (y) or No (n)")
        while choice != "n":
            roll = Die(). value
            print(f"You rolled: {roll}")
        if roll != 1:
            self.turn += roll
            print(f"Total score is: {self.score}")
        while self.score < 100:
            choice = input("Would you like to roll? Yes (y) or No (n)")
            while choice != "n":
                roll = Die(). value
                print(f"You rolled: {roll}")


class Computer:
    def __init__(self, name):
        self.name = name
        self.turn = 0
        self.score = 0

    def __str__(self):
        return f"{self.name}"

    def round(self):
        if self.turn < 20:
            roll = Die().value
            print(f"Computer rolls: {roll}")
            while roll != 1:
                self.turn += roll
                print(f"Computer score is {self.turn}")
            if self.score >= 20:
                # play should return to player here?
                self.round()
        else:
            print("PIG")
            self.turn = 0
            self.score += self.turn


Pig()
