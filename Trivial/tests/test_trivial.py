#!/usr/bin/env python3

import unittest
from tmc import points
from Trivial.trivial import Trivial

@points("trivial")
class TestTrivial(unittest.TestCase):

    @points("1.1", "1.2")
    def test_trivial(self):
        self.assertEqual(1, Trivial.trivial())

    @points("2.1", "2.2")
    def test_trivial2(self):
        self.assertEqual(1, Trivial.trivial())

    @points("3")
    def test_trivial3(self):
        self.assertEqual(10, Trivial.trivial())

    @points("4.1", "4.2", "4.3")
    def test_trivial4(self):
        self.assertEqual(2, Trivial.trivial(), "Failed due to being failure")

    @points("5.1", "5.2", "5.3")
    def test_trivial5(self):
        self.assertEqual(2, Trivial.trivial2(), "Failed due to being failure")

    @points("5.1", "5.2", "5.3")
    def test_trivial6(self):
        self.assertEqual(2, Trivial.trivial3(), "Failed due to being failure")

    @points("5.1", "5.2", "5.3")
    def test_trivial7(self):
        self.assertEqual(2, Trivial.trivial4(), "Failed due to being error message test")
