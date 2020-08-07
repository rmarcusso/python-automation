from driver.WebdriverChrome import Webdriver
from model.auth import authentication
from parameters.ReadParams import ReadParams
from model.CheckoutBuying import checkoutbuying
import requests


if __name__ == "__main__":
    params = ReadParams().reader()
    chrome = Webdriver(params['driver'], params['url']).chrome()
    login = authentication(chrome, params['username'], params['password']).auth()
    addingtocart = checkoutbuying(chrome).firstproduct(params['product_choiced'])
    matchproduct = checkoutbuying(chrome).check_product(addingtocart)

    if matchproduct:
        checkoutbuying(chrome).addtocart()

    newproduct = checkoutbuying(chrome).addnewproduct()
    checkingcart = checkoutbuying(chrome).checkout_success(params['firstname'], params['lastname'], params['zipcode'])


    addingtocart = checkoutbuying(chrome).firstproduct(params['product_choiced'])
    matchproduct = checkoutbuying(chrome).check_product(addingtocart)

    if matchproduct:
        checkoutbuying(chrome).addtocart()
    checkingcart = checkoutbuying(chrome).checkoutfail(params['lastname'], params['zipcode'])
    chrome.quit()
