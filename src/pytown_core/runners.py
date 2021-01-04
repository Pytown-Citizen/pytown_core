from __future__ import annotations

import logging
import threading as th
from abc import ABC, abstractmethod


class Runnable(ABC):
    def __init__(self):
        ABC.__init__(self)

        self._is_running = False

    @abstractmethod
    def do(self):
        raise NotImplementedError

    # Pre run loop preocesses
    def _pre_run(self):
        pass

    # Post run loop processes
    def _post_run(self):
        pass

    def run(self):
        self._pre_run()
        self._is_running = True
        while self._is_running:
            self.do()

    def stop(self):
        if self._is_running:
            self._post_run()
        self._is_running = False


# NOTA BENE : If you reverse the motherclass order, the underlying thread method start() will not call anymore the Runnable run()
class MyThread(Runnable, th.Thread):
    def __init__(self, name):
        Runnable.__init__(self)
        th.Thread.__init__(self, name=name + "_thread")

    @abstractmethod
    def do(self):
        raise NotImplementedError
