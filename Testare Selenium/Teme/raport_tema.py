import unittest
from tema9 import Login
import HtmlTestRunner

class TestSuite(unittest.TestCase):
    def test_suite(self):
        test_derulat = unittest.TestSuite()
        test_derulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Login))
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title="My First Report", report_name="My First Report Name")
        runner.run(test_derulat)