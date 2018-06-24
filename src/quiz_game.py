from states import *
from sets import Set

class QuizGame(object):
    """ 
    A simple state machine that mimics the functionality of a device from a 
    high level.
    """

    state = None

    def __init__(self):
        """ Initialize the components. """
        print("QuizGame __init__")
        self.state = GameInitState()

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)

if __name__ == '__main__':
    quiz = QuizGame()
    while True:
        #quiz.state.process(quiz)
        print(quiz.state.display())
        event = raw_input(quiz.state.options())
        quiz.on_event(event)
