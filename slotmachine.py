from random import choices


class SlotMachine:
    faces = [['dino', '🦖', 20], ['bear', '🧸', 10], ['trophy', '🏆', 5]]

    def spin(self):
        row = choices(self.faces, k=3)
        return row

    def payout(self, row, bet):
        if row[0][0] == row[1][0] and row[1][0] == row[2][0]:
            print("Ding ding ding!")

            print("You won {}".format(row[0][2] * bet))
            return row[0][2] * bet

        return 0
