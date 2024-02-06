from SquareFormatter import SquareFormatter


def main():
    formatter = SquareFormatter()
    nn = int(input("enter number of participants: "))
    for ii in range(nn):
        formatter.add_member()

    formatter.randomize_list()
    formatter.list_to_csv()


if __name__ == '__main__':
    main()
