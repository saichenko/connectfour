from exceptions import PlaceIsOccupiedError
from game import Board, Player


def main():
    board = Board()
    player_one = Player(name=input("Please enter player one name: "))
    player_two = Player(name=input("Please enter player two name: "))

    current_player = player_one

    while (winner := board.check_winner()) is None:
        print("— " * (len(board.board) ** 2))
        for board_row in board.board:
            print("|", end=" ")
            print(" ".join(map(lambda p: str(p), board_row)))

        print(f"{current_player.name} turn")
        n = int(input("Please enter row number: "))
        m = int(input("Please enter column number: "))
        try:
            board.add_move(player=current_player, n=n, m=m)
        except PlaceIsOccupiedError:
            print("Place is occupied, please try again")
            continue
        if current_player == player_one:
            current_player = player_two
        else:
            current_player = player_one

    print(f"{winner.name} won!")


if __name__ == '__main__':
    main()
