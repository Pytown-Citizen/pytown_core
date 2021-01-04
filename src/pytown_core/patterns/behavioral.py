from __future__ import annotations

import logging
from abc import ABC, abstractmethod


class IState(ABC):
    def __init__(self, fsm: FSM):
        ABC.__init__(self)
        self._fsm = fsm

    def set_state(self, state: IState):
        logging.warning(
            "Should avoid to be used, prefered use set_state from fsm method"
        )
        self._fsm.set_state(state)

    def __eq__(self, state):
        return self.__class__.__name__ == state.__name__

    @abstractmethod
    def do(self):
        raise NotImplementedError


class FSM:
    def __init__(self, initial_state: IState):

        self._state = initial_state(self)

    # FSM state delegation #
    def set_state(self, state: IState):
        logging.info("Entering {}".format(state.__name__))
        if self._state != state:
            self._state = state(self)

    def get_state(self):
        return self._state.__class__.__name__

    def do(self):
        self._state.do()


class IObservable(ABC):
    @abstractmethod
    def attach(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def detach(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Observable(IObservable):
    def __init__(self):
        IObservable.__init__(self)

        self._observers = []

    def attach(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def detach(self, observer: IObserver) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)


class IObserver(ABC):
    @abstractmethod
    def update(self, observable: IObservable) -> None:
        pass


class Visitable(ABC):
    @abstractmethod
    def accept_visitor(self, visitor: Visitor) -> None:
        raise NotImplementedError


class Visitor(ABC):

    # Method of visitor depends on the concrete object they are visiting. This has been done for pytown game
    def visit_town(self, visitable: Visitable) -> None:
        raise NotImplementedError

    def visit_tile(self, visitable: Visitable) -> None:
        raise NotImplementedError

    def visit_resource(self, visitable: Visitable) -> None:
        raise NotImplementedError

    def visit_building(self, visitable: Visitable) -> None:
        raise NotImplementedError

    def visit_character(self, visitable: Visitable) -> None:
        raise NotImplementedError


class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError
