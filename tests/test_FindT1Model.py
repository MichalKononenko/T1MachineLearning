"""
Contains unit tests for :mod:`FindT1Model`
"""
from T1Model import T1Model
import unittest
import mock

__author__ = 'Michal Kononenko'


class TestFindT1Model(unittest.TestCase):

    def setUp(self):
        self.model = T1Model()

    def test_is_instance(self):
        """
        Trivial test that gives coverage something to do
        """
        self.assertIsInstance(self.model, T1Model)
