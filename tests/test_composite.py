import unittest

from pytown_core.patterns.structural import IComposite, ILeaf


class CompositeTest(unittest.TestCase):
    def setUp(self):

        self.c1 = MyComposite("C1")
        self.c2 = MyComposite("C2")
        self.c3 = MyComposite("C3")
        self.l1 = MyLeaf("L1")
        self.l2 = MyLeaf("L2")
        self.l3 = MyLeaf("L3")

    def test_composite(self):
        self.c1.add(self.c2)
        self.c1.add(self.c3)
        self.c2.add(self.l1)
        self.c2.add(self.l2)
        self.c3.add(self.l3)

        text = ""
        kwargs = self.c1.operation(text=text)
        self.assertEqual(kwargs["text"], "C1C2L1L2C3L3")

    def test_composite_with_raising_leaf_ok(self):
        self.raising_leaf = MyRaisingExceptionLeaf("No Raise")

        self.c1.add(self.c2)
        self.c1.add(self.c3)
        self.c2.add(self.l1)
        self.c2.add(self.l2)
        self.c3.add(self.raising_leaf)
        self.c3.add(self.l3)

        text = ""
        kwargs = self.c1.operation(text=text)
        self.assertEqual(kwargs["text"], "C1C2L1L2C3No RaiseL3")

    def test_composite_with_raising_leaf_ko(self):
        self.non_raising_leaf = MyRaisingExceptionLeaf("Not Raising")
        self.raising_leaf = MyRaisingExceptionLeaf("Raise")

        self.c1.add(self.c2)
        self.c1.add(self.c3)
        self.c2.add(self.l1)
        self.c2.add(self.l2)
        self.c3.add(self.raising_leaf)
        self.c3.add(self.l3)

        text = ""
        self.assertRaises(ValueError, self.c1.operation, text=text)


class MyComposite(IComposite):
    def __init__(self, name):
        IComposite.__init__(self)

        self.name = name

    def _operation(self, **kwargs):
        kwargs["text"] += self.name
        return kwargs


class MyLeaf(ILeaf):
    def __init__(self, name):
        ILeaf.__init__(self)

        self.name = name

    def _operation(self, **kwargs):
        kwargs["text"] += self.name
        return kwargs


class MyRaisingExceptionLeaf(ILeaf):
    def __init__(self, name):
        ILeaf.__init__(self)

        self.name = name

    def _operation(self, **kwargs):
        kwargs["text"] += self.name
        if self.name == "Raise":
            raise ValueError("RaisingLeaf Exception raised")
        return kwargs
