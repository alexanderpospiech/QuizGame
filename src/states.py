from quiz_game_state import QuizGameState
from sets import Set

class GameInitState(QuizGameState):
    """
    Everybody should answer as fast as they can.
    """

    def get_message(self):
        return """
        MusicGame by Alex
        Which controller is active?
        """

    def get_options_message(self):
        player_list = list(self.get_active_players())
        enough_players_message = "All players attending? (y)"
        return """
            Buzz now to attend the game? (""" + str(player_list) + """)
            """ + (enough_players_message if len(player_list) >= 2 else " ") + """
        """

    def on_event(self, event):        
        player_list = self.get_active_players()
        if event in self.get_possible_players():
            self.add_active_player(event)
            #self.update_messages()
        elif len(player_list) >= 2 and event == 'y': 
            return WelcomeState(self)
        return self

class WelcomeState(QuizGameState):
    """
    Everybody should answer as fast as they can.
    """

    def __init__(self, previous_state = None):
        QuizGameState.__init__(self, previous_state)
        assert len(self.get_active_players()) >= self.minimum_number_of_players,  "#active_players: %r, #minimum_number_of_players: %r" % (len(self.get_active_players()), self.minimum_number_of_players)

    def get_message(self):
        welcome_players_message = ""
        for player in self.get_active_players():
            welcome_players_message += "Player " + player + "\n"
        return """
            Welcome
            """ + welcome_players_message + """
        """

    def get_options_message(self):
        return """
            Begin the game? (y)
        """

    def on_event(self, event):
        if event == 'y': 
            return EveryOneReadyState(self)
        return self

class EveryOneReadyState(QuizGameState):
    """
    The screen, where everybody is asked to acknowledge readiness.
    """

    default_state = False
    ready_players = {}

    def __init__(self, previous_state = None):
        QuizGameState.__init__(self, previous_state)
        assert len(self.get_active_players()) >= self.minimum_number_of_players,  "#active_players: %r, #minimum_number_of_players: %r" % (len(self.get_active_players()), self.minimum_number_of_players)
        for player in self.get_active_players():
            self.ready_players[player] = self.default_state

    def get_message(self):
        players_status = ""
        for player in self.ready_players:
            players_status += "Player " + player + " is" + (" ready " if self.ready_players[player] else " not ready") + "\n"
        return """
            Are you all ready?            
            """ + players_status + """
        """

    def get_options_message(self):
        player_list = list(self.get_active_players())
        return """
            Please press your red buzzer! (""" + str(player_list) + """)
        """

    def clear(self):
        for player in self.ready_players:            
            self.ready_players[player] = self.default_state

    def all_players_active(self):
        all_players_active = True
        for player in self.ready_players:
            all_players_active = all_players_active & self.ready_players[player]
        return all_players_active

    def on_event(self, event):
        if event in self.get_active_players():
            self.ready_players[event] = True
            #self.update_messages()
        if self.all_players_active():
            self.clear()
            return GameRoundState(self)

        return self

class GameRoundState(QuizGameState):
    """
    Everybody should answer as fast as they can.
    """

    def __init__(self, previous_state = None):
        QuizGameState.__init__(self, previous_state)
        assert len(self.get_active_players()) >= self.minimum_number_of_players, "#active_players: %r, #minimum_number_of_players: %r" % (len(self.get_active_players()), self.minimum_number_of_players)

    def get_message(self):
        return """
        This is the question!
        """

    def get_options_message(self):
        player_list = list(self.get_active_players())
        return """
            Buzz now to answer first? (""" + str(player_list) + """)
            Cancel round? (c)
        """

    def on_event(self, event):
        if event in self.get_active_players():
            return AnswerState(event, self)
        elif event == 'c':            
            return CancelRoundSplashState(self)
        return self

class AnswerState(QuizGameState):
    """
    Please tell the answer now
    """

    player = None

    def __init__(self, player, previous_state = None):
        QuizGameState.__init__(self, previous_state)
        assert player in self.get_active_players(), "player: %r, active_players: %r" % (player, self.get_active_players())
        self.player = player

    def get_message(self):
        return """
            Player """ + self.player + """ gives the answer!
        """

    def get_options_message(self):
        return """
            Correct answer? (y)
            Wrong answer? (n)
            Cancel round? (c)
        """

    def on_event(self, event):
        if event == 'y':            
            return CorrectAnswerSplashState(self)
        elif event == 'n':            
            return GameRoundState(self)
        elif event == 'c':            
            return CancelRoundSplashState(self)

        return self

class CorrectAnswerSplashState(QuizGameState):
    """
    Everybody should answer as fast as they can.
    """    

    player = None

    def __init__(self, player, previous_state = None):
        QuizGameState.__init__(self, previous_state)
        assert player in self.get_active_players(), "player: %r, active_players: %r" % (player, self.get_active_players())
        self.player = player
        self.increase_score(self.player)
        super(CorrectAnswerSplashState, self).__init__(self)

    def get_message(self):
        current_score = ""
        scores = self.get_scores()
        for player in scores:
            current_score += "Player " + player + " has " + str(scores[player]) + "\n"
        return """
            Great answer! 
            Player """ + self.player + """ got a point!
            Current score:
            """ + current_score + """
        """

    def get_options_message(self):
        return """
            Next round? (y)
            Cancel? (c)
        """

    def on_event(self, event):
        if event == 'y':
            return EveryOneReadyState(self)
        elif event == 'c':            
            return CancelRoundSplashState(self)

        return self

class CancelRoundSplashState(QuizGameState):
    """
    Everybody should answer as fast as they can.
    """
    
    def get_message(self):
        return """
            Round canceled
        """

    def get_options_message(self):
        return """
            Canceled. Next round? (y)
        """

    def on_event(self, event):
        if event == 'y':
            return EveryOneReadyState(self)

        return self
