from time import sleep

class checkoutbuying(object):
    def __init__(self, chrome):
        self.chrome = chrome
        self.success = None

    def firstproduct(self, product_choiced):

        self.product_choiced_name = str(self.chrome.find_element_by_xpath(product_choiced).get_attribute('textContent'))
        self.chrome.find_element_by_xpath(product_choiced).click()
        self.chrome.save_screenshot("screenshots\\04-selected_product.png")

        return self.product_choiced_name

    def check_product(self, productselected):
        productincart = self.chrome.find_element_by_xpath('//*[@id="inventory_item_container"]/div/div/div/div[1]') \
            .get_attribute('textContent')

        if productselected == productincart:
            print('The product matches!')
            return True
        else:
            print("Recheck your cart, the product doesn't match!")
            self.chrome.save_screenshot("screenshots\\05-product_does_not_match.png")
            self.chrome.find_element_by_xpath('//*[@id="inventory_item_container"]/div/button').click()
            return False

    def addtocart(self):
        self.chrome.save_screenshot("screenshots\\05-product_matches.png")
        self.chrome.find_element_by_xpath('//*[@id="inventory_item_container"]/div/div/div/button').click()
        self.chrome.find_element_by_id('shopping_cart_container').click()


    def addnewproduct(self):
        sleep(1)
        self.chrome.find_element_by_xpath('//*[@id="cart_contents_container"]/div/div[2]/a[1]').click()
        self.chrome.find_element_by_xpath('//*[@id="item_0_title_link"]/div').click()
        self.chrome.find_element_by_xpath('//*[@id="inventory_item_container"]/div/div/div/button').click()

        self.chrome.find_element_by_xpath('//*[@id="shopping_cart_container"]/a').click()
        self.chrome.save_screenshot('screenshots\\06-newproduct.png')


    def checkout_success(self, firstname, lastname, zipcode):
        itemsincontainer = self.chrome.find_element_by_xpath('//*[@id="shopping_cart_container"]/a/span') \
            .get_attribute('textContent')

        if itemsincontainer == '2':
            print('Have 2 items in the container')
            self.chrome.save_screenshot('screenshots\\06-two_items_container.png')
        else:
            print('Do not have 2 items in the container')

        self.chrome.find_element_by_class_name('btn_action').click()
        self.chrome.save_screenshot("screenshots\\07-click_in_cart.png")
        self.chrome.find_element_by_id("first-name").send_keys(firstname)
        self.chrome.find_element_by_id("last-name").send_keys(lastname)
        self.chrome.find_element_by_id("postal-code").send_keys(zipcode)
        self.chrome.find_element_by_xpath("//input[@class='btn_primary cart_button']").click()
        self.chrome.save_screenshot("screenshots\\08-finish_buying.png")
        self.chrome.find_element_by_class_name('btn_action').click()

        self.success = str(self.chrome.find_element_by_xpath('//*[@id="checkout_complete_container"]/h2')
                           .get_attribute('textContent'))

        if self.success == 'THANK YOU FOR YOUR ORDER':
            print('Order finished with success.')

            sleep(2)
            self.chrome.save_screenshot("screenshots\\09-done_success.png")
            self.chrome.find_element_by_xpath('//*[@id="menu_button_container"]/div/div[3]/div/button').click()
            sleep(1)
            self.chrome.find_element_by_id('inventory_sidebar_link').click()

            self.chrome.save_screenshot("screenshots\\09-done_success.png")
        else:
            print('Order fail.')
            self.chrome.save_screenshot("screenshots\\09-done_fail.png")

    def checkoutfail(self, lastname, zipcode):
        self.chrome.find_element_by_class_name('btn_action').click()
        self.chrome.save_screenshot("screenshots\\11-click_in_cart_second_item.png")

        self.chrome.find_element_by_id("last-name").send_keys(lastname)
        self.chrome.find_element_by_id("postal-code").send_keys(zipcode)
        self.chrome.find_element_by_xpath("//input[@class='btn_primary cart_button']").click()

        print('ERRO: FIRST NAME IS REQUIRED')
        self.chrome.save_screenshot("screenshots\\12-fail_firstname.png")