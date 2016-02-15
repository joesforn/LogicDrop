#Foobar.py unit tester
#Matthew Willard

import unittest;

from foobar import FooBar;

class main(unittest.TestCase):
    #Show proof of Success
    def test_divisable_3(self):
        self.assertEqual(FooBar(3).lower(),"foo");
    def test_divisable_5(self):
        self.assertEqual(FooBar(5).lower(),"bar");
    def test_divisable_15(self):
        self.assertEqual(FooBar(15).lower(),"foobar");
    def test_divisable_none(self):
        self.assertEqual(FooBar(2),2);
    #Show proof of failure
    def test_divisable_3_fail(self):
        self.assertEqual(FooBar(3).lower(),"bar");
    def test_divisable_5_fail(self):
        self.assertEqual(FooBar(5).lower(),"foo");
    def test_divisable_15_fail(self):
        self.assertEqual(FooBar(15).lower(),"barfoo");
    def test_divisable_none_fail(self):
        self.assertEqual(FooBar(2),1);

if(__name__ == '__main__'):
    unittest.main();
