from state import State
from sets import Set

class QuizGameState(State):

    active_players = None
    scores = None

    minimum_number_of_players = 2

    message = None
    options_message = None
    
    def __init__(self, previous_state = None):
        """ Initialize the components. """
        if previous_state == None:
            self.active_players = Set()
            self.scores = {}
        else:
            self.active_players = previous_state.active_players
            self.scores = previous_state.scores
        #self.update_messages()

    def update_messages(self):        
        #message = self.message()
        #options_message = self.options_message()
        pass

    def add_active_player(self, active_player):
        if not active_player in self.get_possible_players():
            raise ValueError("Provided active_player not in set of possible players. provided: " + active_player + " possible: " + str(self.get_possible_players()))
        self.active_players.add(active_player)
        self.scores[active_player] = 0

    def get_active_players(self):
        return self.active_players

    def get_possible_players(self):
        return ["1", "2", "3", "4"]

    def get_scores(self):
        return self.scores

    def increase_score(self, player):
        self.scores[player] = self.scores[player] + 1
