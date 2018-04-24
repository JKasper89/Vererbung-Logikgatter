# -*- coding: utf8 -*-
__version__ = '1.0'
__author__ = 'Jan Kasper(jan.kasper@students.tbs1.de)'

import unittest
import Logfunc
from Logfunc import ANDGate,ORGate,NANDGate

class OrGateTest(unittest.TestCase):

    def testcase_01(self):

        o = ORGate()

        o.Input0 = False

        o.Input1 = False

        o.execute()

        self.assertFalse(o.Output, "Class OrGate: Testcase 1 failed.")



    def testcase_02(self):

        o = ORGate()

        o.Input0 = True

        o.Input1 = False

        o.execute()

        self.assertTrue(o.Output, "Class OrGate: Testcase 2 failed.")



    def testcase_03(self):

        o = ORGate()

        o.Input0 = False

        o.Input1 = True

        o.execute()

        self.assertTrue(o.Output, "Class OrGate: Testcase 3 failed.")



    def testcase_04(self):

        o = ORGate()

        o.Input0 = True

        o.Input1 = True

        o.execute()

        self.assertTrue(o.Output, "Class OrGate: Testcase 4 failed.")






class AndGateTest(unittest.TestCase):

    def testcase_01(self):

        a = ANDGate()



        a.Input0 = False



        a.Input1 = False



        a.execute()



        self.assertFalse(a.Output, "AndGate, Testcase 01 failed!")



    def testcase_02(self):

        a = ANDGate()



        a.Input0 = True



        a.Input1 = False



        a.execute()



        self.assertFalse(a.Output, "AndGate, Testcase 02 failed!")



    def testcase_03(self):

        a = ANDGate()



        a.Input0 = False



        a.Input1 = True



        a.execute()



        self.assertFalse(a.Output, "AndGate, Testcase 03 failed!")



    def testcase_04(self):

        a = ANDGate()



        a.Input0 = True



        a.Input1 = True



        a.execute()



        self.assertTrue(a.Output, "AndGate, Testcase 04 failed!")

class NANDGateTest(unittest.TestCase):

    def testcase_01(self):

        a = NANDGate()



        a.Input0 = False



        a.Input1 = False



        a.execute()



        self.assertTrue(a.Output, "NANDGate, Testcase 01 failed!")



    def testcase_02(self):

        a = NANDGate()



        a.Input0 = True



        a.Input1 = False



        a.execute()



        self.assertTrue(a.Output, "NANDGate, Testcase 02 failed!")



    def testcase_03(self):

        a = NANDGate()



        a.Input0 = False



        a.Input1 = True



        a.execute()



        self.assertTrue(a.Output, "NANDGate, Testcase 03 failed!")



    def testcase_04(self):

        a = NANDGate()



        a.Input0 = True



        a.Input1 = True



        a.execute()



        self.assertFalse(a.Output, "NANDGate, Testcase 04 failed!")

if __name__ == "__main__":

    unittest.main()
