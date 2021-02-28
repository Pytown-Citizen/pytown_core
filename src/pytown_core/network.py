import logging
from queue import Queue
from threading import Thread


class NetworkModule(Thread):
    def __init__(
        self, connexion, receive_queue: Queue, send_queue: Queue, error_queue: Queue
    ):
        Thread.__init__(self)

        self.connexion = connexion

        self._is_running = False

        self._receive_queue = receive_queue
        self._send_queue = send_queue
        self._error_queue = error_queue

        self.receive_process = Thread(
            target=self._receive, name=__name__ + "_receive_process"
        )
        self.send_process = Thread(target=self._send, name=__name__ + "_send_process")

    def run(self):
        self._is_running = True
        self._start_exchange()

        while self._is_running:
            self._check_errors()

        self._stop_exchange()

    def stop(self):
        self._is_running = False
        self.connexion.close()

    def _start_exchange(self):
        self.receive_process.start()
        self.send_process.start()

    def _check_errors(self):
        if not self._error_queue.empty():
            logging.error(self._error_queue.get())

    def _stop_exchange(self):
        self.receive_process.join()
        self.send_process.join()
        # Test add smell

    # SubProcesses methods
    def _receive(self):
        while self._is_running:
            if not self._receive_queue.full():
                try:
                    self._receive_queue.put(self.connexion.recv())
                except Exception:
                    self._error_queue.put(
                        NetworkModuleError(str("Issue during _receive"))
                    )
                    # TODO: raise Exception

    def _send(self):
        while self._is_running:
            if not self._send_queue.empty():
                msg_to_send = self._send_queue.get()
                try:
                    self.connexion.send(msg_to_send)
                except Exception:
                    self._error_queue.put(NetworkModuleError(str("Issue during _send")))
                    # TODO:raise Exception


class NetworkModuleError(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
