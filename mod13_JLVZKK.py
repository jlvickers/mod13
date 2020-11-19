import unittest
import datetime
from SymbolInput import SymbolInput
from ChartTypeInput import ChartTypeInput
from TimeSeriesInput import TimeSeriesInput
from startDateInput import StartDateInput
from EndDateInput import EndDateInput
from Constants import Constants

class TestInputs(unittest.TestCase):

    def test_symbols(self):
        symb = SymbolInput()
        self.assertTrue(symb.isInputValid('A'))
        self.assertTrue(symb.isInputValid('AA'))
        self.assertTrue(symb.isInputValid('AAA'))
        self.assertTrue(symb.isInputValid('ACCO'))
        self.assertTrue(symb.isInputValid('AAAAX'))
        self.assertFalse(symb.isInputValid('AMTG$A'))
        self.assertFalse(symb.isInputValid('AAAAAAA'))
    
    def test_ChartType(self):
        chart = ChartTypeInput()
        self.assertTrue(chart.isInputValid("1"))
        self.assertTrue(chart.isInputValid("2"))
    
    def test_TimeSeries(self):
        ts = TimeSeriesInput()
        self.assertTrue(ts.isInputValid(1))
        self.assertTrue(ts.isInputValid(2))
        self.assertTrue(ts.isInputValid(3))
        self.assertTrue(ts.isInputValid(4))

    def test_startDate(self):
        sd = StartDateInput()
        self.assertTrue(sd.isInputValid("1999-06-29"))

    def test_endDate(self):
        ed = EndDateInput("1999-06-29")
        self.assertTrue(ed.isInputValid("1999-07-01"))

if __name__ == "__main__":
    unittest.main()