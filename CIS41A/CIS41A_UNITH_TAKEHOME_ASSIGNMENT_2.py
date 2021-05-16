"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit H Take-Home Assignment
"""


class BritCoins(object):

    __coinValues = {"pound": 240, "shilling": 12, "penny": 1}

    def __init__(self, **kwargs):
        self.totalPennies = 0
        for key, value in kwargs.items():
            if key == "pound":
                self.totalPennies += value * BritCoins.__coinValues["pound"]
            if key == "shilling":
                self.totalPennies += value * BritCoins.__coinValues["shilling"]
            if key == "penny":
                self.totalPennies += value * BritCoins.__coinValues["penny"]

    def __add__(self, other):
        return BritCoins(penny=self.totalPennies + other.totalPennies)

    def __sub__(self, other):
        return BritCoins(penny=self.totalPennies - other.totalPennies)

    def __str__(self):
        pounds, shillings, pennies = BritCoins.return_proper_coins(self.totalPennies)
        return f"{pounds} pounds {shillings} shillings {pennies} pennies"

    @staticmethod
    def return_proper_coins(penny):
        pounds = penny // BritCoins.__coinValues["pound"]
        reminder_pennies = penny % BritCoins.__coinValues["pound"]
        shillings = reminder_pennies // BritCoins.__coinValues["shilling"]
        pennies = reminder_pennies % BritCoins.__coinValues["shilling"]
        return pounds, shillings, pennies


def main():
    c1 = BritCoins(pound=4, shilling=24, penny=3)
    c2 = BritCoins(pound=3, shilling=4, penny=5)
    c3 = c1 + c2
    c4 = c1 - c2
    print(c1)
    print(c2)
    print(c3)
    print(c4)


if __name__ == '__main__':
    main()


"""
Execution results:

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITH_TAKEHOME_ASSIGNMENT_2.py
5 pounds 4 shillings 3 pennies
3 pounds 4 shillings 5 pennies
8 pounds 8 shillings 8 pennies
1 pounds 19 shillings 10 pennies

Process finished with exit code 0

"""

