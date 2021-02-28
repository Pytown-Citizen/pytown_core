import unittest
from pytown_core.patterns.behavioral import IObserver, IObservable, Observable


class ObserverTest(unittest.TestCase):
    def setUp(self):
        self.observable = MyObservable()

        self.observer1 = MyObserver()
        self.observer2 = MyObserver()
        self.observer3 = MyObserver()
        self.observable.attach(self.observer1)
        self.observable.attach(self.observer2)
        self.observable.attach(self.observer3)

    def tearDown(self):
        self.observable.detach(self.observer1)
        self.observable.detach(self.observer2)

    def test_notify(self):
        self.observable.detach(self.observer3)
        self.observable.set_text("TEST")
        self.assertEqual(self.observer1.copytext, "TEST")
        self.assertEqual(self.observer2.copytext, "TEST")
        self.assertEqual(self.observer3.copytext, "None")


class MyObservable(Observable):
    def __init__(self):
        Observable.__init__(self)
        self._text = None

    def get_text(self):
        return self._text

    def set_text(self, text):
        self._text = text
        self.notify()


class MyObserver(IObserver):
    def __init__(self):
        IObserver.__init__(self)

        self.copytext = "None"

    def update(self, observable: IObservable):
        self.copytext = observable.get_text()
