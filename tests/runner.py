import unittest

import TestGameInitState
import TestWelcomeState
import TestEveryOneReadyState
import TestGameRoundState
import TestAnswerState
import TestAnswerState
import TestCorrectAnswerSplashState
import TestCancelRoundSplashState

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(TestGameInitState))
suite.addTests(loader.loadTestsFromModule(TestWelcomeState))
suite.addTests(loader.loadTestsFromModule(TestEveryOneReadyState))
suite.addTests(loader.loadTestsFromModule(TestGameRoundState))
suite.addTests(loader.loadTestsFromModule(TestAnswerState))
suite.addTests(loader.loadTestsFromModule(TestCorrectAnswerSplashState))
suite.addTests(loader.loadTestsFromModule(TestCancelRoundSplashState))



# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
