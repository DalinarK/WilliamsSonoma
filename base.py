import sys

# This is the base class for all the pages
class Page(object):
    def __init__(self, driver, base_url='http://www.app.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    # Finds an element and returns the accompanying text
    def return_text(self, selectorCriteria):
        return self.driver.find_element_by_css_selector(selectorCriteria).text

    # Clicks an item based on CSS Selector
    # Input: css selector criteria
    # Output: Exits with error code 2 if there isn't exactly 1 selector found
    def click_item(self, selectorCriteria):
        select = self.driver.find_elements_by_css_selector(selectorCriteria)
        if len(select) == 1:
            select[0].send_keys("\n")
            return True
        else:
            print ("CSS_Selector did not select exactly one element")
            sys.exit(2)