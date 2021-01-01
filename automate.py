from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()


def automate_web_form():
    driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
    messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
    messageField.send_keys('Hello World')

    showMessageBtn = driver.find_element_by_xpath('//*[@id="get-input"]/button')
    showMessageBtn.click()


def automate_drag_n_drop():
    driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
    source = driver.find_element_by_xpath('//*[@id="box3"]')
    destination = driver.find_element_by_xpath('//*[@id="box103"]')
    actions = ActionChains(driver)
    actions.drag_and_drop(source,destination).perform()

automate_drag_n_drop()
