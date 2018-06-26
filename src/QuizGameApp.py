import os 

from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window
from kivy.logger import Logger
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

from states import *

class QuizGame(Widget):

    """ 
    A kivy app that contains a simple state machine.
    """

    """ Current state of the game """
    state = GameInitState()

    message = StringProperty()
    options_message = StringProperty()

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)

    def update_messages(self):
        self.message = self.state.get_message()
        self.options_message = self.state.get_options_message()

    ### INTERPRETING KEYBOARD CLICKS ###

    def __init__(self, **kwargs):        
        super(QuizGame, self).__init__(**kwargs)
        Logger.debug("QuizGame __init__")
        self.update_messages()        
        
        """ Initialize the components. """
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            # If it exists, this widget is a VKeyboard object which you can use
            # to change the keyboard layout.
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)        

    def _keyboard_closed(self):
        Logger.debug('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        Logger.debug('The key' + str(keycode) + 'has  been pressed')
        Logger.debug(' - text is %r' % text)
        Logger.debug(' - modifiers are %r' % modifiers)

        # Keycode is composed of an integer + a string
        # If we hit escape, release the keyboard
        if keycode[1] == 'escape':
            keyboard.release()

        self.on_event(text)

        self.update_messages()

        # Return True to accept the key. Otherwise, it will be used by
        # the system.
        return True

    ### INTERPRETING MOUSE CLICKS ###

    def on_touch_down(self, touch):
        Logger.debug(str(touch))

    ###

    def update(self, dt):
        Logger.debug(self.state.get_message())
        Logger.debug(self.state.get_options_message())


class QuizGameApp(App):

    def build(self):
        #game = QuizGame()
        #Clock.schedule_interval(game.update, 1.0 / 60.0)
        return QuizGame()

if __name__ == '__main__':
    print("set config")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("use " + dir_path + "/../config.ini")
    Config.read(dir_path + "/../config.ini")
    Config.set('kivy', 'log_dir', dir_path + "/../logs")
    QuizGameApp().run()
