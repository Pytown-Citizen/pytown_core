import unittest
from pytown_core.patterns.behavioral import FSM, IState
from pytown_core.runners import MyThread


class FSMThreadTest(unittest.TestCase):
    def setUp(self):
        self.fsm = fsm()

    def test_fsm_init(self):
        self.fsm.start()
        self.fsm.join()
        self.assertEqual(self.fsm.letters_list, ["D", "A", "B", "C", "F"])


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
        self._fsm.stop()
        self.set_state(StateB)


class fsm(FSM, MyThread):
    def __init__(self):
        FSM.__init__(self, StateA)
        MyThread.__init__(self, "fsm")
        self.letters_list = []

    def _pre_run(self):
        FSM._pre_run(self)
        self.letters_list.append("D")

    def _post_run(self):
        FSM._post_run(self)
        self.letters_list.append("F")
