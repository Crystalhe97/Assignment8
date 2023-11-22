import unittest
from game import Board, Game, HumanPlayer, BotPlayer

class TestBoard(unittest.TestCase):
    def test_board(self):
        board = Board()
        self.assertEqual(board.board, [" "]*9) 

class TestGame(unittest.TestCase):
    def test_game_with_two_players(self):
        player1 = HumanPlayer("X")
        player2 = HumanPlayer("O")
        game = Game(player1, player2)
        self.assertIsInstance(game.player1, HumanPlayer)
        self.assertIsInstance(game.player2, HumanPlayer)

    def test_game_with_one_player(self):
        player1 = HumanPlayer("X")
        player2 = BotPlayer("O")
        game = Game(player1, player2)
        self.assertIsInstance(game.player1, HumanPlayer)
        self.assertIsInstance(game.player2, BotPlayer)

class TestPlayer(unittest.TestCase):
    def test_player_symbol(self):
        player1 = HumanPlayer('X')
        player2 = BotPlayer('O')
        self.assertEqual(player1.symbol, 'X')
        self.assertEqual(player2.symbol, 'O')

    def test_different_player_symbols(self):
        player1 = HumanPlayer('X')
        player2 = BotPlayer('O')
        self.assertNotEqual(player1.symbol, player2.symbol)

class TestPlayerTurns(unittest.TestCase):
    def test_player_turn_switching(self):
        player1 = HumanPlayer('X')
        player2 = HumanPlayer('O')
        game = Game(player1, player2)
        self.assertEqual(game.current_player, player1)

        game.switch_player()
        self.assertEqual(game.current_player, player2)

        game.switch_player()
        self.assertEqual(game.current_player, player1)

class TestGameEnd(unittest.TestCase):
    def test_check_winner(self):
        board = Board()
        board.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(board.check_winner('X'))  

        board.board = ['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']  
        self.assertTrue(board.check_winner('O'))

    def test_is_full(self):
        board = Board()
        board.board = ['X', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O']
        self.assertTrue(board.is_full())  

        board.board = ['X', 'O', 'X', 'X', 'O', 'X', 'O', ' ', ' ']
        self.assertFalse(board.is_full()) 

class TestValidMoves(unittest.TestCase):
    def test_make_valid_move(self):
        board = Board()
        self.assertTrue(board.make_move(0, 'X'))  
        self.assertEqual(board.board[0], 'X') 

    def test_make_invalid_move(self):
        board = Board()
        board.make_move(0, 'X')  
        self.assertFalse(board.make_move(0, 'O'))  
        self.assertFalse(board.make_move(9, 'X')) 

class TestGameWinner(unittest.TestCase):
    def test_check_winner(self):
        board = Board()

        board.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(board.check_winner('X'))

        board.board = ['O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', 'O']
        self.assertTrue(board.check_winner('O'))

        board.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertTrue(board.check_winner('X'))

        board.board = ['X', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'O']
        self.assertFalse(board.check_winner('X'))

if __name__ == '__main__':
    unittest.main()