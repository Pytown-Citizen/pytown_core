import unittest
from pytown_core.patterns.behavioral import FSM, IState


class FSM_test(unittest.TestCase):
    def setUp(self):
        self.fsm = fsm()

    def test_fsm_init(self):
        self.fsm.do()
        self.fsm.do()
        self.fsm.do()
        self.fsm.do()
        self.fsm.do()
        self.assertEqual(self.fsm.letters_list, ["A", "B", "C", "B", "C"])


class fsm(FSM):
    def __init__(self):
        FSM.__init__(self, StateA)
        self.letters_list = []


# State scheme is : A => B => C => B


class StateA(IState):
    def do(self):
        self._fsm.letters_list.append("A")
        self.set_state(StateB)


class StateB(IState):
    def do(self):
        self._fsm.letters_list.append("B")
        self.set_state(StateC)


class StateC(IState):
    def do(self):
        self._fsm.letters_list.append("C")
        self.set_state(StateB)
