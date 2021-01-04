from abc import abstractmethod


class IJSONSerializable:

    INDENT = 4

    @classmethod
    @abstractmethod
    def from_json_dict(cls, json_dict):
        raise NotImplementedError

    @abstractmethod
    def to_json_dict(self):
        raise NotImplementedError
