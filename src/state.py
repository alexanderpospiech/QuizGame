
class State(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self):
        print 'Processing current state:', str(self)

    def on_event(self, event):
        """
        Handle events that are delegated to this State.
        """
        pass

    #def process(self, quiz):
    #    """
    #    Do some logic before displaying.
    #    """
    #    pass


    def get_message(self):
        """
        What to show, when the state is active.
        """
        pass

    def get_options_message(self):
        """
        Which options are available.
        """
        pass

    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__
