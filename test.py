import unittest
from selenium import webdriver
from pages import *
from selenium.webdriver.common.by import By

class testCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Python34\\chromedriver.exe")
        self.driver.get("http://www.williams-sonoma.com")

    def test_page_loaded(self):
        print("Testing home page loads up")
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())
        print("")

    def test_choose_cookware(self):
        print ("Testing navigating to category")
        page = MainPage(self.driver)
        self.assertTrue(page.choose_cookware())
        print("")

    def test_choose_kettle_category(self):
        print("Testing navigating to kettles")
        page = MainPage(self.driver)
        self.assertEqual(page.choose_item_category(), "Tea Kettles")
        print("")

    def test_choose_a_kettle(self):
        print ("Testing tea kettle selection")
        page = MainPage(self.driver)
        self.assertEqual(page.choose_specific_item(), "Shopping Cart")
        print("")

    def test_save_for_later(self):
        print ("Testing save for later")
        page = MainPage(self.driver)
        itemList = page.save_for_later()
        self.assertEqual(itemList[0], itemList[1])
        print("")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
   unittest.main()