# vim: set et sw=4 ts=4 ai:

import unittest
import utils
from testbin import TestBin

class TestBinCocommand(TestBin, unittest.TestCase):

    def setUp(self):
        self.bin = 'co-command'

    def tearDown(self):
        pass