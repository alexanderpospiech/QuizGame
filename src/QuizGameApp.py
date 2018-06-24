import logging

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget

from states import *

class QuizGame(Widget):

    """ 
    A kivy app that contains a simple state machine.
    """

    """ Current state of the game """
    state = GameInitState()

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)

    ### INTERPRETING KEYBOARD CLICKS ###

    def __init__(self, **kwargs):
        logging.debug("QuizGame __init__")
        super(QuizGame, self).__init__(**kwargs)
        
        """ Initialize the components. """
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            # If it exists, this widget is a VKeyboard object which you can use
            # to change the keyboard layout.
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)        

    def _keyboard_closed(self):
        logging.debug('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        logging.debug('The key', keycode, 'has  been pressed')
        logging.debug(' - text is %r' % text)
        logging.debug(' - modifiers are %r' % modifiers)

        # Keycode is composed of an integer + a string
        # If we hit escape, release the keyboard
        if keycode[1] == 'escape':
            keyboard.release()

        print(self.state.display())
        print(self.state.options())
        self.on_event(text)
        
        # Return True to accept the key. Otherwise, it will be used by
        # the system.
        return True

    ### INTERPRETING MOUSE CLICKS ###

    def on_touch_down(self, touch):
        print(touch)


class QuizGameApp(App):
    def build(self):
        return QuizGame()

if __name__ == '__main__':
    QuizGameApp().run()
