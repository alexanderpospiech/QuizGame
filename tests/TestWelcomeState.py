import sys
sys.path.append('../src')
import unittest
from quiz_game import QuizGame
from quiz_game_state import QuizGameState
from states import WelcomeState, EveryOneReadyState

class TestWelcomeState(unittest.TestCase):

    state = None

    def setUp(self):
        previous_state = QuizGameState()
        previous_state.add_active_player("1")
        previous_state.add_active_player("2")
        self.state = WelcomeState(previous_state)

    def test_display_initial(self):
        message = self.state.display()
        self.assertIn('Welcome', message)
        self.assertIn('Player 1', message)
        self.assertIn('Player 2', message)

    def test_options_initial(self):
        message = self.state.options()
        self.assertIn('Begin', message)

    def test_on_event_begin(self):
        result_state = self.state.on_event("y")
        self.assertEquals(EveryOneReadyState.__name__, result_state.__class__.__name__)

if __name__ == '__main__':
    unittest.main()
