import unittest

from pytown_core.runners import MyThread
import logging


class MyThread_test(unittest.TestCase):
    def setUp(self):
        self.subject = Subject()

    def test_my_thread_init(self):
        self.subject.start()
        self.subject.join()

        self.assertEqual(self.subject.compteur, 10)
        self.assertEqual(self.subject.pre_run_message, "PreRun process")
        self.assertEqual(self.subject.post_run_message, "PostRun process")


class Subject(MyThread):
    def __init__(self):
        MyThread.__init__(self, "subject")

        self.compteur = 0
        self.pre_run_message = "None"
        self.post_run_message = "None"

    def do(self):
        if self.compteur < 10:
            self.compteur += 1
        else:
            self.stop()

    def _pre_run(self):
        logging.info("_pre_run")
        self.pre_run_message = "PreRun process"

    def _post_run(self):
        logging.info("_post_run")
        self.post_run_message = "PostRun process"
