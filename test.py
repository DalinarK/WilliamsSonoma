import unittest
from pages import MainPage
from selenium import webdriver

class testCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Python34\\chromedriver.exe")
        self.driver.get("http://www.williams-sonoma.com")

    def test_full_suite(self):
        self.page_loaded_test()
        self.choose_cookware_test()
        self.choose_kettle_category_test()
        self.choose_a_kettle_test()
        self.save_for_later_test()

    def page_loaded_test(self):
        print("Testing home page loads up")
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())
        print("")

    def choose_cookware_test(self):
        print ("Testing navigating to category")
        page = MainPage(self.driver)
        self.assertTrue(page.choose_cookware())
        print("")

    def choose_kettle_category_test(self):
        print("Testing navigating to kettles")
        page = MainPage(self.driver)
        self.assertEqual(page.choose_item_category("a[href='http://www.williams-sonoma.com/shop/cookware/teakettles/?cm_type=lnav']"), "Tea Kettles")
        print("")

    def choose_a_kettle_test(self):
        print ("Testing tea kettle selection")
        page = MainPage(self.driver)
        self.assertEqual(page.choose_specific_item(), "Shopping Cart")
        print("")

    def save_for_later_test(self):
        print ("Testing save for later")
        page = MainPage(self.driver)
        itemList = page.save_for_later()
        self.assertEqual(itemList[0], itemList[1])
        print("")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
   unittest.main()