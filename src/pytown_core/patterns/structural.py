from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class IComponent(ABC):
    @property
    def parent(self) -> IComponent:
        return self._parent

    @parent.setter
    def parent(self, parent: IComponent):
        self._parent = parent

    @abstractmethod
    def add(self, component: IComponent) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove(self, component: IComponent) -> None:
        raise NotImplementedError

    @abstractmethod
    def is_composite(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    # TODO : return type should maybe be a bool with an internal error check on the tree
    def operation(self, **kwargs) -> tuple:
        raise NotImplementedError


class IComposite(IComponent):
    def __init__(self) -> None:
        self._children: List[IComponent] = []

    def add(self, component: IComponent) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: IComponent) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self, *args, **kwargs) -> tuple:
        kwargs = self._operation(**kwargs)
        for child in self._children:
            kwargs = child.operation(**kwargs)
        return kwargs

    @abstractmethod
    def _operation(self, **kwargs) -> tuple:
        raise NotImplementedError


class ILeaf(IComposite):
    def add(self, component: IComponent) -> None:
        raise ValueError("Can't add children to a leaf")

    def remove(self, component: IComponent) -> None:
        raise ValueError("Can't remove children to a leaf")

    def is_composite(self) -> bool:
        return False
