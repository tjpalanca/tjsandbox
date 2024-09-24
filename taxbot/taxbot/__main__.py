from time import sleep

import Browser
import yaml
from Browser.utils.data_types import PageLoadStates, SelectionStrategy

with open("config.yml", "r") as config_file:
    credentials = yaml.safe_load(config_file)["credentials"]

LOGIN_URL = "https://www.bancnetonline.com/apps/servlet/ServletFront?trxcode=0011"
THROTTLE_SECONDS = 3

browser = Browser.Browser()
browser.new_browser(headless=False)

for user, cred in credentials.items():
    # Open a new page to the tax portal
    browser.new_page(LOGIN_URL)
    sleep(THROTTLE_SECONDS)
    browser.wait_for_load_state(PageLoadStates.networkidle)

    # Login to the portal
    browser.set_selector_prefix("frame[name='mainFrame'] >>>")
    browser.fill_text("#loginid", txt=user)
    browser.fill_text("#loginpass", txt=cred["old"]["password"])
    browser.click("input[name='LOGIN']")
    sleep(THROTTLE_SECONDS)
    browser.wait_for_load_state(PageLoadStates.networkidle)

    browser.fill_text("#answer", txt=cred["old"]["challenge"]["answer"])
    browser.click("input[name='SUBMIT']")
    sleep(THROTTLE_SECONDS)
    browser.wait_for_load_state(PageLoadStates.networkidle)

    # Go to change password screen
    browser.set_selector_prefix("frame[name='leftFrame'] >>>")
    browser.click(
        browser.get_element_by(SelectionStrategy("Text"), text="Change Password")
    )
    sleep(THROTTLE_SECONDS)
    browser.wait_for_load_state(PageLoadStates.networkidle)

    # Submit new details
    browser.set_selector_prefix("frame[name='mainFrame'] >>>")

    browser.fill_text("#oldpas", txt=cred["old"]["password"])
    browser.fill_text("#newpas", txt=cred["new"]["password"])
    browser.fill_text("#cnfrmpwd", txt=cred["new"]["password"])

    browser.fill_text("#question", txt=cred["old"]["challenge"]["question"])
    browser.fill_text("#newquestion", txt=cred["new"]["challenge"]["question"])

    browser.fill_text("#oldanswer", txt=cred["old"]["challenge"]["answer"])
    browser.fill_text("#newanswer", txt=cred["new"]["challenge"]["answer"])
    browser.fill_text("#cqconfirmans", txt=cred["new"]["challenge"]["answer"])

    browser.set_selector_prefix("frame[name='bottomFrame'] >>>")
    browser.click("input#btnOk")
    sleep(THROTTLE_SECONDS)
    browser.wait_for_load_state(PageLoadStates.networkidle)

    # Logout
    browser.set_selector_prefix("frame[name='leftFrame'] >>>")
    browser.click(browser.get_element_by(SelectionStrategy("Text"), text="Logout"))
    sleep(THROTTLE_SECONDS)
    browser.wait_for_load_state(PageLoadStates.networkidle)

    # Close page
    browser.close_page()
    sleep(THROTTLE_SECONDS)
