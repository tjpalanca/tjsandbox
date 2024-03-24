from RPA.Browser.Playwright import Playwright

TAX_PAYMENT_PAGE = (
    "https://www.bancnetonline.com/apps/servlet/ServletFront?trxcode=0011"
)

browser = Playwright()
browser.open_browser(url=TAX_PAYMENT_PAGE)
browser.fill_text("#loginid", txt="cbclicerdc")
