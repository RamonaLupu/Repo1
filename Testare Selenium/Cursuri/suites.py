import unittest
from alerts import Alerts
from context_menu import Context_menu
from firefox_authentication import Firefox
from keys import Key


import HtmlTestRunner

class TestSuite(unittest.TestCase):
    def test_suite(self):
        test_derulat = unittest.TestSuite()
        test_derulat.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
                               unittest.defaultTestLoader.loadTestsFromTestCase(Context_menu),
                               unittest.defaultTestLoader.loadTestsFromTestCase(Firefox),
                               unittest.defaultTestLoader.loadTestsFromTestCase(Key)] )
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title="My First Report", report_name="My First Report Name")
        runner.run(test_derulat)
        # Combine reports ne genereaza un singur raport cu toate rezultatele pentru toate testele
