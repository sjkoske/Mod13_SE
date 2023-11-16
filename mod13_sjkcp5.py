import unittest
from StockDataAnalyzer import validate_stock_name
from StockDataAnalyzer import validate_time_series
from StockDataAnalyzer import validate_date
from StockDataAnalyzer import validate_date_range
from StockDataAnalyzer import validate_chart_type

class Unittesting(unittest.TestCase):

    def test_stock_name(self):
        #Arrange
        name = "ASDF"
        #Act
        result = validate_stock_name(name)
        #Assert
        self.assertEqual(result,True)
    
    def test_time_series(self):
        #arrange
        series = "1"
        #Act
        result = validate_time_series(series)
        #assert
        self.assertEqual(result,True)

    def test_date_range(self):
        #arrange
        startdate = "1999-11-10"
        enddate = "1999-11-20"
        #Act
        result = validate_date_range(startdate,enddate)
        #Assert
        self.assertEqual(result,True)

    def test_chart_type(self):
        #arrange 
        type = "3"
        #Act
        result = validate_chart_type(type)
        #Assert
        self.assertEqual(result,False)
    
    def test_date(self):
        #arrange
        date = "199-20-20"
        #Act
        result = validate_date(date)
        self.assertEqual(result,False)

    

if __name__ == "__main__":
    unittest.main()