import sys
sys.path.append('../src')
import unittest
from quiz_game import QuizGame
from quiz_game_state import QuizGameState
from states import EveryOneReadyState, GameRoundState

class TestEveryOneReadyStateState(unittest.TestCase):

    state = None

    def setUp(self):
        previous_state = QuizGameState()
        previous_state.add_active_player("1")
        previous_state.add_active_player("2")
        self.state = EveryOneReadyState(previous_state)

    def test_display_initial(self):      
        message = self.state.display()
        self.assertIn('Player 1 is not ready', message)
        self.assertNotIn('Player 1 is ready', message)
        self.assertIn('Player 2 is not ready', message)
        self.assertNotIn('Player 2 is ready', message)
        self.state.on_event("1")
        message = self.state.display()
        self.assertNotIn('Player 1 is not ready', message)
        self.assertIn('Player 1 is ready', message)
        self.assertIn('Player 2 is not ready', message)
        self.assertNotIn('Player 2 is ready', message)

    def test_options_initial(self):
        message = self.state.options()
        self.assertIn('red buzzer!', message)        
        self.assertIn('1', message)
        self.assertIn('2', message)

    def test_clear(self):      
        message = self.state.display()
        self.assertIn('Player 1 is not ready', message)
        self.assertNotIn('Player 1 is ready', message)
        self.assertIn('Player 2 is not ready', message)
        self.assertNotIn('Player 2 is ready', message)
        self.state.on_event("1")
        message = self.state.display()
        self.assertNotIn('Player 1 is not ready', message)
        self.assertIn('Player 1 is ready', message)
        self.assertIn('Player 2 is not ready', message)
        self.assertNotIn('Player 2 is ready', message)
        self.state.clear()
        message = self.state.display()
        self.assertIn('Player 1 is not ready', message)
        self.assertNotIn('Player 1 is ready', message)
        self.assertIn('Player 2 is not ready', message)
        self.assertNotIn('Player 2 is ready', message)

    def test_all_players_active(self):      
        self.assertEquals(False, self.state.all_players_active())
        self.state.ready_players["1"] = True
        self.assertEquals(False, self.state.all_players_active())
        self.state.ready_players["2"] = True
        self.assertEquals(True, self.state.all_players_active())

    def test_on_event_invalid_input(self):
        self.assertEquals(False, self.state.all_players_active())
        self.assertEquals(False, self.state.ready_players["1"])
        self.assertEquals(False, self.state.ready_players["2"])
        self.state.on_event("x")
        self.assertEquals(False, self.state.all_players_active())
        self.assertEquals(False, self.state.ready_players["1"])
        self.assertEquals(False, self.state.ready_players["2"])

    def test_on_event_first_player(self):
        self.assertEquals(False, self.state.all_players_active())
        self.assertEquals(False, self.state.ready_players["1"])
        self.assertEquals(False, self.state.ready_players["2"])
        self.state.on_event("1")
        self.assertEquals(False, self.state.all_players_active())
        self.assertEquals(True, self.state.ready_players["1"])
        self.assertEquals(False, self.state.ready_players["2"])

    def test_on_event_second_player(self):
        self.assertEquals(False, self.state.all_players_active())
        self.assertEquals(False, self.state.ready_players["1"])
        self.assertEquals(False, self.state.ready_players["2"])
        self.state.on_event("1")
        self.assertEquals(False, self.state.all_players_active())
        self.assertEquals(True, self.state.ready_players["1"])
        self.assertEquals(False, self.state.ready_players["2"])
        return_state = self.state.on_event("2")
        self.assertEquals(GameRoundState.__name__, return_state.__class__.__name__)
        self.assertEquals(False, self.state.ready_players["1"])
        self.assertEquals(False, self.state.ready_players["2"])
