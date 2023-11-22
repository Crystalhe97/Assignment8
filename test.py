import unittest
from game import Board, Game, HumanPlayer, BotPlayer

class TestBoard(unittest.TestCase):
    def test_board(self):
        board = Board()
        self.assertEqual(board.board, [" "]*9) # Check if the board is initialized with empty spaces

class TestGame(unittest.TestCase):
    def test_game_with_two_players(self):
        # Create a game with two human players
        player1 = HumanPlayer("X")
        player2 = HumanPlayer("O")
        game = Game(player1, player2)
        # Check the game is initialized with two human players
        self.assertIsInstance(game.player1, HumanPlayer)
        self.assertIsInstance(game.player2, HumanPlayer)

    def test_game_with_one_player(self):
        # Create a game with one human player and one bot player
        player1 = HumanPlayer("X")
        player2 = BotPlayer("O")
        game = Game(player1, player2)
        # Check the game is initialized with one human player and one bot player
        self.assertIsInstance(game.player1, HumanPlayer)
        self.assertIsInstance(game.player2, BotPlayer)

class TestPlayer(unittest.TestCase):
    def test_player_symbol(self):
        player1 = HumanPlayer('X')
        player2 = BotPlayer('O')
        # Check if each player is assigned a unique symbol "X" or "O"
        self.assertEqual(player1.symbol, 'X')
        self.assertEqual(player2.symbol, 'O')

class TestPlayerTurns(unittest.TestCase):
    def test_player_turn_switching(self):
        # Create a game with two human players
        player1 = HumanPlayer('X')
        player2 = HumanPlayer('O')
        game = Game(player1, player2)
        # Let player1 starts the game
        self.assertEqual(game.current_player, player1)

        #Switch the turn
        game.switch_player()
        # Check if the turn has switched to player2
        self.assertEqual(game.current_player, player2)

        #Switch the turn
        game.switch_player()
        # Check if the turn has switched back to player1
        self.assertEqual(game.current_player, player1)

class TestGameEnd(unittest.TestCase):
    def test_check_winner(self):
        board = Board()
        board.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(board.check_winner('X')) # Test a winning condition in a ro

        board.board = ['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']  
        self.assertTrue(board.check_winner('O')) # Diagonal winning condition

    def test_is_full(self):
        #Test draw condition
        board = Board()
        board.board = ['X', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O']
        self.assertTrue(board.is_full()) # Full board condition

        board.board = ['X', 'O', 'X', 'X', 'O', 'X', 'O', ' ', ' ']
        self.assertFalse(board.is_full()) # Not full

class TestValidMoves(unittest.TestCase):
    def test_make_valid_move(self):
        # Test making a valid move on the board
        board = Board()
        self.assertTrue(board.make_move(0, 'X')) # Make a Valid move
        self.assertEqual(board.board[0], 'X') # Check if move is successfully made

    def test_make_invalid_move(self):
        # Test making an invalid move on a space which has already occupied or outside the board
        board = Board()
        board.make_move(0, 'X') # Placcing on position 0
        self.assertFalse(board.make_move(0, 'O')) # Try placing on an already occupied spot
        self.assertFalse(board.make_move(9, 'X')) # Try placing on an invalid position


class TestGameWinner(unittest.TestCase):
    def test_check_winner(self):
        board = Board()

        board.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(board.check_winner('X')) # Check playerX is the winner

        board.board = ['O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(board.check_winner('O')) # Check playerO is the winner

        board.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertTrue(board.check_winner('X'))

        board.board = ['X', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'O']
        self.assertFalse(board.check_winner('X')) # Check draw

if __name__ == '__main__':
    unittest.main()