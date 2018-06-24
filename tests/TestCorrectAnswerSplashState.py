import sys
sys.path.append('../src')
import unittest
from quiz_game import QuizGame
from quiz_game_state import QuizGameState
from states import CorrectAnswerSplashState, EveryOneReadyState, CancelRoundSplashState

class TestCorrectAnswerSplashState(unittest.TestCase):

    state = None

    def setUp(self):
        previous_state = QuizGameState()
        previous_state.add_active_player("1")
        previous_state.add_active_player("2")
        self.state = CorrectAnswerSplashState("1", previous_state)

    def test_display_initial(self):
        message = self.state.display()
        self.assertIn('Great answer', message)
        self.assertIn('Player 1 got', message)
        self.assertIn('Player 1 has 1', message)
        self.assertIn('Player 2 has 0', message)

    def test_options(self):
        message = self.state.options()
        self.assertIn('Next', message)
        self.assertIn('Cancel', message)

    def test_on_event_invalid_input(self):
        result_state = self.state.on_event("x")
        self.assertEquals(self.state, result_state)

    def test_on_event_valid_input_correct(self):
        result_state = self.state.on_event("y")
        self.assertEquals(EveryOneReadyState.__name__, result_state.__class__.__name__)

    def test_on_event_cancel(self):
        result_state = self.state.on_event("c")
        self.assertEquals(CancelRoundSplashState.__name__, result_state.__class__.__name__)

if __name__ == '__main__':
    unittest.main()
