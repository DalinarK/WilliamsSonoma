import random
from base import *


class MainPage(Page):
    def check_page_loaded(self):
        # Check to see if the page loaded up properly
        self.remove_pop_ups()
        select = self.driver.find_elements_by_css_selector(".logo-image")
        if len(select) == 1:
            return True
        else:
            return False

    # Get rid of the promotional popup if it appears
    def remove_pop_ups(self):
        select = self.driver.find_elements_by_css_selector(".overlayCloseButton.overlayCloseX")
        if len(select) == 1:
            print ("Removing pop up ad")
            select[0].click()

    # Choose cookware category
    # Output: returns the title of the page clicked
    def choose_cookware(self):
        self.click_item("a[href='http://www.williams-sonoma.com/shop/cookware/?cm_type=gnav']")
        # self.click_item(".topnav-cookware.topnav-cookware_current.active")
        select = self.return_text("a[href='http://www.williams-sonoma.com/shop/cookware/cookware-sets/?cm_type=lnav']")
        return select


    # Choose the tea kettle category
    # Output: returns the title of the item category chosen
    def choose_item_category(self, itemCategory):
        self.click_item(itemCategory)
        select = self.return_text(".shop-title.supersection-title")
        print ("Item page selected: " + select)
        return select

    # Choose and add a a random item to the checkout
    # Output: returns the checkout page header text if it exists
    def choose_specific_item(self):
        # randomly choose an item in the category
        select = self.driver.find_elements_by_css_selector(".product-cell")
        random.seed()
        teaKettleChosen = random.randrange(len(select))
        select = select[teaKettleChosen].find_elements_by_css_selector(".product-name")
        select[0].location_once_scrolled_into_view
        select[0].send_keys("\n")

        # If there is more than one color choice, choose the first color
        select = self.driver.find_elements_by_css_selector(".visual-attributes.graphical-att.resetNoneActive>li:nth-of-type(1)>a:nth-of-type(1)")
        if len(select) == 1:
            select[0].send_keys("\n")
        # Add to cart
        self.click_item(".btn_addtobasket")

        self.driver.implicitly_wait(5)
        select = self.driver.find_elements_by_css_selector("a[href='http://www.williams-sonoma.com/checkout/normal.html']")
        if len(select) == 1:
            select[0].send_keys("\n")
            return self.driver.find_element_by_css_selector(".checkout-page-header").text
        else:
            return None

    # Save the item for later
    # Output: A list that contains the item number of both the item to be saved and the item that was actually saved.
    def save_for_later(self):

        # Extract item number of the item to be saved
        itemSaved = [self.return_text(".cart-table-row-sku")]

        # Click save for later
        select = self.driver.find_elements_by_xpath("//*[contains(text(), 'Save For Later')]")
        select[0].send_keys("\n")

        # Click save for later section
        self.click_item("a[href='#save-for-later-section']")
        # Extract the item number of the item that had been saved.
        itemSaved.append(self.driver.find_element_by_css_selector(".cart-table-row-sku").text)
        return itemSaved
