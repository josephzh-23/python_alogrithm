
'''

What's the anti-diagonal index here and how does this make sense?

1.
self.diag and self.antiDiag: Variables to track the scores of the main diagonal (top-left to bottom-right) and the anti-diagonal (top-right to bottom-left), respectively.

'''

class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize the TicTacToe game board with a given size.
        """
        self.board_size = n
        # self.counters store the counts for (rows, columns, diagonal, anti-diagonal)
        # self.counters[player][i]:
        # i from 0 to n-1 (row counts), i from n to 2*n-1 (column counts),
        # i equals 2*n (main diagonal count), i equals 2*n + 1 (anti-diagonal count)
        # Index 0: player 1, Index 1: player 2
        self.counters = [[0] * (2 * n + 2) for _ in range(2)]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player makes a move at a specified row and column.
        :param row: The row index of the board, 0-indexed.
        :param col: The column index of the board, 0-indexed.
        :param player: The identifier of the player (either 1 or 2).
        :return: The current winning condition, can be either:
                 0: No one wins.
                 1: Player 1 wins.
                 2: Player 2 wins.
        """
        player_index = player - 1  # Convert to 0-indexing for players 1 and 2
        diagonal_index = 2 * self.board_size
        anti_diagonal_index = 2 * self.board_size + 1

        # Update the row, column, and possibly the diagonal counts for the move
        self.counters[player_index][row] += 1  # Row count
        self.counters[player_index][col + self.board_size] += 1  # Column count
        if row == col:
            self.counters[player_index][diagonal_index] += 1  # Diagonal count
        if row + col == self.board_size - 1:
            self.counters[player_index][anti_diagonal_index] += 1  # Anti-diagonal count

        # Check if any count has reached the board size, which means a win.
        if (
            self.counters[player_index][row] == self.board_size
            or self.counters[player_index][col + self.board_size] == self.board_size
            or self.counters[player_index][diagonal_index] == self.board_size
            or self.counters[player_index][anti_diagonal_index] == self.board_size
        ):
            return player  # The current player wins

        # If no win, return 0 indicating no winner yet
        return 0


# Example of how the TicTacToe class is used:
# game = TicTacToe(n)
# result = game.move(row, col, player)
