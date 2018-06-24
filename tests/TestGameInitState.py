import sys
sys.path.append('../src')
import unittest
from states import GameInitState, WelcomeState

class TestGameInitState(unittest.TestCase):

    state = None

    def setUp(self):
        self.state = GameInitState()

    def test_display_initial(self):
        message = self.state.display()
        self.assertIn('active?', message)

    def test_options_initial(self):
        message = self.state.options()
        self.assertIn('attend', message)
        self.assertIn('([])', message)
        self.assertNotIn('All', message)

    def test_options_add_one_player(self):
        self.state.add_active_player("1")
        message = self.state.options()
        self.assertIn('attend', message)
        self.assertIn('([\'1\'])', message)
        self.assertNotIn('All', message)

    def test_options_add_two_player(self):
        self.state.add_active_player("1")
        self.state.add_active_player("2")
        message = self.state.options()
        self.assertIn('attend', message)
        self.assertIn('([\'1\', \'2\'])', message)
        self.assertIn('All', message)

    def test_options_add_invalid_player(self):
        with self.assertRaises(ValueError):
            self.state.add_active_player("x")

    def test_on_event_initial_valid_event_new_active_player(self):
        self.assertEquals(0, len(self.state.get_active_players()))
        result_state = self.state.on_event("1")
        self.assertEquals(1, len(self.state.get_active_players()))
        self.assertIn('1', self.state.get_active_players())

    def test_on_event_initial_valid_event_two_new_active_player(self):
        self.assertEquals(0, len(self.state.get_active_players()))
        result_state = self.state.on_event("1")
        result_state = result_state.on_event("2")
        self.assertEquals(2, len(self.state.get_active_players()))
        self.assertIn('2', self.state.get_active_players())

    def test_on_event_initial_valid_event_two_new_active_player_and_begin(self):
        self.assertEquals(0, len(self.state.get_active_players()))
        result_state = self.state.on_event("1")
        result_state = result_state.on_event("2")
        self.assertEquals(2, len(self.state.get_active_players()))
        self.assertIn('2', self.state.get_active_players())
        result_state = result_state.on_event("y")
        self.assertEquals(WelcomeState.__name__, result_state.__class__.__name__)

    def test_on_event_initial_invalid_event(self):
        self.assertEquals(0, len(self.state.get_active_players()))
        result_state = self.state.on_event("o")
        self.assertEquals(0, len(self.state.get_active_players()))

if __name__ == '__main__':
    unittest.main()
