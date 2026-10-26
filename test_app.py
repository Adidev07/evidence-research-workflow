import unittest
from app import *
class DomainTests(unittest.TestCase):
    def test_valid_quote(self):self.assertTrue(verify({'summary':'ok','evidence':[{'source':'a','quote':'refund'}]},[{'source':'a','text':'refund policy'}]))
    def test_fabricated_quote(self):
        with self.assertRaises(ValueError):verify({'summary':'ok','evidence':[{'source':'a','quote':'free forever'}]},[{'source':'a','text':'refund policy'}])
    def test_missing_evidence(self):
        with self.assertRaises(ValueError):verify({'summary':'ok','evidence':[]},[])
