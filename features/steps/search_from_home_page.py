from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then("input text '{text}' and click search")
def header_input_text_and_click_search(context, text):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'keywords'))
    )
    element = context.browser.find_element_by_id('keywords')
    element.clear()
    element.send_keys(text)
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button'))
    )
    context.browser.find_element_by_xpath('//button').click()


@then("page include text '{text}'")
def page_include_text(context, text):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[contains(text(), "%s")]' % text))
    )
    assert context.browser.find_element_by_xpath(
        '//*[contains(text(), "%s")]' % text)
