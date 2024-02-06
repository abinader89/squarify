import random
import csv


class SquareFormatter:
    def __init__(self):
        self.members = []

    def add_member(self):
        name = input("input name: ")
        entries = int(input("input entries for {0}: ".format(name)))

        for entries in range(entries):
            self.members.append(name)

    def print_list(self):
        print(self.members)

    def randomize_list(self):
        random.shuffle(self.members)

    def list_to_csv(self):
        with open('squares.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            if len(self.members) > 100:
                raise RuntimeError("Too many squares defined!")

            if len(self.members) < 100:
                print("squares defined: {0}".format(len(self.members)))
                complement = 100 - len(self.members)
                print("adding {0} entries...".format(complement))

                for ii in range(complement):
                    self.members.append("*")

            for ii in range(0, len(self.members), 10):
                row = self.members[ii:ii + 10]
                writer.writerow(row)

            print("data formatted successfully!\nexiting...")
